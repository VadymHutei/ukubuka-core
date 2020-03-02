from core import validator


class Entity():

    _validate_methods = {}
    _fields = set()

    def __init__(self, data):
        self._data = {field: None for field in self._fields}
        self._fillFields(data)

    def __getattr__(self, name):
        return self._data.get(name, None)

    @classmethod
    def createCollection(cls, data):
        entityCollection = []
        for el in data:
            entity = cls(el)
            entityCollection.append(entity)
        return entityCollection

    def _setField(self, field, value):
        if field not in self._fields: return False
        if not self._validate_methods[field](value): return False
        self._data[field] = value

    def _fillFields(self, data):
        for field in data:
            value = data[field]
            self._setField(field, value)

    def setField(self, field, value):
        self._data[field] = value

    def getFields(self):
        return self._data
