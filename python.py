name = "Yogesh Kumar"
PSNumber = 40003577
weight = 60.25
average = 49.06
matches = 45
# approach1
print(name, PSNumber, weight)
# approach2 using curl braces
print("Name is: {}, PSNumber is: {}, Weight is; {}".format(name, PSNumber, weight))
# approach3 using % operator
print("Name is: %s, PSNumber is: %d, Weight is: %g." %
      (name, PSNumber, weight))
print("==================")
x = {"Name": "Yogesh.L", "organisation": "LTTS", "DOJ": "12"}
# approach4
y = "My name is {} and I joined this {} organisation on {}th of December.".format(
    x["Name"], x["organisation"], x["DOJ"])
print(y)
print("==================")
z = ["Yogesh Kumar", "'LTTS'", 25]
p = "My name is {0[0]} and I joined this {0[1]} organisation on {0[2]}th of December.".format(
    z)
print(p)
print("==================")
q = "%s is averaging %g as he played just %d matches in his entire career " % (
    name, average, matches)
print(q)
print("==================")
for i in range(1, 12):
    output = "The value is {:03}".format(i)
print(output)
print("==================")
m = 12.3456789
x = " m equals {:.3f}".format(m)
print(x)
