from abc import ABC, abstractmethod


class AbstractFormValidator(ABC):

    def __init__(self, form):
        self.fields = self.setRules()
        self.hasErrors = False
        self.errors = {}

        for field in self.fields:
            field.setValue(form[field.name])
            field.validate()
            if field.hasErrors:
                self.addErrors(field.getErrors())

    @abstractmethod
    def setRules(self):
        pass

    def addErrors(self, errors):
        if not self.hasErrors:
            self.hasErrors = True
        self.errors.update(errors)

    def getFormData(self):
        return {field.name: field.value for field in self.fields}