import xml.etree.ElementTree as et

from xml.etree.ElementTree import XML


def find_example():
    with open("sample.xml", "rt") as sf:
        tree = et.parse(sf)

    for node in tree.find(".//outline"):  # need to use double slash
        for name, value in node.attrib.items():
            # print name, "::",  value
            if name == "xmlUrl":
                print name, ":", value


def findall_example():
    with open("sample.xml", "rt") as sf:
        tree = et.parse(sf)

    for node in tree.findall(".//outline"):
        for name, value in node.attrib.items():
            # print name, "::",  value
            if name == "xmlUrl":
                print name, ":", value


def iterfind_example():
    with open("sample.xml", "rt") as sf:
        tree = et.parse(sf)

    for node in tree.iterfind(".//outline"):
        for name, value in node.attrib.items():
            # print name, "::",  value
            if name == "xmlUrl":
                print name, ":", value


def use_iterparse():
    for event, node in et.iterparse("sample.xml", ['start', 'end', 'start-ns', 'end-ns']):
        # for event, node in et.iterparse("sample.xml"):# its default event is "end"
        print event, node.tag


#important
def xml_demo():
    parsed = XML('''<root>
          <group>
            <child id="a">This is child "a".</child>
            <child id="b">This is child "b".</child>
          </group>
          <group>
            <child id="c">This is child "c".</child>
          </group>
        </root>
        ''')

    for node in parsed:  # it give only parent groups
        print node
        for i in node:
            for name, value in i.attrib.items():
                print name, "::", value


# use_iterparse()
# xml_demo()

print "-----------------------find----------------------"
find_example()

print "-----------------------find----------------------"
findall_example()

print "-----------------------find----------------------"
iterfind_example()
