from flask import render_template


class View:

    def __init__(self, template=None, language=None):
        self.data = {
            't': {}
        }
        self.template = template

    def addData(self, data):
        self.data.update(data)

    def render(self):
        self.prepageData()
        return render_template(self.template, **self.data)

    def prepageData(self):
        self.prepareTemplateData()
        self.preparePageData()

    def prepareTemplateData(self):
        pass

    def preparePageData(self):
        pass