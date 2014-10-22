"""
Configuration for BubbleHub analyzer
"""
import json
import os

JSON_CONFIG = "config.json"

project_root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
json_config_file = os.path.join(project_root_dir, JSON_CONFIG)

with open(json_config_file) as f:
    json_contents = f.readlines()

config = json.loads("".join(json_contents))
