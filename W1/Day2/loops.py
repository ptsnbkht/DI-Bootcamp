#Loops: For and While Loops

# for loop

fruits = ['apple', 'banana', 'kiwi', 'pear']

for each_fruit in fruits:
    print(f'I love {each_fruit}') 
for i in range(1,10):
    print(i)
for i in range(len(fruits)+1):
    print(i)


#Print list of odd numbers
    odd_nums list(range(1,11,2))
    print(odd_nums)
    
    
    print(min(odd_nums))
    print(max(odd_nums))
    print(sum(odd_nums))


# While loop: condition

num = 0
while num <= 10:
    print(num)
    num += 1
    
#break
num = 0
while num <= 10:
    if num == 5:
    print(num)
    num += 1    




secret_num = 77



while user_num != secret_num:
      user_num = input('try a number')
            if user_num =='q':
            break
      user_num = int(input('try a number'))
else:
    print('congrats you won')
