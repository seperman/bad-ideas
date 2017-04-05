from .filtered import filtered


class grep:

    def __init__(self, item):
        self.item = item.lower()

    def is_item_in_line(self, line):
        return self.item in line

    def __ror__(self, other):
        if isinstance(other, str):
            other = other.lower().split('\n')
        return filtered(self.is_item_in_line, other)
