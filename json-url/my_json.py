import json

# some JSON:
x =  '{ "name":"Barış", "age":30, "city":"İstanbul"}'


# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(y["name"])