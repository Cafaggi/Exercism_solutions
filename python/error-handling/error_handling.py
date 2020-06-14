def handle_error_by_throwing_exception():
    raise Exception("This is an error")


def handle_error_by_returning_none(input_data):
    if input_data.isnumeric():
        return int(input_data)
    else:
        return None


def handle_error_by_returning_tuple(input_data):
    tested_input_data = handle_error_by_returning_none(input_data)
    return (tested_input_data != None, tested_input_data)


def filelike_objects_are_closed_on_exception(filelike_object):
    with filelike_object as file:
        filelike_object.do_something()

