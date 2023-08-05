def task1():    # define a function named "task1"
    name = "Eusuf"  # string type value assign in variable mannually
    age = 23    # int type value assign in variable mannually
    print("My name is %s and I am %d years old." % (name ,age) )    #print a string with value of two variable

def task2():    # define a function named "task2"
    num1 = 1    # int type value assign in variable mannually
    num2 = 1.652    # int type value assign in variable mannually
    num1_float = float(num1) # type casting int to float
    num2_int = int(num2)    # type casting float to int
    print("num1 :", num1 , "its data type is " + str(type(num1)))   #print a string with value of variable and data type using type()
    print("num1_float :", num1_float , "its data type is " + str(type(num1_float)))     #print a string with value of variable and data type using type()
    print("num2 :", num2 , "its data type is " + str(type(num2) ) )        #print a string with value of variable and data type using type()
    print("num2_int :", num2_int , "its data type is " + str(type(num2_int) ))      #print a string with value of variable and data type using type()

def task3():    # define a function named "task3"
    a = "\"Python programming is fun!\""    #string type value assign in variable mannually
    print("Length of" + a + " is " , len(a))    #print a string with value of variable and length of a string using len()
    print("8th character (index 7) in the string is " + a[8] )  #print a string with variable value of index number 8
    b = a[1:7]  # assign a sub-string into a variable from index 1 to index 7
    print(b + " I enjoy it!")       #print a string with value of variable which contain sub-string

def task4():    # define a function named "task4"
    fruits = [ "apple", "banana", "cherry", "date"]     #string type value assign in list variable mannually
    fruits.append("grape")      #string type value assign in list variable by using append()
    fruits.remove("banana")     #string type value remove from list variable by using remove()
    print("Length of the list is " , len(fruits))   #print a string with value of list variable and length of that list using len()
    sliced_fruits = fruits[2:4]     # assign few value from list into a variable from index 2 to index 4
    extra_fruits = ["kiwi" , "lemon"]       #string type value assign in list variable mannually
    combined = sliced_fruits + extra_fruits     # concatenate two list using + operator
    print("combined list are : " , combined)    #print a string with value of list variable

def task5():    # define a function named "task5"
    num = 5     # int type value assign in variable manually
    mod = num % 2       # assign value of modules of a variable devided by 2
    if mod > 0:     # check condition. if it true then traverse into code block. otherwise jump to else branch
        print(num, " is an odd number.")    #print a string with value of variable
    else:  # if ,condition not true then interpreter jump to this branch
        print(num, " is an even number.")   #print a string with value of variable

def task6():    ## define a function named "task6"
    i = 0       # int type value assign in variable mannually
    print("Number from 0 to 10 :")      #print a string
    while (i <= 10) :   # continue loop until condition became false
        print( i )      #print a string with value of variable
        i = i + 1       # add 1 with value of i for continue a loop
    j = 0       # int type value assign in variable mannually
    sum = 0     # int type value assign in variable mannually
    while (j <= 100) :      # continue loop until condition became false
        sum = sum + j
        j = j + 1       # add 1 with value of j for continue a loop
    print("sum of numbers from 1 to 100 is " , sum)     #print a string with value of variable

# Task 7 :
def calculate_square (num):     # define a function named "calculate_square". with a parameter
    num = int(input("Enter a number: "))    # type casting str to int and take input from user
    print("Square of ",num," is " , (num*num) )     #print string with value of variable and multiplication operation of variable
def is_prime (num):     # define a function named "is_prime". with a parameter
    num = int(input("Enter a number: "))    # type casting str to int and take input from user
    i = 2   # int type value assign in variable mannually
    t = 0   # int type value assign in variable mannually
    while (i <= (num/2)) :      # continue loop until condition became false
        if (num % i == 0) : # check condition. if it true then traverse into code block. otherwise jump to else branch
            t = 1   # int type value assign in variable mannually for flagging
        i = i + 1   # add 1 with value of i for continue a loop

    if (t == 1) :  # check condition. if it true then travarse into code block. otherwise jump to else segment
        print(num, " is not prime")     #print a string with value of variable
    else :      # if ,condition not true then interpreter jump to this branch
        print(num, " is prime")     #print a string with value of variable

# Task 8 :

def task8():    # define a function named "task6"
    student = {
        "name" : "Eusuf Abdullah" ,
        "age" : 23 ,
        "grade" : "1st Class"
    }   #string type value assign in key of Dictionaries  mannually
    student["course"] = "WebEngr"   #string type value assign in key of dictonary  mannually
    print(student)  #print a Dictionaries
    print("All key-value pairs: ")      #print a string
    for i,j in student.items():  # assign value of key and value of Dictionaries using in keyword under a loop
        print(i,":",j)      #print Dictionaries key and value

# call those declared function bellow
task1()
print("\n") #print new line

task2()
print("\n")

task3()
print("\n")

task4()
print("\n")

task5()
print("\n")

task6()
print("\n")

calculate_square(7)     # value pass into function
is_prime(29)    # value pass into function
print("\n")

task8()



