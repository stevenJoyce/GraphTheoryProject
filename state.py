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

