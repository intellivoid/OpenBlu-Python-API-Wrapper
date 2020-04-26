# OpenBlu-Python-Wrapper

Official Python wrapper around OpenBlu API


# Overview

This wrapper can be used to fetch servers from the OpenBlu API and retrieve their OpenVPN configuration.

To make things easy, the library abstracts the JSON responses from the API inside two objects:

- `Server` -> Contains the OpenVPN configuration as described in [OpenBlu's Documentation](https://docs.intellivoid.info/openblu/v1/get_server)
- `ServerListing` -> Contains extra info from a server such as ping, IP address and location

The `ServerListing` object can be printed to get an overview of the server's metadata.


## Installation

To install this wrapper, simply clone this repo with `git clone`, then run `python3 setup.py install`


## Usage

### Fetch multiple servers

To fetch multiple servers, without their OpenVPN configuration, you can use the `list_servers()` of the `openblu.OpenBluAPI` class like shown below

```python

from openblu import OpenBluAPI

api = OpenBluAPI('access_key')  # Get your access key at openblu.intellivoid.net

servers = servers.list_servers(filter_by=("germany", "country"))
```

Below the full documentation for the `list_servers` method in Sphinx format

```
Fetches OpenVPN servers from the OpenBlu API

:param filter_by: If not ``None``, filter the results by the given parameter. It must be a tuple containing a country name and either one of these strings (In this order): "country", "country_short". If "country_short" is the second element of the tuple, the country name must be the short form of its name (e.g. 'de' for germany or 'jp' for Japan) otherwise, the full extended form is required. Defaults to ``None``
:type filter_by: tuple, None, optional
:param order_by: If not ``None``, order the results by this order. It can either be ``'ascending'`` or ``'descending'``, defaults to ``None``.
:type order_by: str, None, optional
:param sort_by: Sorts the list by the given condition, defaults to ``None`` (no sorting). Possible choices are "score", "ping", "sessions", "total_sessions", "last_updated" and "created"
:type sort_by: str, None, optional
:param verbose: If ``True``, make the output verbose, default to ``False``
:type verbose: bool, optional
:returns servers_list: A list of class:ServerListing objects
:rtype servers_list: list
:raises OpenBluError: An proper subclass of OpenBluError is raised if something goes wrong. If the error cannot be determined, a generic OpenBluError is raised
```


### Get a single server (OpenVPN config)

As described in OpenBlu's documentation, servers can be identified by a unique ID. That ID can be used to fetch the OpenVPN server configuration from the OpenBlu API as shown below


```python

from openblu import OpenBluAPI

api = OpenBluAPI('access_key')  # Get your access key at openblu.intellivoid.net

servers = servers.list_servers(filter_by=("germany", "country"))

server = servers[0]    # Take the first entry

ovpn = api.get_server(server.id)   # Retrieve the server's configuration
```

Below the full documentation for the `get_server` method in Sphinx format

```

Fetches a single OpenVPN server from the OpenBlu API, given its unique ID

:param uuid: The unique ID of the desired server
:type uuid: string
:param verbose: If ``True``, make output verbose, default to ``False``
:type verbose: bool, optional
:returns: A class:Server object
:rtype: class: Server
:raises OpenBluError: An proper subclass of OpenBluError is raised if something goes wrong. If the error cannot be determined, a generic OpenBluError is raised
```

### Exceptions

The wrapper implements 3 exceptions:
- `OpenBluError` -> Generic parent class for all exceptions, also raised when an error other than 401 and 404 is returned by the API
- `ServerNotFound` -> When an invalid server ID is provided to the API
- `Unauthorized Access` -> When an invalid access key is provided to the API

Other errors, such as JSON decoding errors or HTTP failures, are not catched and must be handled by the wrapper itself.

### Last, but not least

`Server` and `ServerListing` objects support dict-like accessing and dot notation accessing for their attributes.

Doing `server["id"]` or `server.id` yields the same result.


