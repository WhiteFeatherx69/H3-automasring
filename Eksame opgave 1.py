
from email.quoprimime import body_check, header_check
from idlelib.multicall import r

import requests

response = requests.get(
'http://20.91.198.208', headers={'Authorization': 'access_token df2e6ced'})

var = r.status_code
var = response.status_code
var = body_check()
var = header_check()