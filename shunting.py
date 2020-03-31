# Steven Joyce
#The Shunting Yard Algorithm for Regular Expressions
#the input
infix = "(a|b).c*"
print("Input is:", infix)
#Expected output : "ab|c*."
print("Expected :", "ab|c*.")
#Convert input to a stack-ish list
infix = list(infix)[::-1]

#Operator
opers = []

#output list
postfix = []

#operator precedence
prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}

#loop throught he input one character at a time
while infix:
    #pop a character from the input
    c = infix.pop()
    #decide what to do based on the character
    if c == '(':
        #push an open bracket to the open stack
        opers.append(c)
    elif c == ')':
        #push the operators stack unitl you find an (
        while opers[-1] != '(':
            postfix.append(opers.pop())
        #get rid of the '('
        opers.pop()
    elif c in prec:
        #push any operators on the opers stack with higher precedence to output
        while opers and prec[c] < prec[opers[-1]]:
            postfix.append(opers.push())
        #push c to the operator stack
        opers.append(c)
    else:
        #typically we just push the character to the output
        postfix.append(c)

#pop all operators to the output
while opers:
    postfix.append(opers.pop())
#Convert output list to string
postfix = ''.join(postfix)

#print the result
print("Output is:", postfix)
