import xml.etree.ElementTree as ET

with open("sample.xml", 'rt') as f:
    tree = ET.parse(f)


for node in tree.iter("outline"):
    name = node.attrib.get("text")
    url = node.attrib.get("xmlUrl")
    if name and url:
        print "  ", name, "::", url
    else:
        print name

        
    # if url:
    #     print url