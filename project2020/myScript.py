# Steven Joyce
#Used to run a few regular expressions and test the algorithms
#User can also run their own tests
#import all classes from regex.py
import regex
print("Steven Joyce - G00362012");
print("Graph Theory Project 2020");
 
#using regex run the match method
#true match
print( "Test to compare a.b|b* to bbbbbb") 
print("result = ",regex.match("a.b|b*","bbbbbb"))
#false match
print("Test to compare a.b|b* to bbx")
print("result = ",regex.match("a.b|b*","bbx"))
#other false match
print("Test to compare a.b to ab")
print("result = ",regex.match("a.b","ab"))
#other true  match
print("Test to compare b** to b")
print("result = ",regex.match("b**","b"))
#empty string match
print("Test to compare b* to empty string " " ")
print("result = ",regex.match("b*",""))

def UserChoice():
    """Used to ask user if they want to run a new test with user input"""
    userchoice = input("Type y to create a new test or n to exit: ")
 
    while userchoice != "n":
        if userchoice == "y":
            #user inputs a new regular expression
            regexExpression = input("Enter a new regular expression: ")
            #user inputs a new string to compare it in match
            compareString = input("Enter String to compare: ")
            print("Answer: ",regex.match(regexExpression, compareString))
	    #re-prompt the user to continue or end program
            userchoice = input("Enter y to create a new test or n to exit: ")
        else:
            print("Error wrong input- please try again")
            userchoice= input("Enter y to create a new test or n to exit: ")

    print("Goodbye")

#run the function
UserChoice()
