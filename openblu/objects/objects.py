"""This file contains the abstraction layers over the JSON response got from OpenBlu API"""


class Server(object):
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



class ServerListing(Server):
    """An abstraction layer over a dictionary object representing a server on the OpenBlu network.
       Server attributes can be accessed trough dot notation (e.g. ``foo.bar``) and trough slicing (``foo["bar"]``)
       This object is iterable and yields one server at a time when used in a for loop

       :param data: The dictionary object converted from the JSON response from OpenBlu API
    """

    def __init__(self, data):
        """Object constructor"""

        self._data = data
        servers = []
        for server in self._data["servers"]:
            servers.append(Server(server))
        self._data["servers"] = servers

    def __iter__(self):
        """Implements iter(self)"""

        for server in self._data["servers"]:
            yield server


