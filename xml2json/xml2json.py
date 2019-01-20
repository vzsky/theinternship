from lxml import etree
from json import dumps as jsonify

xml = open("input.xml", 'r')
json = open("output.json", 'w+')
xml_str = xml.read()

xml_arr = [x for x in xml_str.split('\n') if x!= xml_str.split('\n')[0]]
xml_str = '\n'.join(xml_arr)
#discard the xml version heading

root = etree.XML(xml_str)
tree = etree.ElementTree(root)
#building an lxml tree for the given xml string

def dfs (node):

    json_dict = {}
    sub_dict = {}

    if (node.text is not None and '\n' not in node.text):
        json_dict[node.tag] = node.text
    elif (node.items() != []):
        for key, val in node.items():
            sub_dict[key] = val
        json_dict[node.tag] = sub_dict
        #recursion
        for child in node:
            sub_dict = dfs(child)
            for key in sub_dict:
                json_dict[node.tag][key] = sub_dict[key]
    else :
        json_dict[node.tag] = {}
        #recursion
        for child in node:
            sub_dict = dfs(child)
            for key in sub_dict:
                json_dict[node.tag][key] = sub_dict[key]
    return json_dict

json_dict = dfs(root)
for key in json_dict:
    json.write(jsonify(json_dict[key],indent=4))
    break

json.close()
xml.close()