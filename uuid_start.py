import uuid

result = uuid.uuid4()
print("UUID4: ", result)
print(result)
print(result.hex)
print(result.urn)
print("~~~~~~~~~~~~~~~~~\n")

result = uuid.uuid5(uuid.NAMESPACE_DNS,"example.com")
print("UUID5: ", result)
print(result)
print(result.hex)
print(result.urn)

print("~~~~~~~~~~~~~~~~~\n")
