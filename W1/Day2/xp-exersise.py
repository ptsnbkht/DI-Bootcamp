# Question 1:

# Create a set called my_fav_numbers and populate it with your favorite numbers
my_fav_numbers = {'7', '10', '3', '13'}

#Add two new numbers to the set.
my_fav_numbers.add(99)
my_fav_numbers.add(100)

#Remove the Last Added Number
my_fav_numbers.remove(100)

#Create and Populate 
friend_fav_numbers = {5, 13, 42}

print("My favorite numbers:", my_fav_numbers)
print("Friend's favorite numbers:", friend_fav_numbers)

print("Our favorite numbers:", my_fav_numbers, friend_fav_numbers)

# Question 2:
my_tuple = (1, 2, 3)
new_tuple = (my_tuple)+(4,5)
print(new_tuple)

#Question 3:
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert("0,Apples")
count_apples = basket.count("Apples")
empty_list = basket.clear

#Question 4:
mixed_numbers = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
mixed_numbers = [x * 0.5 for x in range(3, 11)]

#Question 5:
for number in range(1, 21):
    print(number)

#Even index
for index, number in enumerate(range(1, 21)):
    if index % 2 == 1: 

#Odd index
for index, number in enumerate(range(1, 21)):
    if index % 2 == 0: 

#Question 6 
name = ""

while name != "Paul":
    name = input("Please enter your name?")
  if name == "Bill"
break

print("Please enter your name?")   

#Question 7





