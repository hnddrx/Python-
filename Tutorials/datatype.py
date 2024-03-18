"""
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

intVariable = 5
print(type(intVariable))
stringVariable = "This"
print(type(stringVariable))
floatVariable = 5.5
print(type(floatVariable))
complexVariable = 1j
print(type(complexVariable))
listVariable = ['l','i','s','t']
print(type(listVariable))
tupleVariable = ("apple", "banana", "cherry")
print(type(tupleVariable))
rangeVariable = range(6)
print(type(rangeVariable))
dictVariable = {"name" : "John", "age" : 36}
print(type(dictVariable))
setVariable = {"apple", "banana", "cherry"}
print(type(setVariable))
frozensetVariable = frozenset({"apple", "banana", "cherry"})
print(type(frozensetVariable))
boolVariable = True
print(type(boolVariable))
bytesVariable = b"Hello"
print(type(bytesVariable))
bytearrayVariable = bytearray(5)
print(type(bytearrayVariable))
memoryviewVariable = memoryview(bytes(5))
print(type(memoryviewVariable))
nonetypeVariable = None
print(type(nonetypeVariable))