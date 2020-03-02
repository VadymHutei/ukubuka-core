class Menu():

    _items = []

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)

    def _createStructure(self, data):
        result = []
        checked = []
        data_d = {}
        dependencies = {}
        for item in data:
            parent = item['parent']
            id_ = item['id']
            data_d[id_] = item
            if parent not in dependencies:
                dependencies[parent] = []
            dependencies[parent].append(id_)
        movement_counter = 1
        while movement_counter > 0:
            movement_counter = 0
            for id_ in data_d:
                item = data_d[id_]
                parent = item['parent']
                if id_ in checked:
                    continue
                if id_ in dependencies:
                    continue
                if parent in data_d:
                    if 'subitems' not in data_d[parent]:
                        data_d[parent]['subitems'] = []
                    data_d[parent]['subitems'].append(item)
                    dependencies[parent].remove(id_)
                    if not dependencies[parent]:
                        del dependencies[parent]
                else:
                    result.append(item)
                checked.append(id_)
                movement_counter += 1
        return result

    def getItems(self):
        return self._items
