import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

def LoadDataFromJsonFile(filename, *keyname):
    f = open(filename, 'r', encoding='utf-8')
    data = json.load(f)
    if 0 != len(keyname):
       for keyname_array in keyname:
           data = data[keyname_array]
    f.close()
    return data

def WriteDataToJsonFile(data, filename):
    f = open(filename, 'w', encoding='utf-8')
    if isinstance(data, dict):
       json.dump(data, f)
       print("write json file successfully")
       f.close()
       return 0
    else:
       print("write json file failed")
       f.close()
       return -1

def LoadDataFromJsonDict(json_dict):
    data = json.loads(json_dict)
    return data

def WriteDataToJsonDict(data, *print_flag):
    json_dict = json.dumps(data, indent = 4, sort_keys= True)
    if 1 == len(print_flag):
        if 1 == print_flag:
           print(json_dict)
    return json_dict

def TravelXml(element):
    if len(element)>0:
        for child in element:
            print (child.tag, "----", child.attrib)
            TravelXml(child)
    #else:
        #print (element.tag, "----", element.attrib)
    return

def LoadDataFromXmlFile(filename, *keyname):
    f = open(filename, 'r', encoding='utf-8')
    tree = ET.parse(f)
    root = tree.getroot()
    travelXml(root)
    f.close()
    return root

def SetXmlRoot(root_str):
    root = ET.Element(root_str)
    return root

def InsertXmlChild(root, tag, text):
    ele = ET.SubElement(root, tag)
    ele.text = text
    ele.tail = '\n'
    return ele

def WriteDataToXmlFile(filename, root):
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration = True)
    return 

def WriteDataToXmlFile_1(filename, root, indent="\t", newl="\n", encoding="utf-8"):
    rawText = ET.tostring(root)
    dom = minidom.parseString(rawText)
    with open(filename, 'w') as f:
        dom.writexml(f, "", indent, newl, encoding)



'''
def WriteDataToXmlFile(data, filename):
    f = open(filename, 'w', encoding='utf-8')
    if isinstance(data, dict):
       json.dump(data, f)
       print("write json file successfully")
       f.close()
       return 0
    else:
       print("write json file failed")
       f.close()
       return -1
'''