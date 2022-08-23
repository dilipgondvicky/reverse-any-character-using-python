#dilipgondvicky
def reverse_string(characterinp): 
    revstr = characterinp[::-1]
    return revstr

while True:
    tkinp = input("\n Enter Any Characters To Reverse \n")
    output = reverse_string(tkinp)
    print("\n Your Reverse Character Is : ", output)
    a = input('\n Type yes to Continue \n Type Somenthing To Exit \n') 
    if a == 'yes':
        continue
    else:
        break
