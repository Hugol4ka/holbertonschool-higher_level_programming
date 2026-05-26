#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    """functionality to serialize a Python dictionary to a JSON file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """deserialize the JSON file to recreate the Python Dictionary"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
