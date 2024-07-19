import json
from io import StringIO


json_data1 = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}], sort_keys=True, indent=4)
print(json_data1, type(json_data1), sep='\n')



print(json.dumps("\"foo\bar"))

print(json.dumps('\u1234'))

print(json.dumps('\\'))

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))


io = StringIO()
json.dump(['streaming API'], io)
io.getvalue()

print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':')))


data = {
    'user': 'admin',
    'password': 'password'
}

json_data = json.dumps(data)

print(json_data, type(json_data))

