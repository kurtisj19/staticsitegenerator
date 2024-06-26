

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


def text_node_to_html_node(text_node):
    # Helper function to convert TextNode to HTMLNode
    
    text_types = ["text", "bold", "italic", "code", "link", "image"]

    text_type = text_node.text_type
    if text_type not in text_types:
        raise Exception("Text node does not have valid text type")
    
    if text_type == "text":
        return LeafNode(value=text_node.text)
    elif text_type == "bold":
        return LeafNode(tag="b", value=text_node.text)
    elif text_type == "italic":
        return LeafNode(tag="i", value=text_node.text)
    elif text_type == "code":
        return LeafNode(tag="code", value=text_node.text)
    elif text_type == "link":
        return LeafNode(tag="a", text=text_node.text, props={"href": text_node.url})
    elif text_type == "image":
        return LeafNode(tag="img", text="", props=
                        {"src": text_node.url, "alt": text_node.text})

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