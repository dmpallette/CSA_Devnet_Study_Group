#!/usr/bin/env python3

import requests

chuck = requests.get("https://api.chucknorris.io/jokes/random")

joke = chuck.json()

print(joke['value'])

