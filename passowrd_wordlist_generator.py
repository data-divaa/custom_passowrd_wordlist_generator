'''
author: data-divaa
desc: A password wordlist generator that generates password combinations for bruteforce with inputs such as name, birthyear, phonenumber, current year
version: 1.0
'''

from itertools import product
import sys

special_chars = ["_","-","@","#","$","!","%"]

#function to generate various combinations of lower and upper case character of the string
def generate_name_combinations(name):
    l1 = []
    for i in product(*[(ch.lower(),ch.upper()) for ch in name]):
        l1.append("".join(i))
    return l1


#function to generate combinations with different symbols and birth year
def birth_year_combinations(name_list,birth_year):
    lst = []
    for i in name_list:
        for j in special_chars:
            lst.append(i + j + birth_year)
    return [k for k in lst]


#function to generate combinations with current year
def current_year_combinations(name_list,current_year):
    lst = []
    for i in name_list:
        for j in special_chars:
            lst.append(i + j + current_year)
    return [k for k in lst]


#function to generate combinations with mobile number
def mobile_number_combinations(name_list,mobile_number):
    lst = []
    for i in name_list:
        for j in special_chars:
            lst.append(i + j + mobile_number)
    return [k for k in lst]

########################################################################33


#taking input for name
name = input("enter your name: ").strip()
if not name:
    print("NAME IS REQUIRED!!!")
    print("Existing the Program")
    sys.exit()
name_result = generate_name_combinations(name)

#copying the outputs from password_generate function for furthur use
final_result = name_result.copy()


#taking input for birthday
b_year = input("enter your birthyear(press enter to skip):").strip()
b_year = str(b_year)
if b_year and len(b_year) == 4 and b_year.isdigit():
    final_result.extend(birth_year_combinations(name_result,b_year))
elif b_year and (len(b_year) != 4 or not(b_year.isdigit())):
    print("INVALID INPUT EXISTING THE PROGRAM")
    sys.exit()


#taking input for current year
c_year = input("enter the current year(press enter to skip):").strip()
if c_year and len(c_year) == 4 and c_year.isdigit():
    c_year = str(c_year)
    final_result.extend(current_year_combinations(name_result,c_year))
elif c_year and (len(c_year) != 4 or not(c_year.isdigit())):
    print("INVALID INPUT EXISTING THE PROGRAM")
    sys.exit()


#taking inputs for mobile number
m_num = input("enter mobile number(press enter to skip):").strip()
m_num = str(m_num)
if m_num and len(m_num) == 10 and m_num.isdigit():
    final_result.extend(mobile_number_combinations(name_result,m_num))
elif m_num and (len(m_num) != 10 or not(m_num.isdigit())):
    print("INVALID INPUT EXISTING THE PROGRAM")
    sys.exit()



#to print the final file with the output
with open("pass_wordlist.txt", "w") as file:
    file.write("\n".join(final_result))

print(" Output file has been created with name - 'pass_wordlist.txt'")
