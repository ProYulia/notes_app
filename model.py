import datetime
import os
from json_manager import *

date_format = '%d.%m.%Y'
file = 'data.json'


def add_note(note):
    current_id = int(get_last_id(file))
    current_id += 1
    new_note = dict(id=str(current_id), header=note[0], body=note[1],
                    modified=datetime.datetime.now().strftime(date_format))

    if os.path.isfile(file):
        content = read_file(file)
        content.append(new_note)
        write_to_file(content, file)
    else:
        create_new_file(new_note, file)


def edit_note(element_id, note):
    content = read_file(file)
    for element in content:
        if element['id'] == element_id:
            element['header'] = note[0]
            element['body'] = note[1]
            element['modified'] = datetime.datetime.now().strftime(date_format)
            break
    write_to_file(content, file)


def check_note(required_id):
    content = read_file(file)
    for element in content:
        if element['id'] == required_id:
            return required_id
    return False


def get_note(required_id):
    content = read_file(file)
    for element in content:
        if element['id'] == required_id:
            return element
    return False


def get_by_date(required_date):
    content = read_file(file)
    result = []
    for element in content:
        if element['modified'] == required_date:
            result.append(element)
    return result


def delete_note(required_id):
    content = read_file(file)
    index = -1
    for element in content:
        if element['id'] == required_id:
            index = content.index(element)
            break
    if index != -1:
        content.pop(index)
        write_to_file(content, file)





