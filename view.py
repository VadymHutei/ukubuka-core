from flask import render_template


class View:

    def __init__(self, template=None):
        self._template = template
        self._data = {}
        self._templateData = {}

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, template):
        self._template = template

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data.update(data)

    @property
    def templateData(self):
        return self._templateData

    @templateData.setter
    def templateData(self, data):
        self._templateData.update(data)

    def _prepageData(self):
        self._prepareTemplateData()
        self._preparePageData()
        self._data['t'] = self._templateData

    def _prepareTemplateData(self):
        pass

    def _preparePageData(self):
        pass

    def render(self):
        self._prepageData()
        return render_template(self._template, **self._data)