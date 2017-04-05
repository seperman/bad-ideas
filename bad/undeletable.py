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
        frame, filename, line_number, function_name, lines, index = inspect.stack()[1]
        obj_name = lines[-1].strip().lstrip('del').strip()
        set_in_frame(frame, obj_name, self)
        print("You can't delete me!")

    def __str__(self):
        return "<undeletable:{}>".format(id(self))
