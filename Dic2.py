dic1 ={
   "name" : "ali",
   "family" : "mohhebi",
    "age" : 23
}



inexist = "ali" in dic1.values()

if inexist:
    print("yes")
else:
    print("there is Not ")



print("-----------------dict methods----------------------")

copyfrom_d1 = dic1.copy()

print(copyfrom_d1)

print(copyfrom_d1 == dic1)
print(copyfrom_d1 is dic1)



newdic = {}.fromkeys(["name", "family", "age"], "unknown")

print(newdic)



print(dic1["name"])

print("name" in dic1)

x = dic1.get("name")

print(x is None)
