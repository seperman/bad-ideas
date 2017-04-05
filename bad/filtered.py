class filtered(filter):

    @property
    def listed(self):
        self._listed = getattr(self, "_listed", list(self))
        return self._listed

    def __str__(self):
        return str(self.listed)

    __repr__ = __str__

    def __eq__(self, other):
        return self.listed == other
