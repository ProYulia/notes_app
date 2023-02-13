import json


def read_file(file):
    with open(file, 'r') as f:
        return json.load(f)


def write_to_file(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)


def create_new_file(data, file):
    with open(file, 'w') as f:
        json.dump([data, ], f, indent=4)


def get_last_id(file):
    try:
        content = read_file(file)
        return max(note['id'] for note in content)
    except FileNotFoundError:
        return 0

