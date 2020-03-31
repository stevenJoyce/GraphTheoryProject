# Steven Joyce
# Thompson's construction classes

class State:
<<<<<<< HEAD
    """ A state that has 1 or 2 edges, all edges will be labelled by label """
    # Constructor for the Class
    def __init__(self, label=None, edges=None):
        # Every state has 0,1 or 2 edges from it
        self.edges = edges if edges else []
        # Label for the arrows.None means epsilon.
=======
    # Every state has 0,1 or 2 edges from it
    edges = []

    # Label for the arrows.None means epsilon.
    label = None

    # Constructor for the Class
    def __init__(self, label=None, edges=[]):
        self.edges = edges
>>>>>>> origin/master
        self.label = label

class Fragment:
    # Start state of the NFA fragment
    start = None
    # Accept state of the NFA fragment
    accept = None

    # Constructor
<<<<<<< HEAD
    """ NFA fragment that contains a start state and an accept state """
=======
>>>>>>> origin/master
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

def shunt(infix):
<<<<<<< HEAD
    """ Used to return an infix regular expression in postfix """
    # convert input into stack-ish list
    infix  = list(infix)[::-1]
    #operator stack
=======

    # convert input into stack-ish list
    infix  = list(infix)[::-1]
    #operator stack 
>>>>>>> origin/master
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

def compile(infix):
<<<<<<< HEAD
    """ Used to return an NFA Fragment that represents an infix regular expression"""
    #Convert infix to postfix
    postfix = shunt(infix)
    #Make postfix a stack of characters
    postfix = list(postfix)[::-1]
    #Stack for NFA Fragments
=======
    postfix = shunt(infix)
    postfix = list(postfix)[::-1]

>>>>>>> origin/master
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
<<<<<<< HEAD
            #start State equals frag2.start
            start = frag2.start
            #accept State equals frag1.accept
            accept = frag1.accept
=======
            # create new instance of Fragment to represent the new NFA
            newfrag = Fragment(frag2.start, frag1.accept)
>>>>>>> origin/master
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
<<<<<<< HEAD
=======
            # create new instance of Fragment to represent the new NFA
            newfrag = Fragment(start,accept)
>>>>>>> origin/master
        elif c == '*':
            # pop a single fragment off the stack
            frag = nfa_stack.pop()
            # create new start and accept states
            accept = State()
            start = State(edges=[frag.start, accept])
            # point the arrows
<<<<<<< HEAD
            frag.accept.edges = [frag.start, accep6]
        else:
            accept = State()
            start = State(label=c, edges=[accept])

        # create new instance of fragment to represent the new NFA
        newfrag = Fragment(start, accept)
=======
            frag.accept.edges = [frag.start, accept]
            # create new instance of fragment to represent the new NFA
            newfrag = Fragment(start, accept)
        else:
            accept = State()
            start = State(label=c, edges=[accept])
            # create new instance of fragment to represent the new NFA
            newfrag = Fragment(start, accept)
>>>>>>> origin/master
        # push the new NFA to the NFA stack
        nfa_stack.append(newfrag)

    # The NFA stack should have exactly one NFA on it.
    return nfa_stack.pop()
#follow all the e's arrows and add state to set
def followE(state, current):
    #only run when state has not be visited already
    if state not in current:
        #put state into current
        current.add(state)
        #check if the state is labelled E
        if state.label is None:
            #loop throught the states being pointed to 
            for currState in state.edges:
                #follow all of their E labels as well
                followE(currState, current)

def match(regex, s):
    # This function will return true if and only if the regular expression
    # regex (fully) matches the string s . it returns false otherwise.

    # compile the regular expressions into an NFA
    nfa = compile(regex)
    #Match the regular expression to the string s
    current = set()
    followE(nfa.start, current)
    previous = set()
    
    #looping through the characters in s
    for c in s:
        #to keep track of where we were and are now
        previous = current
        #empty the set to create an empty set about to be used
        current = set()
        #looping through the elements in the previous states
        for state in previous:
            #Only follow arrows not labelled by e - epsilon
            if state.label is not None:
                if state.label == c:
                    #add states at the end of the arrow to current
                    followE(state.edges[0], current)


    # Ask  the NFA if it matches the string s
    return (nfa.accept in current)

<<<<<<< HEAD
    #Test cases for code
if __name__ == "__main__":
    tests =[
        ["a.b|b*", "bbbbbbbb", True],
        ["a.b|b*", "bbx", False],
        ["a.b", "ab", True],
        ["b**", "b", True],
        ["b*", "", True],
    ]

    for test in tests:
        assert match(test[0], test[1]) == test[2],test[0]+ \
        ("should match" if test[2] else "should not match") + test[1]
=======
print(match("a.b|b*","bbbbbbbbbb"))
>>>>>>> origin/master
