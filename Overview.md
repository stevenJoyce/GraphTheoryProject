![](RackMultipart20200518-4-x20wcd_html_9f602a99b3366f46.gif)

|
##
# **Graph Theory Project Report**

 ![](RackMultipart20200518-4-x20wcd_html_49d178840f048537.gif) ![](RackMultipart20200518-4-x20wcd_html_974d118ce6ea344c.gif) |
| --- |
| **Table of Contents**![](RackMultipart20200518-4-x20wcd_html_f0210c35e834828f.gif) |
| Student name: Steven Joyce Student ID: G00362012Lecturer: Ian McLoughlin ![](RackMultipart20200518-4-x20wcd_html_66f126f2148ac934.gif) |
|
 |
|
## **Graph Theory Project Report**
 ![](RackMultipart20200518-4-x20wcd_html_dff76bca174652a9.gif)

# Contents

[Introduction 2](#_Toc40645245)[Problem Statement 2](#_Toc40645246)[Overview 2](#_Toc40645247)[Run 3](#_Toc40645248)[Steps to download the code 3](#_Toc40645249)[Steps to install python 3](#_Toc40645250)[Steps to run the code 3](#_Toc40645251)[Test 4](#_Toc40645252)[Regex file 4](#_Toc40645253)[Shunting file 4](#_Toc40645254)[myScript.py file 4](#_Toc40645255)[RegexUserCommand.py file 5](#_Toc40645256)[Algorithm 6](#_Toc40645257)[Shunting Algorithm 6](#_Toc40645258)[Thompson&#39;s Construction 6](#_Toc40645259)[References 6](#_Toc40645260)[Webpages 6](#_Toc40645261)[Videos 6](#_Toc40645262)


 |
 |

# Introduction

An introduction to your repository and the code. Describe what is contained in the repository and what the code does.

## Problem Statement

You must write a program in the Python programming language [2] that can build a non-deterministic finite automaton (NFA) from a regular expression, and can use the NFA to check if the regular expression matches any given string of text. You must write the program from scratch and cannot use the re package from the Python standard library nor any other external library. A regular expression is a string containing a series of characters, some of which may have a special meaning. For example, the three characters ., |, and \* have the special meanings concatenate, or, and Kleene star respectively. For example, the regular expression 0.1 means a 0 followed by a 1, 0|1 means a 0 or a 1, and 1\* means any number of 1&#39;s. These special characters must be used in your submission. Other special characters you might consider allowing as input are brackets () which can be used for grouping, + which means at least one of, and ? which means zero or one of. You might also decide to remove the concatenation character, so that 1.0 becomes 10, with the concatenation implicit. You may initially restrict the non-special characters your program works with to 0 and 1. However, you should at least attempt to expand these to all the digits, and the characters a to z, and A to Z.

## Overview

This repository contains code written in the programming language Python. It converts a regular expression to a non-deterministic finite automation (NFA). It then checks to see if the NFA matches strings of text. The string of text can be found in 2 different ways – The repository has a few pre-written strings that can be used in the matching process and the user can input in new strings to be used in that process.

# Run

You should explain how to download and run your code, including instructions of how to install Python. Remember, this is to be pitched at students in the year below you.

## Steps to download the code

1. Go to this GitHub repository: [https://github.com/stevenJoyce/GraphTheoryProject](https://github.com/stevenJoyce/GraphTheoryProject)
2. On this page click this button

![](RackMultipart20200518-4-x20wcd_html_83a3a8a635457921.png)

 ![](RackMultipart20200518-4-x20wcd_html_98b601b66dfab1e.gif)
1. When button is clicked this menu appears, click this icon

![](RackMultipart20200518-4-x20wcd_html_c6af3ed647631078.png)

1. Open up your virtual machine
2. Check if virtual machine has git installed using git –version
3. If git is not installed, install it by typing sudo apt install git
4. Create a new folder using mkdir foldername
5. Open the newly created folder by typing cd foldername
6. When folder opens type: git clone and paste in the copied link from step 3

The Repository is now cloned and able to view and use

## Steps to install python

1. Open your virtual machine
2. Check if your vm has vi – this is a programming text editor
3. If it does not

## Steps to run the code

1. When the previous steps have been taken, open the folder using cd.
2. Inside this folder type in cd project2020.
3. Now type ls and make sure these 4 files labelled myScript.py, regex.py, regexUserCommand.py and shunting.py are shown.
4. Type python3 shunting.py to run the tests in the shunting file
5. Type python3 regexUserCommand -nfa &quot;nfa input&quot; -string &quot;string input&quot; to test the file.
6. Lastly type python3 myScript.py to run the myScript file
7. When the first tests are completed, the user can now enter y to run a test of the own

Or n to exit the test. If any other input is entered the user will get the choice again.

# Test

Explain how to run the tests incorporated in your code.

## Regex file

1. This is tested in the myScript file

## Shunting file

1. First type python3 shunting.py to test the shunting file
2. The result should be

![](RackMultipart20200518-4-x20wcd_html_4e555f050e47072c.png)

This file tests the code using the unittest package in python

## myScript.py file

- Now type python3 myScript.py to test the myScript file
- The outputted result should be

![](RackMultipart20200518-4-x20wcd_html_d07b2d23d99b0eea.png)

- If user inputs &quot;y&quot; – the user can run a new search that is all user input

![](RackMultipart20200518-4-x20wcd_html_1a6029159674b34e.png)

- If user inputs any letter or number not &quot;y&quot; or &quot;n&quot; , the output is

![](RackMultipart20200518-4-x20wcd_html_360b7101b23450bb.png)

- If User inputs &quot;n&quot; – the test will end user exits that file

![](RackMultipart20200518-4-x20wcd_html_42dda2c536e6042.png)

- All aspects of the file is now tested

## RegexUserCommand.py file

- To test this file the user will input a custom comparison in the command line using the argparse library in Python3.
  1. The user will type python3 regexUserCommand -nfa &quot;nfa input&quot; -string &quot;string input&quot;

![](RackMultipart20200518-4-x20wcd_html_9dd7a031bacde8ea.png)

1. To get help the user will type in python 3 regexUserCommand -h or –help
![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)

# Algorithm

Give an overview and explanation of the main algorithm(s) in your code. A well-thought out diagram is a great aide here. You may use a referenced diagram from online or, better yet, create your own. Make sure any image displays correctly in GitHub.

## Shunting Algorithm

It is a method for parsing mathematical expressions that are specified in infix notation. It was created by Edsger Dijkstra. It is used to convert an infix expression into a postfix expression.

An Example of this algorithm

Infix === Postfix

(a.b)|c\* -----\&gt; ab|c\*

| **Current Symbol** | **Operator Stack** | **Postfix String** |
| --- | --- | --- |
| A |
 | A |
| . | . | A |
| B | . | AB |
| | | .| | AB| |
| C | . | AB|C |
| \* | . \* | AB|C \*. |

## Thompson&#39;s Construction

Thompson&#39;s construction is a way of converting a regular expression into a non-deterministic finite automation (NFA). It was designed by Ken Thompson. It is also called the McNaughton-Yamada-Thompson Algorithm. We normally would assume the regular expression is a postfix expression. It is already converted using the shunting yard algorithm.

Example taken from [https://www.geeksforgeeks.org/regular-expression-to-nfa/](https://www.geeksforgeeks.org/regular-expression-to-nfa/)

![](RackMultipart20200518-4-x20wcd_html_6b20a865503ef50a.png)

# References

##

## Webpages

[https://en.wikipedia.org/wiki/Thompson%27s\_construction](https://en.wikipedia.org/wiki/Thompson%27s_construction)

[https://www.tutorialspoint.com/automata\_theory/constructing\_fa\_from\_re.htm](https://www.tutorialspoint.com/automata_theory/constructing_fa_from_re.htm)

[https://www.researchgate.net/figure/Thompsons-NFA-construction-The-regular-expression-for-a-character-a-S-corresponds-to\_fig1\_1959575](https://www.researchgate.net/figure/Thompsons-NFA-construction-The-regular-expression-for-a-character-a-S-corresponds-to_fig1_1959575)

[https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse\_args](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args)

[https://docs.python.org/dev/library/argparse.html](https://docs.python.org/dev/library/argparse.html)

[https://www.geeksforgeeks.org/regular-expression-to-nfa/](https://www.geeksforgeeks.org/regular-expression-to-nfa/) - example for Thompson&#39;s construction

## Videos

[https://www.youtube.com/watch?v=6YH9wsLM-8o](https://www.youtube.com/watch?v=6YH9wsLM-8o) – Barry Brown

[https://www.youtube.com/watch?v=RYNN-tb9WxI](https://www.youtube.com/watch?v=RYNN-tb9WxI) – Barry Brown

[https://www.youtube.com/watch?v=84oNUttWlN4&amp;feature=youtu.be&amp;t=105](https://www.youtube.com/watch?v=84oNUttWlN4&amp;feature=youtu.be&amp;t=105) – Neso Academy

[https://www.youtube.com/watch?v=q94B9n\_2nf0](https://www.youtube.com/watch?v=q94B9n_2nf0) - DrapsTV

