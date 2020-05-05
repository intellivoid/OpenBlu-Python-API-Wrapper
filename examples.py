# OpenBlu API usage examples


# The filter_by parameter

# This parameter is used to filter VPN servers by the country they are located
# in. It has to be a tuple containing the desired country name and its form. For instance,
# if the desired country name is 'Japan', the second parameter must be 'country', because that is the full name of the country.
# Another option would be 'JP', the shorter form, in which case the second parameter must be 'country_short'
# Below some examples


from openblu import OpenBluAPI


api = OpenBluAPI("key here")

servers = api.list_servers(filter_by=("Japan", "country"))
# The above line is equivalent to the one below
servers = api.list_servers(filter_by=("JP", "country_short"))


# The sort_by parameter

# This parameter is used to sort server entries by one of their attributes.
# The resulting list will be ordered (sorted) according to that parameter
# Options for this parameter are: 'ping', 'last_updated', 'total_sessions', 'created', 'sessions' and 'score'


from openblu import OpenBluAPI


api = OpenBluAPI("key here")

servers = api.list_servers(sort_by="last_updated")
# This will fetch the server with the highest 'last_updated' value


# The order_by parameter simply determines the sorting order of the servers list

from openblu import OpenBluAPI


api = OpenBluAPI("key here")

servers = api.list_servers(sort_by="ping", order_by="ascending")
# This will sort the servers by their ping, from lowest to highest

servers = api.list_servers(sort_by="score", order_by="descending")
# This will sort the servers by their score, from highest to lowest


