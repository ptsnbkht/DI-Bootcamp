  # Tuples: immutable, there is no notion of an empty tuple

  my_tuple = ('TLV')
  print(type(my_tuple))

#convert a sequence into a tuple
my_tuple = tuple(range(11))
print(my_tuple)

password = ('abc','cde','123', 'abc')
print(password.count('abc'))

#accessing by index
print(passwords[1])

#wordaround on how to change tuples:
temp_list = list(my_tuple)
temp_list.extend(['A','B','C'])
my_tuple = tuple(temp_list)
print(my_tuple)

#SETS: 
# not ordered: (cant access by index)
# dont allow for duplicated elements

set = set()
countries = {'Israel', 'USA', 'Brazil'}
names = {'Shimon', 'Hanna', 'Israel'}

print(countries[1]) #typeerror: 'set' object is not subscriptable

person_country = countries.intersection(names)
print(person_country)


