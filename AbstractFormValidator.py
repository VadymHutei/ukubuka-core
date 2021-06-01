from abc import ABC, abstractmethod


class AbstractFormValidator(ABC):

    def __init__(self):
        self.fields = self.setRules()
        self.hasErrors = False
        self.errors = {}

    @abstractmethod
    def setRules(self):
        pass

    def addErrors(self, errors):
        if not self.hasErrors:
            self.hasErrors = True
        self.errors.update(errors)