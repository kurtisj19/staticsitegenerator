import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        string = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"}).props_to_html()
        string2 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(string, string2)

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        string = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        string2 = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(string, string2)

    def test_to_html_no_tag(self):
        string = LeafNode(tag=None, value="This is a paragraph of text.").to_html()
        string2 = "This is a paragraph of text."
        self.assertEqual(string, string2)


if __name__ == "__main__":
    unittest.main()
