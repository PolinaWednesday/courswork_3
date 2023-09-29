
import json

def operation(filename):
    if not os.path.exists(path):
        return []
    with open('operations.json', 'r', encoding='utf-8') as file:
        text = json.load(file)
        return text