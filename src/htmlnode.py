

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        result = ""
        for key in self.props.keys():
            result += f' {key}="{self.props[key]}"'
        return result
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError('LeafNode requires a value')
        if self.tag is None:
            return self.value
        
        result = f"<{self.tag}"
        if self.props:
            result += self.props_to_html()
        result += f">{self.value}</{self.tag}>"

        return result


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('ParentNode requires a tag')
        if self.children is None:
            raise ValueError('ParentNode requires children')
        
        # Build opening tag
        result = f"<{self.tag}"
        if self.props:
            result += self.props_to_html()
        result += ">"

        # Add children recursively
        for child in self.children:
            result += child.to_html()
        
        return result + f"</{self.tag}>"


if __name__ == "__main__":
    # node = HTMLNode(tag="a", value="a simple link", props={"href": "https://www.google.com", "target": "_blank"})
    # print(node.props_to_html())
    
    # leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    # print(leaf_node.to_html())

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())