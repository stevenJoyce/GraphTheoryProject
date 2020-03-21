<<<<<<< HEAD
#Steven Joyce - classes used in Thompson's Constructions

class State:
   #Every State has 0, 1 or 2 edges from it
   edges =[]

   #labels for the arrows, none means epsilon
   label = None

   #Constructor for the class
   def __init__(self, label=None, edges=[]):
       self.label = label
       self.edges = edges

class Fragment:
    #start state of NFA fragment
    start=None
    #accept state of NFA fragment
    accept=None

    #constructor
    def __init__(self,start,accept):
        self.start = start

        self.accept=accept


def regex_compile(infix):
    postfix = shunt_(infix)



def match(regex, s):
    #this function returns true only if the regular expression
    #regex matches the string s completely. It returns false otherwise
    
    #compiles the regular expression into an NFA
    nfa = regex_compile(regex)
    #Aks the NFA if the regualr expression matches the string s
    nfa.match(s)

=======
# Steven Joyce
# Thompson's construction classes

class State:
    # Every state has 0,1 or 2 edges from it
    edges = []

    # Label for the arrows.None means epsilon.
    label = None

    # Constructor for the Class
    def __init__(self, label=None, edges=[]):
        self.edges = edges
        self.label = label

class Fragment:
    # Start state of the NFA fragment
    start = None
    # Accept state of the NFA fragment
    accept = None

    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

def shunt(infix):

    # convert input into stack-ish list
    infix  = list(infix)[::-1]
    #operator stack 
    opers = []
    #output list.
    postfix = []
    # operator precedence
    prec = {'*':100, '.':80, '|':60, ')':40, '(':20}
    # Loop through the input one character at a time
    while infix:
        # pop a character  from the input.
        c = infix.pop()
        # Decide what to do based on the character
        if c == '(':
            # push an open bracket to the opers stack
            opers.append(c)
        elif c == ')':
            # pop the operator stack until you find (.
            while opers[-1] != '(':
                postfix.append(opers.pop())
            # get rid of the '('# expected output; "ab|c*."
            opers.pop()
        elif c in prec:
            # push any operators on the opers stack with higher prec to the output.
            while opers and prec[c] < prec[opers[-1]]:
                postfix.append(opers.pop())
            # push c to the operator stack
            opers.append(c)
        else:
            # Typically, we just push the character to the output
            postfix.append(c)

    # pop all operators to the output
    while opers:
        postfix.append(opers.pop())

    # convert output list to string
        return ''.join(postfix)

def regex_compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix)[::-1]

    nfa_stack = []

    while postfix:
        # pop a character from postfix
        c = postfix.pop()
        if c == '.':
            # pop two fragments off the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # point frag2's accept state at frag1's start state
            frag2.accept.edges.append(frag1.start)
            # create new instance of Fragment to represent the new NFA
            newfrag = Fragment(frag2.start, frag1.accept)
        elif c == '|':
            # pop two fragments off the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # create new start and accept states
            accept = State()
            start = State(edges=[frag2.start, frag1.start])
            # point the old accept states at the new one
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)
            # create new instance of Fragment to represent the new NFA
            newfrag = Fragment(start,accept)
        elif c == '*':
            # pop a single fragment off the stack
            frag = nfa_stack.pop()
            # create new start and accept states
            accept = State()
            start = State(edges=[frag.start, accept])
            # point the arrows
            frag.accept.edges = [frag.start, accept]
            # create new instance of fragment to represent the new NFA
            newfrag = Fragment(start, accept)
        else:
            accept = State()
            start = State(label=c, edges=[accept])
            # create new instance of fragment to represent the new NFA
            newfrag = Fragment(start, accept)
        # push the new NFA to the NFA stack
        nfa_stack.append(newfrag)

    # The NFA stack should have exactly one NFA on it.
    return nfa_stack.pop()

def match(regex, s):
    # This function will return true if and only if the regular expression
    # regex (fully) matches the string s . it returns false otherwise.

    # compile the regular expressions into an NFA
    nfa = regex_compile(regex)
    # Ask  the NFA if it matches the string s.
    return nfa

print(match("a.b|b*","bbbbbbbbbb"))
>>>>>>> 1d9bc2ca1e501dd8abe9bc86041c09bfd8c9edc1
