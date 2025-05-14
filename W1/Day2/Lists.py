#LISTS

# A list is a sequence of elements

# Syntax
some_list = list('item 1') #to convert other sequence in a list
other_list = ['item 1']  #bets way to create an empty list

print(some_list)
print(other_list) 

print(len(some_list))

#accessing by index
print(some_list[1])

#methods for lists
some_list.append('A')

#methods for lists
my_list.append('A')
print(my_list)

my_list.extend(['A','C','D'])
print(my_list)


#Create an empty list called names and add (using a method) 4 names of your favorite characters in a show
sopranos = ['Character Name']
sopranos.extend(['Tony','Christopher','Meadow','Paulie'])
print(sopranos)

# start >> stop >> step


num_list = list(range(1,8))
print(nums_list)


print(nums_list[2:6])
print(nums_list[:5])

#copy list
copied_list = nums_list[:]
print(copied_list)

copied_list = nums_list.copy()
print(copied_list)

#other methods
# other = insert(where,what)
# remove(what) removes the first occurance of the element
del nums_list[3]
print(nums_list)

nums-list.pop()
print(nums_list)

poped_el = nums_list.pop()
print(poped_el)
print(nums_list)

print(nums_list)

fruits = ['banana', 'orange','lime','apple']

#sorted()
sorted_list = sorted(nums_list)
print(sorted_list)
print(fruits)


#sort()
fruits.sort()
print(fruits)

#index(element) and it returns you the index of the element



#Exersise
#Given this list:
list1 = [5,10,15,20,25,50,20]
# find the value 20 in the list, and if it is present, replace it with 200. Only update the fist occurance
# Hint: look at the index method

if list1.index(20):
  index_found = list1.index(20)
  list1.insert(index_found, 200)
  list1.remove(20)
  print(list1)
else:
  print('element not found')











