#In the workspace at the bottom of the page, there is a piece of code in the user_input_numlist.py Python file. The code prompts the user to enter 10 two-digit numbers. It should then find and print the sum of all of the even numbers among those that were entered.



# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0

# seek user input for ten numbers 
for i in range(10):
    userInput = int(input("Enter any 2-digit number: "))
# print incorrect value warning  when ValueError exception occurs
    number = userInput
    user_list.append(number)
    if number % 2 == 0:
        list_sum += number
    


print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))