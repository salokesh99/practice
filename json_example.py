import json

a ='{ "name":"John", "age":30, "city":"New York"}'

# load json data as python object
b = json.loads(a)

#dump python object into json

print(b)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

y = json.dumps(x)

print(y)

