import random

# dictionaries: always key:value pairs
#   Key is always a string/text (in quotes)
#   values can by any python object

phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}

"""
mydictionary = dict(m=8, n=9)
print(mydictionary)

print(f"Number of key-value pairs:  {len(mydictionary)}")




print()
print("*****  start section 1 - print dictionary ********")
print()


print()
print("*****  end section 1 ********")
print()



print()
print("*****  start section 2 - search dictionary ********")
print()

# is case sensitive, failed reference is called a "key error"
print(phonebook["Chris"])


print()
print("*****  end section 2 ********")
print()



print()
print("*****  start section 3 - edit/append dictionary ********")
print()

# updates if already found
phonebook["Chris"] = "555-4444"

# creates if not found
phonebook["Joe"] = "555-0123"

print(phonebook)


print()
print("*****  end section 3 ********")
print()




print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

print(phonebook)
# will throw key error if key does not exist
del phonebook["Chris"]
print(phonebook)

print()
print("*****  end section 4 ********")
print()




print()
print("*****  start section 5 - iterate through keys, values, items ********")
print()

# naturally iterates through keys
for key in phonebook:
    print(f"The key is: {key} and the value is {phonebook[key]}")

for k, v in phonebook.items():
    print(f"The key is {k} and the value is {v}")

print()
print("*****  end section 5 ********")
print()





print()
print("*****  start section 6 - using get and clear ********")
print()

name = "Chris"

# can give a default value if it does not find a match
phone = phonebook.get(name, "key not found")

print(phone)

phonebook.clear()

print()
print("*****  end section 6 ********")
print()



print()
print("*****  start section 7 - using pop method ********")
print()

remove = phonebook.pop("Chris", "not found")

print(remove)


print()
print("*****  end section 7 ********")
print()



print()
print('*****  start section 8 - using popitem ********')
print()






print()
print('*****  end section 8 ********')
print()


"""
print()
print("*****  start section 9 - using random and converting to list ********")
print()

list_of_keys = list(phonebook)
random_key = random.choice(list_of_keys)
print(phonebook[random_key])

print(phonebook[random.choice(list(phonebook))])


print()
print("*****  end section 9 ********")
print()
