import re


def verify_c_list(maxi_value, value, c_list):

    max_value =  max(c_list)

    if value >= max_value:
        return True
    if  value >= maxi_value:
        return True
    else:
        return False


string1 = '''30373
25512
65332
33549
35390
'''

list_input = re.split('\n', string1)

modidied_list_input = [[i for i in cities] for cities in list_input]
visibility_count = (len(modidied_list_input[0])-1)*2 + (len(list_input)-2)*2
print(modidied_list_input)
max_value = len(list_input)-1
comparable_list = []
def calculate(i,number):

    value = modidied_list_input[number][i]
    comparable_list.append(int(value))

def add_first(i,a):
    value = modidied_list_input[i][a]

    comparable_list.append(int(value))

def add_last(number):
    value = modidied_list_input[-2][number]

    comparable_list.append(int(value))

for i in range(1,max_value-1):
    value = len(list_input[i])-1
    first_count = 1
    last_count = 1

    for j in range(1,value):
        if first_count==1:
            add_first(0,i)
            first_count = 0
        calculate(i,j)
        last_count = last_count+1
        if last_count==len(list_input)-2:
            add_last(i)


    print(comparable_list)

    is_row = None
    is_column  = None
    for value in range(1, len(comparable_list)-1):
        output = [int(i) for i in modidied_list_input[value]]

        max_value = max(comparable_list)
        i = verify_c_list(max_value, comparable_list[value], output)
       # print(comparable_list[value])

        if i:
            visibility_count = visibility_count+1

    comparable_list = []


print(visibility_count)






















