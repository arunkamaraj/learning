import xml.etree.cElementTree as ET


def without_file_handler():
    # file key word arg is very important or else it won't work
    # tree_without_file = ET.ElementTree(file="doc.xml")
    tree_without_file = ET.ElementTree(file="movies.xml")

    # for node in tree_without_file.iter("branch"):
    for node in tree_without_file.iter():
        print node.tag, node.attrib


def with_file():
    with open("doc.xml", "rt") as f:
        tree = ET.parse(f)

    for node in tree.iter("branch"):
        print node

without_file_handler()