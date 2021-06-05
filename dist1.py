# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:42:05 2020

@author: Mahabaleshwara.Bairi
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

x = thisdict["model"]
print (x)

y = thisdict.get("model")
print (y)

thisdict["year"] = 2018
z = thisdict.get("year")
print (z)

print(thisdict)

print ("Print all key names in the dictionary, one by one:")
for x in thisdict:
  print(x)
print ("Print all values in the dictionary, one by one:")
for x in thisdict:
  print(thisdict[x])

print ("You can also use the values() function to return values of a dictionary:")
for x in thisdict.values():
  print(x)
  
print ("Loop through both keys and values, by using the items() function:")
for x, y in thisdict.items():
  print(x, y)
print ('Check if "model" is present in the dictionary:')
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  
print ("Print the number of items in the dictionary:")
print(len(thisdict))

print ("Adding an item to the dictionary is done by using a new index key and assigning a value to it:")
thisdict["color"] = "red"
print(thisdict)
print ("The pop() method removes the item with the specified key name:")
thisdict.pop("model")
print(thisdict)
print ("The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):")
thisdict.popitem()
print(thisdict)

print ("The del keyword removes the item with the specified key name:")
del thisdict["year"]
print(thisdict)

print ("Make a copy of a dictionary with the copy() method:")
mydict = thisdict.copy()
print(mydict)

mydict1 = dict(thisdict)
print(mydict1)

print ("Create a dictionary that contain three dictionaries")
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print (myfamily)
print ("It is also possible to use the dict() constructor to make a new dictionary:")
thisdict12 = dict(brand="Ford", model="Mustang", year=1964)
print (thisdict12)

print ('Get the value of the "model" item:')
car = {
  "brand": "HONDA",
  "model": "CRV",
  "year": 2020
}

c = car.get("model")
print ("***********")
value_1 = car.values()
print (value_1)
print ("***********")
print(c)

c1 = car.keys()

print(c1)


print ("+++++++++++++")
car2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car2.update({"color": "White"})
print (car2)

c2 = car2.setdefault("color", "white")
print(c2)



