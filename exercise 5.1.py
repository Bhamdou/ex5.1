# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


#task 1
# first_number = int(input("first number: "))
# second_number = int(input("second number: "))
# third_number = int(input("third number: "))

# if first_number == second_number \
#     and first_number == third_number \
#     and second_number== first_number \
#     and second_number== third_number:
#         print(f"The triple sum is: {first_number * 3 + second_number * 3 + third_number * 3 }")
               
# elif first_number != second_number and first_number != third_number:
#     print(f"The sum is:{ first_number + second_number + third_number}")
    
    
    
   
    # #task 2
    
    # num1 = int(input("First number: "))
    # num2 = int(input("Second number: "))
    
    # if num1 > num2:
    #     calc1 =(num1 - num2) * 2
    #     print(f"the result of the calculation is {calc1}")
    # else:
    #     calc2 = abs(num1-num2)
    #     print(f"the result of the calculation is {calc2}")
        
    # num1 = int(input("first number: "))
    # num2 = int(input("first number: "))
    
    # result = abs(num1-num2)
    
    # if num1 > num2:
    #     print(f"the result is: {result*2}")
    # else:
    #     print(f"the result is: {result}")
        
    
    
    



#task 3
# for i in range(3):
    
#   enter_number = int(input("please check this number: "))
 
#   if enter_number %2 == 0:
#     print(f"{enter_number} is an even number.")
#   elif enter_number %2 != 0:
#     print(f"{enter_number} is an odd number")








# #task 5
# import random
# guess_a_number = 0
# random_num = random.randint(1,10)
# while guess_a_number != random_num:
    

#     guess_a_number = int(input("guess a number between 1 and 10 until you get it right :"))
#     print(guess_a_number)
#     if guess_a_number != random_num:
#         print("try it again")
#     else:
#         print("well guessed")



# #task6


# c_or_f = str(input("Convert from Fahrenheit to Celsius please enter c or C, convert from Celsius to Fahrenheit press f or F: ")).lower()
# enter_temperature = float(input("Input the value of the temperature you'd like to convert : "))
# celsius_to_fahrenheit = ((enter_temperature * 1.8) + 32)
# fahrenheit_to_celsius = (enter_temperature - 30) / 2
# if c_or_f == "c":
#  print(f"The temperature in Celsius is {fahrenheit_to_celsius} degrees.")
# elif c_or_f == "f":
#  print(f"The temperature in Fahrenheit is {celsius_to_fahrenheit} degrees.") 






#task7

user_stars = int(input("How many lines of stars do you want? "))
for star in range(user_stars+1):
    print(star * "*")
for star in range(user_stars+1, 0, -1):
    print(star * "*") 


# #task8

# Number1 = 0
# Number2 = 1
# counter = 0
# while counter <= 5:
#     sum = Number1 + Number2
#     print(sum)
#     Number1 = Number2
#     print(f"this is the updated variable Number1: {Number1}")
#     Number2 = sum
#     print(f"this is the updated variable Number2: {Number2}")
#     counter += 1
    
