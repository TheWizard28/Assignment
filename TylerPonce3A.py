#This program will be able to arrange shopping expenses and costs from lowest to highest
from functools import reduce

def main():
    my_list = [] #This will be the beginning of our list
    numbers = [100, 200,300, 400, 500, 600, 700, 800, 900, 1000] #This will be base for determining the highest and lowest expenses
    sum_result = reduce(my_list, numbers)

    while True:
        s = input('Enter your monthly expense and the cost:')#This is where the user will enter their expenses
        if len(s) == 0:
            break
        my_list.append(s)
    my_list.sort() #This will place the expenses in order
    print('Here are your monthly expenses:')
    for a_word in my_list:
        print(a_word, end='')

main()