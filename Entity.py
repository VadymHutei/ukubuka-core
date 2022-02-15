class Entity:
        
    properties = {}
    booleanProperties = {}

    def __init__(self, data):
        for propertyName, fieldName in self.__class__.properties.items():
            setattr(self, self.__class__._getAttributeName(propertyName), data[fieldName])
        for propertyName, fieldName in self.__class__.booleanProperties.items():
            setattr(self, self.__class__._getAttributeName(propertyName), bool(data[fieldName]))

    def __getattr__(self, propertyName):
        return getattr(self, self.__class__._getAttributeName(propertyName))

    @staticmethod
    def _getAttributeName(attributeName):
        return '_' + attributeName