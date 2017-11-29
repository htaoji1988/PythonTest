import json
import time
import os

VersionFile = "/tmp/version.json"
time = time.strftime("%Y%m%d%H%M%S", time.localtime())


def newversion():
    with open(VersionFile) as version:
        content = json.load(version)
        content['version'] = content['version'] + "." + time
        return content


with open("%s.bak" % VersionFile, "w") as version:
    json.dump(newversion(), version)

os.remove(VersionFile)
os.rename("%s.bak" % VersionFile, VersionFile)
