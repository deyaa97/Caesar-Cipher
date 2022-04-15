# code starts
alpha = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
final = ''

myinput = input("Enter a String\n")
key = int(input("Enter Value of Key\n"))
myinput = myinput.lower()

for x in myinput:
    if(x in alpha):
        pos = alpha.find(x)
        pos = (pos+key)%26
        final+=(alpha[pos])
    # add function for numbers
    elif (x in num):
        pos = num.find(x)
        pos = (pos+key)%10
        final+= (num[pos])
        
    else:
        final+=x

print(final)
