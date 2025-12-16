
#factors
#using a while loop
#a basic comment can be added using the editor

'''
#standard check to make sure input is valid
answer = False
while(answer == False):
    number = input("Please enter an integer between 1 and 5000: ")
    answer = number.isdigit()
    if answer == True:
        if (int(number) > 0 and int(number) < 5001):
            print("\nThank you!\n")
        else:
            print("\nThis integer is not between 1 and 5000!\n")
            answer = False
    else:
        print("\nThis is not an integer!\n")

#to get here the number must be a valid integer but still currently a string
number = int(number) 

#calculate and print out factors
x = 1 #counter variable
while(x <= number): #loop through all possible numbers
    if(number % x == 0): #check to see if the current number is a factor
        print(str(x) + " is a factor of " + str(number)) #if so print it out
    x += 1 #increase counter
'''


#factors
#using for loop

'''
#standard check to make sure input is valid
answer = False
while(answer == False):
    number = input("Please enter an integer between 1 and 5000: ")
    answer = number.isdigit()
    if answer == True:
        number = int(number) # is a number so convert once here
        if (number > 0 and number < 5001):
            print("\nThank you!")
        else:
            print("\nThis integer is not between 1 and 5000!\n")
            answer = False
    else:
        print("This is not an integer!\n")

#if we are here we have a valid integer between 1 and 5000        
#calculate and print out factors
print()
for x in range(1, number + 1): #loop through all possible numbers
    if(number % x == 0): #check to see if the current number is a factor
        print(x, "is a factor of", number) #if so print it out
'''


#factors
#excluding the values of 1 and the number itself as factors

'''
#standard check to make sure input is valid
answer = False
while(answer == False):
    number = input("Please enter an integer between 1 and 5000: ")
    answer = number.isdigit()
    if answer == True:
        number = int(number) # is a number so convert once here
        if (number > 0 and number < 5001):
            print("\nThank you!")
        else:
            print("\nThis integer is not between 1 and 5000!\n")
            answer = False
    else:
        print("This is not an integer!\n")

#if we are here we have a valid integer between 1 and 5000        
#calculate and print out factors
print()
for x in range(2, number): #loop through all possible numbers
    if(number % x == 0): #check to see if the current number is a factor
        print(x, "is a factor of", number) #if so print it out
'''




