#!/usr/bin/env python

#  SPDX-License-Identifier: AGPL-3.0-only
#  Copyright (C) 2020-2021  Patrick McLean - psmware ltd

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.

import json
import os
import requests
from base64 import b64encode

my_user = os.environ.get("GH_USER")
my_tokn = os.environ.get("GH_TOKN")

my_url = "https://api.github.com/repos/b-skwad/duckview/labels"
encoded_credentials = b64encode(bytes(f'{my_user}:{my_tokn}',
                                encoding='ascii')).decode('ascii')
# Let's load up our labels definition and prepare our repository.
with open('labels.json') as json_file:
    labels = json.load(json_file)

    for label in labels:
        print(label)

        my_headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': f'Basic {encoded_credentials}'}
        print(my_headers)
        my_data = json.dumps(label).encode('utf-8')
        response = requests.post(my_url, headers=my_headers, data = my_data)
