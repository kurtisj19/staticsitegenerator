import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        string = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        ).to_html()
        string2 = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(string, string2)

    def test_nested_parents(self):
        string = ParentNode(
            "p",
            [
                ParentNode(
                    "b",
                    [
                        LeafNode("i", "Bold italics text")
                    ]
                )
            ]
        ).to_html()
        string2 = "<p><b><i>Bold italics text</i></b></p>"
        self.assertEqual(string, string2)

    def test_nested_parents2(self):
        string = ParentNode(
            "p",
            [
                ParentNode(
                    "b",
                    [
                        LeafNode(None, "Bold text"),
                        LeafNode("i", "Bold italics text")
                    ]
                ),
                LeafNode(None, "Normal text")
            ]
        ).to_html()
        string2 = "<p><b>Bold text<i>Bold italics text</i></b>Normal text</p>"
        self.assertEqual(string, string2)

    def test_nested_parents3(self):
        string = ParentNode(
            "p",
            [
                ParentNode(
                    "b",
                    [
                        ParentNode(
                            "a",
                            [
                                LeafNode("i", "Bolded italics link")
                            ],
                            {"href": "https://www.google.com"}
                        ),
                        LeafNode(None, "Bold text")
                    ]
                )
            ]
        ).to_html()
        string2 = '<p><b><a href="https://www.google.com"><i>Bolded italics link</i></a>Bold text</b></p>'
        self.assertEqual(string, string2)

    def test_nested_parents4(self):
        string = ParentNode(
            "p",
            [
                ParentNode(
                    "b",
                    [
                        ParentNode(
                            "a",
                            [
                                LeafNode("i", "This bold italics link")
                            ],
                            {"href": "https://www.google.com"}
                        ),
                        LeafNode(None, "or"),
                        ParentNode(
                            "a",
                            [
                                LeafNode("i", "This bold italics link")
                            ],
                            {"href": "https://www.microsoft.com"}
                        )
                    ]
                ),
            ]
        ).to_html()
        string2 = '<p><b><a href="https://www.google.com"><i>This bold italics link</i></a>or<a href="https://www.microsoft.com"><i>This bold italics link</i></a></b></p>'
        self.assertEqual(string, string2)


if __name__ == "__main__":
    unittest.main()
