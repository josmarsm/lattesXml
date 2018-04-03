import xml.etree.ElementTree as ET

tree = ET.parse('0538173746410766.xml')
root = tree.getroot()
for child in root:
    print (child.tag, child.attrib)
root[0][1].text