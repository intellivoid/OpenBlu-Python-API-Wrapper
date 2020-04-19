"""This file contains the abstraction layers over the JSON response got from OpenBlu API"""


class ServerListing(object):
    """An abstraction layer over a dictionary object representing a server on the OpenBlu network.
       Server attributes can be accessed trough dot notation (e.g. ``foo.bar``) and trough slicing (``foo["bar"]``)

       :param data: The dictionary object converted from the JSON response from OpenBlu API
    """

    def __init__(self, data: dict):
        """Object constructor"""
        self._data = data

    def __getitem__(self, item):
        """Implements self['item']"""

        return self._data.__getitem__(item)

    def __getattr__(self, attr):
        """Implements self.attr"""

        return self.__getitem__(attr)

    def __repr__(self):
        """Implements repr(self)"""

        show = "\n"
        for index, (key, value) in enumerate(self._data.items()):
            show += f"{key}={value}"
            if index < len(self._data) - 1:
                show += ", \n"
        return f"ServerListing({show})"


class Server(ServerListing):
    def __init__(self, data):
        """Object constructor"""

        super().__init__(data)

    def __repr__(self):
        """Implement repr(self)"""

        return f"<Server object at {hex(id(self))}>"
