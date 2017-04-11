import ctypes
import inspect

locals_to_fast = ctypes.pythonapi.PyFrame_LocalsToFast
locals_to_fast.restype = None
locals_to_fast.argtypes = [ctypes.py_object, ctypes.c_int]


def set_in_frame(frame, name, value):
    frame.f_locals[name] = value
    locals_to_fast(frame, 1)


class Undeletable:
    def __del__(self):
        # Modified from http://stackoverflow.com/a/8178726/1497443
        inspected_stack = inspect.stack()
        frame, filename, line_number, function_name, lines, index = inspected_stack[1]

        # If we don't see lines in stack, maybe it is an interactive shell
        # Trying to get the object name via readline history then
        if not lines:
            import readline
            lastline_index = readline.get_current_history_length()
            lines = [readline.get_history_item(lastline_index)]

        obj_name = lines[-1].strip().lstrip('del').strip()
        set_in_frame(frame, obj_name, self)
        print("You can't delete me!")

    def __str__(self):
        return "<undeletable:{}>".format(id(self))

    __repr__ = __str__
