from abc import ABC, abstractmethod


class AbstractFormValidator(ABC):

    def __init__(self, form):
        self.fields = self.setRules()
        self.hasErrors = False
        self.errors = {}

        for field in self.fields:
            field.validate(form[field.name])
            if field.hasErrors:
                self.addErrors(field.getErrors())

    @abstractmethod
    def setRules(self):
        pass

    def addErrors(self, errors):
        if not self.hasErrors:
            self.hasErrors = True
        self.errors.update(errors)