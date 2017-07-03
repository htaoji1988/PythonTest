import fileinput
import re

pat = re.compile('From:(.*)<.*?>$')
for line in fileinput.input('/Users/tt/Downloads/test'):
    m = pat.match(line)
    if m:
        print(m.group(1))
