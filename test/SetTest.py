a = set("")
a.add("bb")
for i in range(10):
    a.add("dd " + str(i))

a.add("dd 8")

for i in a:
    print("It's %s" % i)
