from lxml import etree

xml = open("input.xml", 'r')
json = open("output.json", 'w+')
json.write('{\n')
xml_str = xml.read()

xml_arr = [x for x in xml_str.split('\n') if x!= xml_str.split('\n')[0]]
xml_str = '\n'.join(xml_arr)
#discard the xml version heading

root = etree.XML(xml_str)
tree = etree.ElementTree(root)
#building an lxml tree for the given xml string

def dfs (node, depth):

    for i in range (depth):
        json.write("\t")
    if (node.text is not None and '\n' not in node.text):
        json.write('"{}" : "{}",\n'.format(node.tag, node.text))
    elif (node.items() != []):
        json.write('"'+node.tag+'" : {\n')
        for key, value in node.items():
            for i in range (depth+1):
                json.write("\t")
            json.write('"{}" : "{}",\n'.format(key, value))

        #recursion
        for child in node:
            dfs(child, depth+1)

        for i in range (depth):
            json.write("\t")
        json.write('},\n')
    else :
        json.write('"'+node.tag+'" : {\n')

        #recursion
        for child in node:
            dfs(child, depth+1)

        for i in range (depth):
            json.write("\t")
        json.write('},\n')

for child in root:
    dfs(child, 1)

parser = JsonComment(JSON)
data = parser.load(json)

json.write('}')
json.close()
xml.close()