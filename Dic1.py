s = dict(name = "ali", age = 32, status = "on")
print(s)
print(type(s))

print("______________________")

print("name is:" ,s["name"])

print("s value is:" ,s.values())

for value in s.values():
    print(value)

print("---------s------------")

v = [print(val) for val in s]

# print(v)

print("--------------")

print(s.keys())

for key in s.keys():
    print(s[key])

print("-------------------")


for k in s.items():
    print(k)

print("-------------------")


for key, value in s.items():
    print(key, value)