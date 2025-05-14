#CONDITIONALS : IF STATEMENT

#SYNTAX
# IF CONDITION:
#    <INDENTED BLOCK OF CODE>

# secret_number = 55
# user_number = int(input('Guess a number: '))

# if user_number == secret_number:
#    print('Congrats, you won!')
# elif user_number == 7:
#    print('oh, that\'s my fav number')
# else:
#    print('Sorry, not the same number')

#excercise
number = int(input('add a number'))

if number % 3 == 0 and number % 5 == 0:
    print('fizzbuzz')
elif number % 5 == 0:
    print('Buzz')
elif number % 3 == 0:
    print('Fizz')
else:
    print('not valid')    