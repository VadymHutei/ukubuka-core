from flask import render_template


class View:

    def __init__(self, template=None):
        self.template = template
        self.data = {}
        self.templateData = {}

    def addData(self, data):
        self.data.update(data)

    def prepageData(self):
        self.prepareTemplateData()
        self.preparePageData()
        self.data['t'] = self.templateData

    def prepareTemplateData(self):
        pass

    def preparePageData(self):
        pass

    def render(self):
        self.prepageData()
        return render_template(self.template, **self.data)