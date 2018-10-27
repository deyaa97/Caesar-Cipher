# code starts
alpha = 'abcdefghijklmnopqrstuvwxyz'
final = ''
myinput = input("Enter a String")
key = int(input("Enter Value of Key"))
myinput = myinput.lower()
for x in myinput:
    if(x in alpha):
        pos = alpha.find(x)
        pos = (pos+key)%26
        final+=(alpha[pos])
    else:
        final+=x

print(final)
