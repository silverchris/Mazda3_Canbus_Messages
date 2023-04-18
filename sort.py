import xml.etree.ElementTree as ET


def sortchildrenby(parent, attr):
    try:
        parent[:] = sorted(parent, key=lambda child: child.get(attr))
    except TypeError as e:
        raise(e)

def sort(filename):
    ET.register_namespace("", "http://kayak.2codeornot2code.org/1.0")
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))

    with open(filename, "r") as infile:
        tree = ET.parse(infile, parser)
        root = tree.getroot()
        for bus in root.findall("{http://kayak.2codeornot2code.org/1.0}Bus"):
            print(bus.tag, bus.attrib)
            sortchildrenby(bus, "id")
            for child in bus:
                if not child.attrib['name']:
                    child.attrib['name'] = f"Unknown_{child.attrib['id']}"
                # print(child.tag, child.attrib)
    tree.write(filename)

sort("skyactive_new.kcd")
sort("Vehicle_Settings.kcd")