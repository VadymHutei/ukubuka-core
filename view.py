from flask import render_template


class View:

    def __init__(self, template=None, language=None):
        self.data = {
            'template': {
                'language': language
            }
        }
        self.template = template

    def addData(self, data):
        self.data.update(data)

    def render(self):
        self._prepageData()
        return render_template(self.template, **self.data)

    def _prepageData(self):
        self._preparePageData()
        self._prepareTemplateData()

    def _prepareTemplateData(self):
        self.data.update(self.data['template'])

    def _preparePageData(self):
        pass