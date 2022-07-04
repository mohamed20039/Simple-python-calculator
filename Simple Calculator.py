first_num=input('Enter First Number: ')
second_num=input('Enter Second Number: ')
#this part tells you the operands that you gomna you use in calculations so use them operands
print('Note:\nUse + as adding\nUse - as minus of subtraction\nUse * as multiplying\nUse / as dividing')
#put your operand here
operand=input('input your operand: ')

if operand=='+':
    try:
        print(int(first_num)+int(second_num))
    except:
        print(float(first_num)+float(second_num))
elif operand=='-':
    try:
        print(int(first_num)-int(second_num))
    except:
        print(float(first_num)-float(second_num))
elif operand=='*':
    try:
        print(int(first_num)*int(second_num))
    except:
        print(float(first_num)*float(second_num))
elif operand=='/':
    try:
        print(int(first_num)/int(second_num))
    except:
        print(float(first_num)/float(second_num))
else:
	print('Error!, Input Valid Operand')
#this part tells you error if put unidentified operand		