class ValidatedField:

    def __init__(self, name, required):
        self.name = name
        self.required = required
        self.rules = []
        self.hasErrors = False
        self.errors = []

    def addRule(self, rule, message):
        self.rules.append({
            'callback': rule,
            'message': message
        })

    def validate(self, value):
        if value is None:
            if self.required:
                self._addError(f'{self.name} is required')
        else:
            for rule in self.rules:
                if not rule['callback'](value):
                    self._addError(message)

    def getErrors(self):
        return {self.name: self.errors}

    def _addError(message):
        if not self.hasErrors:
            self.hasErrors = True
        self.errors.append(message)