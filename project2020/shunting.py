# Steven Joyce
#The Shunting Yard Algorithm for Regular Expressions
#default input
infix = "(a|b).c*"
print("Input is:", infix)
#Expected output : "ab|c*."
print("Expected :", "ab|c*.")

#Convert infix variable into a stack-ish list
infix = list(infix)[::-1]
#Operator
opers = []
#output list
postfix = []
#operator order of precedence
prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}

#loop through infix, one character at a time
while infix:
    #pop a character from the input
    c = infix.pop()
    #depending on the character,a different outcome will happen
    if c == '(':
        #push an open bracket to the open stack
        opers.append(c)
    elif c == ')':
        #push the operators stack until you find a ( character
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
        #push the character to the output
        postfix.append(c)
#pop all operators to the output
while opers:
    postfix.append(opers.pop())
#Convert output list to string
postfix = ''.join(postfix)

#print the result
print("Output is:", postfix)
