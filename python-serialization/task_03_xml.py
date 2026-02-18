import xml.etree.ElementTree as ET
'''
test test 1, 2, 1, 2
'''


def serialize_to_xml(dictionary, filename):
    '''
    Docstring for serialize_to_xml

    :param dictionary: Description
    :param filename: Description
    '''
    data = ET.Element('data')
    name = ET.SubElement(data, "name")
    age = ET.SubElement(data, "age")
    city = ET.SubElement(data, "city")
    name.text = dictionary["name"]
    age.text = dictionary["age"]
    city.text = dictionary["city"]
    tree = ET.ElementTree(data)
    tree.write(filename)


def deserialize_from_xml(filename):
    '''
    Docstring for deserialize_from_xml

    :param filename: Description
    '''
    tree = ET.parse(filename)
    root = tree.getroot()
    dict_xml = {}
    for child in root:
        val = child.text
        if child.tag == "age":
            val = int(val)
        dict_xml.update({child.tag: val})
    return dict_xml
