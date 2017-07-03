import re

pat = re.compile(r'[A-Za-z0-9.\-]+@[A-Za-z0-9.\-]+', re.IGNORECASE)
addresses = set()

with open('/Users/tt/Downloads/test') as content:
    for line in content:
        for address in pat.findall(line):
            addresses.add(address)
for address in sorted(addresses):
    print(address)
