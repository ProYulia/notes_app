from view import *
from model import *


def run_app():
    while True:
        match show_menu():
            case '1':
                add_note(new_note_ui())
                confirm_result()
            case '2':
                required_id = check_note(ask_for_id())
                if required_id is not False:
                    edit_note(required_id, new_note_ui())
                    confirm_result()
                else:
                    error_message()
            case '3':
                required_id = check_note(ask_for_id())
                if required_id is not False:
                    show_note(get_note(required_id))
                else:
                    error_message()
            case '4':
                lst = get_by_date(ask_for_date())
                for el in lst:
                    show_note(el)
            case '5':
                content = read_file(file)
                for el in content:
                    show_note(el)
            case '6':
                required_id = check_note(ask_for_id())
                if required_id is not False:
                    delete_note(required_id)
                    confirm_result()
            case '7':
                break
            case _:
                error_message()
