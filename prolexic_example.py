#! /usr/bin/env python

""" Copyright 2015 Akamai Technologies, Inc. All Rights Reserved.
 
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.

 You may obtain a copy of the License at 

    http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.


"""

import requests, logging, json, random, sys, re
from akamai.edgegrid import EdgeGridAuth
from config import EdgeGridConfig
from urllib import parse
from subprocess import call
import os
session = requests.Session()
debug = False
verbose = False
section_name = "prolexic"
contract = "bankworldcorp"
headers = {'content-type':'application/json'}

# If all parameters are set already, use them.  Otherwise
# use the config
config = EdgeGridConfig({"verbose":False},section_name)

if hasattr(config, "debug") and config.debug:
	debug = True

if hasattr(config, "verbose") and config.verbose:
	verbose = True

# Set the config options
session.auth = EdgeGridAuth(
            client_token=config.client_token,
            client_secret=config.client_secret,
            access_token=config.access_token
)

baseurl = '%s://%s/' % ('https', config.host)
# To find the metric types, call /prolexic-analytics/v2/metric-types/{contract}

postbody = {
    "contract": "bankworldcorp",
    "start": 1562008743,
    "end": 1564600743,
    "samples": 100,
    "type": {
        "mitigationPost": [
            "bandwidth",
	    "packets"
        ],
        "mitigationPre": [
            "bandwidth",
   	    "packets"
        ]
    }
}


user_post_result = session.post(baseurl + '/prolexic-analytics/v2/metrics', json.dumps(postbody), headers=headers)
printoutput = json.loads(user_post_result.text)
print (json.dumps(printoutput, indent=4))

# Now, list of attacks
# prolexic-analytics/v2/attack-reports/contract/coral/start/1397049511/end/1399641518

attacksurl = baseurl + "/prolexic-analytics/v3/attack-reports/contract/bankworldcort/start/1562008743/end/1564600743"

user_get_result = session.get(attacksurl)
printoutput = json.loads(user_get_result.text)
print (json.dumps(printoutput, indent=4))
