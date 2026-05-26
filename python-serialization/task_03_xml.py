#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for cle, valeur in dictionary.items():
        child = ET.SubElement(root, cle)
        child.text = str(valeur)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    my_dict = {}

    for child in root:
        my_dict[child.tag] = child.text
    return my_dict
