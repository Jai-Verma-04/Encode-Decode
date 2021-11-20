# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def encode(inp, value):
    final = " "
    for i in inp:
        temp = ord(i) + value
        temp = chr(temp)
        final+=temp
        
    return final
    
def decode(inp, value):
    final = " "
    for i in inp:
        temp = ord(i) - value
        temp = chr(temp)
        final+=temp
        
    return final


done = False

while not done:
    print("\n")
    print("1. Encode")
    print("2. Decode")
    ch = int(input("Enter your choice: "))
    print("\n")
    
    if ch == 1:
        inp = input("Enter some text: ")
        value = int(input("Enter encode value: "))
        print("Result = ", encode(inp, value))
        
    elif ch == 2:
        inp = input("Enter some text: ")
        value = int(input("Enter decode value: "))
        print("\nResult = ", decode(inp, value))
    else:
        print("Invalid choice!!")
        continue
    
    ask = input("Continue? [y/n]: ").lower()
    
    if ask == 'n': done = True
    else: continue
