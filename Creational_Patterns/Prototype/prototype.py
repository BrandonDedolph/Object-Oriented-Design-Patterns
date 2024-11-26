from copy import deepcopy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        """Register an object."""
        self._objects[name] = obj

    def unregister(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attrs):
        """Clone a registered object and update attributes."""
        obj = deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj
