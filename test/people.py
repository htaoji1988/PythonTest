people = {
    'jihaitao': {
        'phone': '13770866821',
        'address': 'nanjing,jiangning',

    },
    'yuanchen': {
        'phone': '6666666666',
        'address': 'taizhou,jiangyan',
    },
    'juheng': {
        'phone': '77777777777',
        'address': 'nanjing,pukou',
    },
}

labels = {
    'phone': 'phone number',
    'address': 'address',
}

name = raw_input('name:')

request = raw_input('phone number (p) or address (a)?')

key = request
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'address'

person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

print "%s's %s is %s." % (name, label, result)
