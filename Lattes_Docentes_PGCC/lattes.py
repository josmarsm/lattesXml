import xml.etree.ElementTree as ET
tree = ET.parse('0865997296771785.xml')
root = tree.getroot()
#for child in root:
#   print(child.tag, child.attrib)

#for projeto_pesquisa in root.iter('PROJETO-DE-PESQUISA'):
#    print(projeto_pesquisa.tag, projeto_pesquisa.attrib)

for projeto_pesquisa in root.findall('PROJETO-DE-PESQUISA'):
    equipe = projeto_pesquisa.find('EQUIPE-DO-PROJETO').text
    name = projeto_pesquisa.get('name')
    print(name, equipe)