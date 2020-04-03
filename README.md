# GraphTheoryProject
#Steven Joyce - G00362012

regex.py
	It contains 2 classes called State and Fragment
	The state class is used to give each edge a label inside a constructor
	The fragement class is used to create an NFA that has a start state and an accept state.
	It also contains 4 functions called shunt, compile followE and match. 
	The Shunt function
		is used to return an infix regular expression in a postfix regular expression depending on what order of precedence applies.
	Compile Function
		is used to read the NFA and create a stack for the fragements in the NFA
	Match Function
		is run to compare the string and the NFA. 
		if String is a match it returns true otherwise it returns false
	FollowE function
		This is used to follow all the arrows from each state.
		It is added to the match function to used to compare the string to the the NFA.
		
shunting.py
	Converts an inputted regular expression into an output which is ordered by precedence.
	It uses a while loop that reads the input and ranks the characters by order of precedence.
	The order of precedence is * . | ) (
	The infix precedence is converted into a postfix precedence.
myScript.py
	This is the main runnable code of the program.
	A predefined test is run first before user input it imports the regex.py code into a variable called regex
	A precoded test is created and used.
	A function called UserChoice is used to generate user input.
	It is put into a while loop which has a if/else that will only run the test again if y is inputted. 
	The while loop will not run if n is inputted.
	When user inputs n the program will end. 
