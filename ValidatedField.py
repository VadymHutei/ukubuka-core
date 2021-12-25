class ValidatedField:

    def __init__(self, name, required):
        self._name = name
        self._value = None
        self._required = required
        self._rules = []
        self._hasErrors = False
        self._errors = []

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @property
    def hasErrors(self):
        return self._hasErrors

    def _addError(self, message):
        if not self._hasErrors:
            self._hasErrors = True
        self._errors.append(message)

    def addRule(self, rule, message):
        self._rules.append({
            'callback': rule,
            'message': message,
        })

    def validate(self):
        if self._value is None:
            if self._required:
                self._addError(f'{self._name} is required')
        else:
            for rule in self._rules:
                if not rule['callback'](self._value):
                    self._addError(rule['message'])

    def getErrors(self):
        return {self._name: self._errors}

    def setValue(self, value):
        self._value = value