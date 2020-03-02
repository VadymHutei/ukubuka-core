import requests

import config
from errors import ContentServiceError, NotFoundError


class ContentService():

    def __init__(self):
        self._url = config.CONTENT_SERVICE['url']
        self._timeout = (
            config.CONNECT_TIMEOUT,
            config.READ_TIMEOUT
        )
        self._headers = {
            'Accept': 'application/json',
            'language': config.CURRENT_LANGUAGE
        }

    def _setEntity(self, entity):
        self._entity = entity

    def _setParams(self, params):
        self._params = params

    def _get(self):
        return requests.get(
            self._url + self._entity,
            timeout = self._timeout,
            headers = self._headers,
            params = self._params
        )

    def _makeRequest(self, method):
        method = '_' + method
        if not hasattr(self, method):
            raise ContentServiceError(f'Method {method} is not implemented')
        reqMeth = getattr(self, method)
        try:
            response = reqMeth()
        except requests.exceptions.ReadTimeout:
            raise ContentServiceError('Read timeout occured')
        except requests.exceptions.ConnectTimeout:
            raise ContentServiceError('Connection timeout occured')
        except requests.exceptions.RequestException:
            raise ContentServiceError('RequestException')
        except Exception:
            raise ContentServiceError()
        if response.status_code == 200:
            return response.json()
        if response.status_code == 404:
            raise NotFoundError
        else:
            raise ContentServiceError

    def get(self, entity, **params):
        self._setEntity(entity)
        self._setParams(params)
        return self._makeRequest('get')
