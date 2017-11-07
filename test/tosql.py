#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import request
import httplib, urllib
import sys

jsonfile = '/Users/tt/.jenkins/workspace/yq/src/version.json'
posturl = "https://eep-t.efivestar.com/api/version/create"

config_data = open(jsonfile)
config = json.load(config_data)
config_data.close()
version = config['version']

mydata = {
    "lastVersion": 'true',
    "versionNO": version,
    "versionAbout": "",
    "androidAddress": "https://dl.efivestar.com/eep/test/v1.1.0.3/EEP_v1.1.0.3.apk",
    "iosAddress": "itms-services://?action=download-manifest&url=https://dl.efivestar.com/eep/test/v1.1.0.3/manifest.plist",
    "forceUpate": 'true'
}

conn = httplib.HTTPConnection(posturl)
conn.request(method="POST", url=posturl, body=mydata, headers={"Content-Type": "application/json"})

response = conn.getresponse()
print(response.status)
conn.close()

