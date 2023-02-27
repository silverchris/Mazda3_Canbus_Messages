import xml.etree.ElementTree as ET


def sortchildrenby(parent, attr):
    parent[:] = sorted(parent, key=lambda child: child.get(attr))


ET.register_namespace("", "http://kayak.2codeornot2code.org/1.0")
parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))

with open("skyactive_new.kcd", "r") as infile:
    tree = ET.parse(infile, parser)
    root = tree.getroot()
    for bus in root.findall("{http://kayak.2codeornot2code.org/1.0}Bus"):
        print(bus.tag, bus.attrib)
        sortchildrenby(bus, "id")
        for child in bus:
            print(child.tag, child.attrib)
tree.write("skyactive_new.kcd")
