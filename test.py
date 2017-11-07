#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import sys

jsonfile = '/Users/tt/.jenkins/workspace/yq/src/version.json'
posturl = "https://eep-t.efivestar.com/api/version/create"

config_data = open(jsonfile)
config = json.load(config_data)
config_data.close()
version = config['version']

mydata = {
    "lastVersion": sys.argv[3],
    "versionNO": version,
    "versionAbout": sys.argv[1],
    "androidAddress": "https://dl.efivestar.com/eep/%s/%s/EEP_%s.apk" % (sys.argv[2], version, version),
    "iosAddress": "itms-services://?action=download-manifest&url=https://dl.efivestar.com/eep/%s/%s/manifest.plist" % (
    sys.argv[2], version),
    "forceUpate": sys.argv[4]
}

r = requests.post(url=posturl, data=json.dumps(mydata), headers={"Content-Type": "application/json"})
print(r.content)
