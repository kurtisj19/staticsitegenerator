

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



if __name__ == "__main__":
    node = HTMLNode(tag="a", value="a simple link", props={"href": "https://www.google.com", "target": "_blank"})
    print(node.props_to_html())
    
    leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(leaf_node.to_html())
