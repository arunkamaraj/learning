import xml.sax

class xml_handler(xml.sax.ContentHandler):
    def __init__(self):

        self.data = None

    def startElement(self, name, attrs):
        if name == "movie":
            print name, "::", attrs["title"]

    def endElement(self, name):
        print self.data

    def characters(self, content):
        self.data = content

# parser = xml.sax.make_parser() # creating parser

# parser.setFeature(xml.sax.handler.feature_namespaces, 0) # setting name space param

handler = xml_handler()

# parser.setContentHandler(handler)
# parser.parse("movies.xml")

xml.sax.parse("movies.xml", handler)

# xml.sax.parseString("movies.xml", handler)
