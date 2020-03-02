from flask import render_template


class View():

    _template = None
    _layout = None
    _params = {}

    def _setTemplate(self, template_path):
        self._template = template_path
    
    def _setParam(self, name, value):
        self._params[name] = value

    def _render(self):
        return render_template(self._template, **self._params)

    def setLayout(self, layout_path):
        self._setParam('layout', layout_path)

    def setParam(self, name, value):
        self._setParam(name, value)

    def render(self):
        return self._render()
