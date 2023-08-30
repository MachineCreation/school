                                                                # Note to staff or other person that reads this. I left the code lines that I used to debug and test the code in tact in case I needed it again. I hope thats not beyond the parameters of the assignment

                                                                # Question 1
                                                                # Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    print(f'Hello_{user_name.upper()}!')


hello_name('world')


                                                                # Question 2
                                                                # Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    for i in range(1, 100):
        if i % 2 != 0:
            print(i)

first_odds()
            
                                                                # Question 3
                                                                # Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    a_list.sort()
#    print(a_list[-1])
    return a_list[-1]

#max_num_in_list([1,7,3,4,2,8,9])

                                                                # Question 4
                                                                # write a function to return if a given year is a leap year. A leap year is divisable by 4 but not by 100 unless its also divisable by 400. return bool

def is_leap_year(a_year):
    if ((a_year % 400 == 0) or (a_year % 100 != 0) and (a_year % 4 == 0)):
#        print(True)
        return True
    else:
#        print(False)
        return False

# is_leap_year(2001)

                                                                # Question 5 
                                                                # Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    if sorted(a_list) == list(range(min(a_list),max(a_list)+1)):
        print(True)
        return True
    else:
        print(False)
        return False
    
#is_consecutive([1,2,3,4,5,6])
#is_consecutive([8,5,7,3,4,5])