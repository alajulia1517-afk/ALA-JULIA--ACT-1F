import time
from datetime import date


#makes the letters appear one at a time
def slow_print(text, delay=0.1):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

#shows my name, section, and title 
slow_print("\n     ====== PYTHON TUTORIAL ======", 0.05)
slow_print("       BY: ALA, JULIA MARIE AJOC   ", 0.01)
slow_print("                  ACT‑1F", 0.01)
print("="*50)
#it prints the exact date when you open the code
today = date.today()
print(f" Today's Date: {today.strftime('%B %d, %Y')}")  
print("=" * 50)
#asking the user to enter his/her name 
name = input("\n Hello !!!! Please enter your name:  ")
slow_print(f"WELCOME, {name.upper()}! TO PROGRAMMING LANGUAGE TUTORIAL", 0.05)
print("=" * 50)
#pause the program 
slow_print("\n****READY TO LEARN PYTHON PROGRAMMING?****", 0.001)
time.sleep(1)
print("   PRESS ENTER TO BEGIN YOUR LESSON..... ")
input()
print("\n         LET'S START :) !!!!!")
time.sleep(1)

#while true = keep looping until the user pick exit() /the main loop
while True:
    #notes = it creates an empty list where the user can enter their own notes each lesson 
    notes = []
    #shows all lesson
    print("\n     Pick a lesson number (1—7)")
    print("[1] Introduction to Programming")
    print("[2] Python Basic Syntax")
    print("[3] Arithmetic Operators and Expressions")
    print("[4] Basic Input and Output in Python")
    print("[5] Conditional Statements in Python")
    print("[6] Logical Operator")
    print("[7] Introduction to Iteration and Loops")
    print("=" * 40)
    #checks if the user enter a umber 
    choice = input("\nEnter lesson number: ")
    if choice.isdigit():
        num = int(choice)
#shows the lesson 1
        if num == 1:
            print("\n<><><> LESSON 1: INTRODUCTION TO PROGRAMMING <><><>")
            print("• A programming language is a special language that computers understand and use to perform tasks.")
            print("• Common programming languages include: Python, C/C++, PHP, Java, JavaScript, Ruby.")
            print("• Python is a widely‑used programming language created by Guido van Rossum in 1991.")
            print("• Guido van Rossum is a Dutch software engineer. He designed Python to be simple, readable, and easy to learn.")
            print("• Python is a high‑level, interpreted, general‑purpose programming language.")
            print("\nWhy learn Python?")
            print("1. Simple and easy to learn – Great for beginners")
            print("2. Readable syntax – Code looks almost like English")
            print("3. Versatile – Used in AI, web, automation, games, and more")
            print("4. Huge community – Lots of support, tutorials, and libraries")
            print("\nTools you need to start: PyCharm, VS Code, Jupyter Notebook / JupyterLab")
            
            #a loop inside a loop / nested loop
            while True:
                #a sub menu where yo7 can choose what to do next 
                opt = input("""\nPress [s] for summary,
      [q] for mixed quiz,
      [c] for mini code activity,
      [n]notes
      [m] back to main menu:   
      [e] Exit   :""").lower()
                
                #the summary of lesson 1
                if opt == "s":
                    print("""\n~~~~ SUMMARY ~~~~
• Programming languages let computers follow instructions
• Python was created by Guido van Rossum in 1991
• It is beginner‑friendly, readable, versatile, and has a big community
• Common tools: PyCharm, VS Code, Jupyter Notebook
""")
                #quiz of lesson 1
                elif opt == "q":
                    print("\n=== QUIZ: (5 ITEMS TOTAL) ===")
                    #the start and the total of the quizzes 
                    score = 0
                    total = 5

                    q1 = input("Q1: Who created Python? ")
                    if q1.lower() == "guido van rossum":
                        print("Correct!")
                        #add 1 point to the 0 if the answer is correct
                        score += 1
                    else:
                        print(" Answer: Guido van Rossum")

                    q2 = input("Q2: What year was Python first released? ")
                    if q2 == "1991":
                        print(" Correct!")
                        score += 1
                    else:
                        print("Answer: 1991")

                    print("\nQ3: What is Python?")
                    print("a. Compiled language by Bjarne Stroustrup")
                    print("b. Java by Sun Microsystems")
                    print("c. High‑level, interpreted, general‑purpose language")
                    ans = input("Your answer: ").lower()
                    if ans == "c":
                        print("Correct!")
                        score += 1
                    else:
                        print(" Wrong.")

                    print("\nQ4: Which is not a Python tool?")
                    print("a. VS Code")
                    print("b. Jupyter Notebook")
                    print("c. WPS Office")
                    ans = input("Your answer: ").lower()
                    if ans == "c":
                        print("Correct!")
                        score += 1
                    else:
                        print("Wrong.")

                    print("\nQ5: Which is not a programming language?")
                    print("a. C++")
                    print("b. Python")
                    print("c. Word#")
                    ans = input("Your answer: ").lower()
                    if ans == "c":
                        print("Correct!")
                        score += 1
                    else:
                        print(" Wrong.")

                    print(f"\nQuiz Score: {score}/{total}")
                    if score >= 4:
                        print("       GOOD JOB!!!")
                    elif score >= 2:
                        print("       NICE!!")
                    else:
                        print("       It’s okay, review the lesson more!")
                 
                #mini code 
                elif opt == "c":
                    print("\n=== MINI CODE ACTIVITY ===")
                    print("Try to fix this code ")
                    print(" 'Hello, World!', (), print ")
                    ans_L1=input("Enter your answer : ")
                    if ans_L1 == "print('Hello, World!')":
                        print("Good job!!")
                    else:
                        print("Nice try! That is your first Python output.")
                #this will go back to main menu 
                elif opt == "m":
                    break
                 #end of the program 
                elif opt == "e":
                    print(f"\n                    THANK YOU FOR USING PYTHON TUTORIAL,{name}!!! ")
                    print("                                   HAPPY CODING :)")
                    print("""\nThe best way to learn a new programming language is by writing programs in it — one step at a time."
— Dennis Ritchie""")    
                    #stops the program
                    exit()
                    #users can add notes 
                elif opt == "n":
                    print("\n YOUR LESSON 1 NOTES")
                    print("-" * 40)
                    for i, note in enumerate(notes, 1):
                        print(f"{i}. {note}")
                    print("-" * 40)
                    new_note = input("Add a new note: ")
                    if new_note:
                      notes.append(new_note)
                      print("Note saved!")
                  
                else: 
                     print("Invalid input! Enter s, q, c, n, e, or m only.")

        elif num == 2:
            print("\n<><><> LESSON 2: PYTHON BASIC SYNTAX <><><>")
            print("Syntax refers to the set of rules that tells us how to correctly write a program in Python.")
            print()
            print("1. Python is Case‑Sensitive")
            print("Python treats uppercase and lowercase letters differently.")
            print('Example: name = "John" and print(name) is correct, but print(Name) will give an error.')
            print()
            print("2. Indentation")
            print("Unlike other programming languages, Python uses indentation (spaces) to define blocks of code.")
            print("Example: after an if‑statement, the code inside must be indented.")
            print()
            print("3. The print() Function")
            print("print() displays information on the screen.")
            print('• Text (string) must be inside quotes: print("Hello, World!")')
            print("• Numbers can be printed without quotes: print(100), print(25.5)")
            print()
            print("4. Python Comments")
            print("Comments are ignored by Python. They are used to explain the code.")
            print("• Single‑line: starts with #")
            print('• Multi‑line: wrapped with triple quotes """ """')
            print()
            print("5. Variables and Naming Rules")
            print("A variable is a named storage location that holds data. Its value can change.")
            print("Rules:")
            print("‑ Must start with a letter or underscore _")
            print("‑ Cannot start with a number")
            print("‑ No spaces or special characters like #, @")
            print("‑ Case‑sensitive: age and AGE are two different variables")

            while True:
                opt = input("""\nPress [s] for summary,
      [q] for mixed quiz,
      [c] for mini code activity,
      [n]notes
      [m] back to main menu:   
      [e] Exit    :""").lower()
       

                if opt == "s":
                    print("""
SUMMARY:
• Python basic syntax are the rules for writing proper code
• It is case‑sensitive and uses indentation to separate code blocks
• print() shows output; text uses quotes, numbers do not
• Comments explain code and are ignored by Python
• Variables store changeable data and follow fixed naming rules
""")

                elif opt == "q":
                    print("\n=== QUIZ: (5 ITEMS TOTAL) ===")
                    score = 0
                    total = 5

                    q1 = input("Q1: What symbol marks a single‑line comment? ")
                    if q1 == "#":
                        print(" Correct!")
                        score += 1
                    else:
                        print("wrong. the correc Answer is: #")

                    q2 = input("Q2: What separates blocks of code in Python? ")
                    if q2.lower() in ["indentation", "spaces"]:
                        print(" Correct!")
                        score += 1
                    else:
                        print(" Answer: Indentation")

                    print("\nQ3: Which is a valid variable name?")
                    print("a. 67_score")
                    print("b. 2option")
                    print("c. slow_burn")
                    print("d. just‑m3")
                    ans = input("Your answer: ").lower()
                    if ans == "c":
                        print(" Correct!")
                        score += 1
                    else:
                        print("Wrong. The correct answer is: c [slow_burn]")

                    print("\nQ4: Why is Print('Hi') wrong?")
                    print("A. Missing quote")
                    print("B. Python is case‑sensitive")
                    print("C. Needs indent")
                    print("D. Invalid comment symbol")
                    ans = input("Enter A/B/C/D: ").upper()
                    if ans == "B":
                        print("Correct!")
                        score += 1
                    else:
                        print("Wrong. The correct answer is: B [Python is case sensitive]")

                    print("\nQ5: What does Python use for code blocks?")
                    print("A. Brackets")
                    print("B. Indentation")
                    print("C. @")
                    print("D. #")
                    ans = input("Enter A/B/C/D: ").upper()
                    if ans == "B":
                        print("Correct!")
                        score += 1
                    else:
                        print(" Wrong. The correct answer is: B [Indentation]")

                    print(f"\nQuiz Score: {score}/{total}")
                    if score >= 4:
                        print("       GOOD JOB!!!")
                    elif score >= 2:
                        print("       NICE!!")
                    else:
                        print("       It’s okay, review the lesson more!")

                elif opt == "c":
                    print("\n=== MINI CODE ACTIVITY ===")
                    print("Task: Fix this invalid variable and print it.")
                    print("Wrong: 4name = 'Lila'")
                    code_ans=input("Press Enter for the correct version: ")
                    if code_ans == "name = 'Lila' ":
                        print("name = 'Lila'")
                    else:
                        print("Wrong, Remember variables cannot start with numbers.")

                elif opt == "m":
                    break
                elif opt == "e":
                    print(f"\n                    THANK YOU FOR USING PYTHON TUTORIAL,{name}!!! ")
                    print("                                   HAPPY CODING :)")
                    print("""\nThe best way to learn a new programming language is by writing programs in it — one step at a time."
— Dennis Ritchie""")    
                    exit()
                elif opt == "n":
                    print("\n YOUR LESSON 2 NOTES")
                    print("-" * 40)
                    for i, note in enumerate(notes, 1):
                        print(f"{i}. {note}")
                    print("-" * 40)
                    new_note = input("Add a new note: ")
                    if new_note:
                      notes.append(new_note)
                      print("Note saved!")
                else:
                    print("Invalid input! Enter s, q, c, or m only.")
                    
        elif num == 3:
            print("\n<><><> LESSON 3: ARITHMETIC OPERATORS AND EXPRESSIONS <><><>")
            print("What are Arithmetic Operators?")
            print("Arithmetic operators are symbols used to perform mathematical calculations on numbers. They work the same way as the operators used in everyday mathematics.")
            print("\nExpressions in Python")
            print("An expression is a combination of values, variables, and operators that evaluates to a result.")
            print("\nOperator Examples (a = 10, b = 5):")
            a = 10
            b = 5
            print(f"Addition           :{a} + {b} =", a + b)
            print(f"Subtraction      :{a} - {b}  =", a - b)
            print(f"Multiplication  :{a} * {b}  =", a * b)
            print(f"Division            :{a} / {b}  =", a / b)
            print(f"Floor Division  :{a} // {b} =", a // b)
            print(f"Modulus           :{a} % {b} =", a % b)
            print(f"Exponentiation:{a} ** {b} =", a ** b)
            print("\nSample Expression: Student Grade Average")
            math = 90
            science = 85
            english = 88
            average = (math + science + english) / 3
            print(f"Average Grade: {average:.2f}")
            print("\nNote: Python follows PEMDAS for the order of operations.")

            while True:
                opt = input("""\nPress [s] for summary,
      [q] for mixed quiz,
      [c] for mini code activity,
      [n]notes
      [m] back to main menu:   
      [e] Exit  :""").lower()
       

                if opt == "s":
                    print("\n~~~~ SUMMARY ~~~~")
                    print("• Arithmetic operators perform math calculations.")
                    print("• An expression combines values, variables, and operators.")
                    print("• Python supports addition, subtraction, multiplication, division, floor division, modulus, and exponentiation.")
                    print("• It follows PEMDAS for the order of operations.")

                elif opt == "q":
                    print("\n=== QUIZ: (5 ITEMS TOTAL) ===")
                    score = 0
                    total = 5

                    q1 = input("Q1: What operator gives the remainder? ")
                    if q1 in ["%", "modulus"]:
                        print("Correct!")
                        score += 1
                    else:
                        print(" Answer: % / Modulus")

                    q2 = input("Q2: What is a combination of values and operators called? ")
                    if q2.lower() == "expression":
                        print("Correct!")
                        score += 1
                    else:
                        print("Answer: Expression")

                    print("\nQ3: Which is exponentiation?")
                    print("A. *")
                    print("B. /")
                    print("C. **")
                    print("D. //")
                    ans = input("Enter A/B/C/D: ").upper()
                    if ans == "C":
                        print("Correct!")
                        score += 1
                    else:
                        print("Wrong. The correct answer is: C [**]")

                    print("\nQ4: Which follows PEMDAS?")
                    print("A. Variable naming")
                    print("B. Order of operations")
                    print("C. Indentation")
                    print("D. Input")
                    ans = input("Enter A/B/C/D: ").upper()
                    if ans == "B":
                        print(" Correct!")
                        score += 1
                    else:
                        print("Wrong.The correct answer is: B [order of operations]")
                        print(f"\nQuiz Score: {score}/{total}")
                    if score >= 4:
                        print("       GOOD JOB!!!")
                    elif score >= 2:
                        print("       NICE!!")
                    else:
                        print("       It’s okay, review the lesson more!")
        
                elif opt == "c":
                    print("\n=== MINI CODE ACTIVITY ===")
                    print("What's missing?")
                    print("Correct the code so age is stored as a whole number:")
                    print("age = ____(input('Enter your age: '))")
                    ans_L3 = input("Your answer: ")
                    if ans_L3 == "int":
                        print("Good job!! int() converts input to an integer!")
                    else:
                        print("Nice try! The answer is: int")
                        print("Correct code: age = int(input('Enter your age: '))")
                            
                elif opt == "m":
                    break
                    
                elif opt == "e":
                    print(f"\n                    THANK YOU FOR USING PYTHON TUTORIAL,{name}!!! ")
                    print("                                   HAPPY CODING :)")
                    print("""\nThe best way to learn a new programming language is by writing programs in it — one step at a time."
— Dennis Ritchie""")    
                    exit()
                elif opt == "n":
                    print("\n YOUR LESSON 3 NOTES")
                    print("-" * 40)
                    for i, note in enumerate(notes, 1):
                        print(f"{i}. {note}")
                    print("-" * 40)
                    new_note = input("Add a new note: ")
                    if new_note:
                      notes.append(new_note)
                      print("Note saved!")
                else:
                    print("Invalid input! Enter s, q, c, or m only.")    
        
        
        elif num == 4:
            print("\n=== LESSON 4: BASIC INPUT AND OUTPUT IN PYTHON ===")
            print("• Purpose of input: Lets programs receive data or responses from the user.")
            print("• Real‑life analogy: Asking for a person’s name and giving a reply based on what they entered.")
            print("• input() function:")
            print("  Syntax: variable = input(\"Prompt message: \")")
            print("  Default: Every value you type in is saved as a string (text).")
            print("\nExample:")
            print("name = input(\"Enter your name: \")")
            print("age = input(\"Enter your age: \")")
        
            print("\nFormatting Output")
            print("• Use a comma inside print() to show text together with stored values.")
            print("\nExample:")
            print("name = input(\"Enter your name: \")")
            print("age = input(\"Enter your age: \")")
            print("print(\"Name: \", name)")
            print("print(\"Age: \", age)")
        
            print("\nConverting Input to Other Data Types")
            print("All input starts as text; convert it if you need numbers or True/False values.")
            print("• Integer (whole numbers): age = int(input(\"Enter your age: \"))")
            print("• Float (decimal numbers): grade = float(input(\"Enter your grade: \"))")
            print("• Boolean (True / False): Compare user answers to get True or False.")
        
            print("\nCombined full example:")
            print("name = input(\"Enter your name: \")")
            print("age = int(input(\"Enter your age: \"))")
            print("grade = float(input(\"Enter your final grade: \"))")
            print("print(f\"Student: {name}, Age: {age}, Final Grade: {grade}\")")
        
            while True:
                opt = input("""\nPress [s] for summary,
      [q] for mixed quiz,
      [c] for mini code activity,
      [n]notes
      [m] back to main menu:   
      [e] Exit  :""").lower()
       
        
                if opt == "s":
                    print("""\n~~~~ SUMMARY ~~~~
        • input() receives user data; by default it stores text as a string.
        • print() displays output on the screen.
        • Use int() to convert input into whole numbers.
        • Use float() to convert input into decimal numbers.
        • Combine input, conversion, and print to build interactive Python programs.
        """)
        
                elif opt == "q":
                    print("\n=== QUIZ: (5 ITEMS TOTAL) ===")
                    score = 0
                    total = 5
        
                    
                    q1 = input("Q1: What built‑in function is used to collect user input? ")
                    if q1.lower() in ["input", "input()"]:
                        print("Correct!")
                        score += 1
                    else:
                        print(" Answer: input()")
        
                    q2 = input("Q2: What function sends and displays output to the screen? ")
                    if q2.lower() in ["print", "print()"]:
                        print(" Correct!")
                        score += 1
                    else:
                        print(" Answer: print()")
        
                    print("\nQ3: What data type does input() return by default?")
                    print("A. Integer")
                    print("B. Float")
                    print("C. String")
                    print("D. Boolean")
                    ans = input("Enter A/B/C/D: ").upper()
                    if ans == "C":
                        print(" Correct!")
                        score += 1
                    else:
                        print("Wrong.The correct answer is: C [String]")
        
                    print("\nQ4: Which function converts a value into a whole number?")
                    print("A. str()")
                    print("B. int()")
                    print("C. float()")
                    print("D. bool()")
                    ans = input("Enter A/B/C/D: ").upper()
                    if ans == "B":
                        print(" Correct!")
                        score += 1
                    else:
                        print("Wrong.The correct answer is: B [int()]")
        
                    print("\nQ5: Which function converts input into decimal numbers?")
                    print("A. int()")
                    print("B. float()")
                    print("C. print()")
                    print("D. input()")
                    ans = input("Enter A/B/C/D: ").upper()
                    if ans == "B":
                        print("Correct!")
                        score += 1
                    else:
                        print(" Wrong.The correct answer is: B [float()]")
        
                    print(f"\nQuiz Score: {score}/{total}")
                    if score >= 4:
                        print("       GOOD JOB!!!")
                    elif score >= 2:
                        print("       NICE!!")
                    else:
                        print("       It’s okay, review the lesson more!")
        
                elif opt == "c":
                    print("\n=== MINI CODE ACTIVITY ===")
                    print("What's missing?")
                    print("Correct the code so age is stored as a whole number:")
                    print("age = ____(input('Enter your age: '))")
                    ans_L3 = input("Your answer: ")
                    if ans_L3 == "int":
                        print("Good job!! int() converts input to an integer!")
                    else:
                        print("Nice try! The answer is: int")
                        print("Correct code: age = int(input('Enter your age: '))")
        
                elif opt == "m":
                    break
                    
                elif opt == "e":
                    print(f"\n                    THANK YOU FOR USING PYTHON TUTORIAL,{name}!!! ")
                    print("                                   HAPPY CODING :)")
                    print("""\nThe best way to learn a new programming language is by writing programs in it — one step at a time."
— Dennis Ritchie""")    
                    exit()
                elif opt == "n":
                    print("\n YOUR LESSON 4 NOTES")
                    print("-" * 40)
                    for i, note in enumerate(notes, 1):
                        print(f"{i}. {note}")
                    print("-" * 40)
                    new_note = input("Add a new note: ")
                    if new_note:
                      notes.append(new_note)
                      print("Note saved!")
                else:
                    print("Invalid input! Enter s, q, c, or m only.")    
        
        elif num == 5:
            print("\n<><><> LESSON 5: CONDITIONAL STATEMENTS IN PYTHON <><><>")
            print("Conditional statements let a program make decisions, running code only when a condition evaluates to True or False.")

            print("\n• Relational / Comparison Operators")
            print("These compare two values and always return True or False:")
            print("  ==   Equal to")
            print("  !=   Not equal to")
            print("  >    Greater than")
            print("  <    Less than")
            print("  >=   Greater than or equal to")
            print("  <=   Less than or equal to")
            print("Example: score = 85; score >= 75 → True")

            print("\n• if Statement")
            print("Syntax:")
            print("if condition:")
            print("    statement(s)")
            print("Runs the indented block only if the condition is True. If False, the block is skipped.")
            print("Example:")
            print("age = 20")
            print("if age >= 18:")
            print("    print(\"You are an adult.\")")

            print("\n• if‑else Statement")
            print("Gives an alternate block to run when the if condition is False. Only one block runs.")
            print("Syntax:")
            print("if condition:")
            print("    statement")
            print("else:")
            print("    statement")
            print("Example: score = 65; if score >=75: print('Passed') else: print('Failed')")

            print("\n• if‑elif‑else Statement")
            print("Used for multiple conditions. Python checks from top to bottom; it runs the FIRST True block and skips the rest.")
            print("Syntax:")
            print("if condition1:")
            print("    statement")
            print("elif condition2:")
            print("    statement")
            print("else:")
            print("    statement")
            print("Example: grading system for Excellent, Very Good, Passed, Failed")

            while True:
                opt = input("""\nPress [s] for summary,
      [q] for mixed quiz,
      [c] for mini code activity,
      [n]notes
      [m] back to main menu:   
      [e] Exit      :""").lower()
       

                if opt == "s":
                    print("""\n~~~~ SUMMARY ~~~~
• Conditional statements let Python make decisions based on True / False conditions.
• Relational operators compare values: ==, !=, >, <, >=, <=.
• if runs code only when the condition is True.
• if‑else adds an alternative action for False results.
• if‑elif‑else handles many conditions; only the first true block executes.
• Always use proper indentation for conditional blocks.
""")

                elif opt == "q":
                    print("\n=== QUIZ:(5 ITEMS TOTAL) ===")
                    score = 0
                    total = 5

                 
                    q1 = input("Q1: What is the result always returned by relational operators? ")
                    if q1.lower() in ["true or false", "true / false", "boolean"]:
                        print("Correct!")
                        score += 1
                    else:
                        print(" Answer: True or False")

                    q2 = input("Q2: What keyword adds extra conditions inside a conditional block? ")
                    if q2.lower() == "elif":
                        print("Correct!")
                        score += 1
                    else:
                        print(" Answer: elif")

                    
                    print("\nQ3: Which operator checks if two values are equal?")
                    print("A. =")
                    print("B. ==")
                    print("C. =>")
                    print("D. ->")
                    ans = input("Enter A/B/C/D: ").upper()
                    if ans == "B":
                        print("Correct!")
                        score += 1
                    else:
                        print(" Wrong.The correct answer is: B [==]")

                    print("\nQ4: Which statement provides an alternative action when the if condition fails?")
                    print("A. elif")
                    print("B. else")
                    print("C. if")
                    print("D. for")
                    ans = input("Enter A/B/C/D: ").upper()
                    if ans == "B":
                        print(" Correct!")
                        score += 1
                    else:
                        print(" Wrong.The correct answer is: B [else]")

                    print("\nQ5: In if‑elif‑else, what happens once Python finds the first True condition?")
                    print("A. It runs all remaining blocks")
                    print("B. It executes that block and skips the rest")
                    print("C. It automatically runs else")
                    print("D. It rechecks every condition")
                    ans = input("Enter A/B/C/D: ").upper()
                    if ans == "B":
                        print("Correct!")
                        score += 1
                    else:
                        print("Wrong.The correct answer is: B [It executes that block and skips the rest]")

                    print(f"\nQuiz Score: {score}/{total}")
                    if score >= 4:
                        print("       GOOD JOB!!!")
                    elif score >= 2:
                        print("       NICE!!")
                    else:
                        print("       It’s okay, review the lesson more!")

                elif opt == "c":
                    print("\n=== MINI CODE ACTIVITY ===")
                    print("Fill in the blank:")
                    print("score = int(input('Enter your score: '))")
                    print("if score ____ 75:")
                    print("    print('Passed')")
                    print("else:")
                    print("    print('Failed')")
                    ans = input("\nYour answer: ")
                    if ans == ">=":
                       print("Good job!!")
                    else:
                       print(" Wrong. The correct answer is: >=")

                elif opt == "m":
                    break
                elif opt == "e":
                    print(f"\n                    THANK YOU FOR USING PYTHON TUTORIAL,{name}!!! ")
                    print("                                   HAPPY CODING :)")
                    print("""\nThe best way to learn a new programming language is by writing programs in it — one step at a time."
— Dennis Ritchie""")    
                    exit()
                elif opt == "n":
                    print("\n YOUR LESSON  5 NOTES")
                    print("-" * 40)
                    for i, note in enumerate(notes, 1):
                        print(f"{i}. {note}")
                    print("-" * 40)
                    new_note = input("Add a new note : ")
                    if new_note:
                      notes.append(new_note)
                      print("Note saved!")
                else:
                    print("Invalid input! Enter s, q, c, or m only.")
        elif num == 6:
            print("\n<><><> LESSON 6: LOGICAL OPERATORS <><><>")
            print("Logical operators combine or flip boolean conditions, often used together with if, elif, and else statements. Python has three logical operators: and, or, not.")

            print("\n• and Operator")
            print("Returns True only when ALL conditions are True. If any one is False, the whole result becomes False.")
            print("Example: age >= 18 and age <= 60 → both must be True.")
            print("Truth rule: True and True = True; all other combinations give False.")

            print("\n• or Operator")
            print("Returns True if at least ONE condition is True. It only becomes False when every condition is False.")
            print("Example: day == 'Saturday' or day == 'Sunday'")
            print("Truth rule: If any side is True, the result is True.")

            print("\n• not Operator")
            print("It reverses the boolean result: True turns into False, and False turns into True.")
            print("Example: if not is_raining: runs when is_raining equals False.")

            print("\nQuick guide:")
            print("  and → all true")
            print("  or → at least one true")
            print("  not → flip the result")

            while True:
                opt = input("""\nPress [s] for summary,
      [q] for mixed quiz,
      [c] for mini code activity,
      [n]notes
      [m] back to main menu
      [e] Exit    :""").lower()
       

                if opt == "s":
                    print("""\n~~~~ SUMMARY ~~~~
• Logical operators combine or reverse True / False conditions.
• and: True only if every condition is True.
• or: True if at least one condition is True.
• not: Inverts the boolean value.
• They work well with conditional statements to build multi‑condition decisions.
""")

                elif opt == "q":
                    print("\n=== QUIZ:  (5 ITEMS TOTAL) ===")
                    score = 0
                    total = 5

                    
                    q1 = input("Q1: What logical operator reverses a boolean result? ")
                    if q1.lower() == "not":
                        print(" Correct!")
                        score += 1
                    else:
                        print(" Answer: not")

                    q2 = input("Q2: Which operator requires all conditions to be True? ")
                    if q1.lower() == "and":
                        print("Correct!")
                        score += 1
                    else:
                        print("Answer: and")

                  
                    print("\nQ3: When will the or operator return False?")
                    print("A. If one condition is True")
                    print("B. If all conditions are False")
                    print("C. If you use not")
                    print("D. If only two conditions exist")
                    ans = input("Enter A/B/C/D: ").upper()
                    if ans == "B":
                        print("Correct!")
                        score += 1
                    else:
                        print("Wrong.The correct answer is: B [If all conditions are False]")

                    print("\nQ4: What is the result of True and False?")
                    print("A. True")
                    print("B. False")
                    print("C. Not")
                    print("D. Depends")
                    ans = input("Enter A/B/C/D: ").upper()
                    if ans == "B":
                        print("Correct!")
                        score += 1
                    else:
                        print("Wrong.The correct answer is: B [False]")

                    print("\nQ5: What does 'not True' evaluate to?")
                    print("A. True")
                    print("B. False")
                    print("C. and")
                    print("D. or")
                    ans = input("Enter A/B/C/D: ").upper()
                    if ans == "B":
                        print("Correct!")
                        score += 1
                    else:
                        print("Wrong.B [False]")

                    print(f"\nQuiz Score: {score}/{total}")
                    if score >= 4:
                        print("       GOOD JOB!!!")
                    elif score >= 2:
                        print("       NICE!!")
                    else:
                        print("       It’s okay, review the lesson more!")

                elif opt == "c":
                    print("\n=== MINI CODE ACTIVITY ===")
                    print("Fill in the blank:")
                    print("age = int(input('Enter age: '))")
                    print("if age >= 13 ____ age <= 19:")
                    print("    print('You are a teenager')")
                    print("else:")
                    print("    print('Not a teenager')")
                    ans = input("\nYour answer: ")
                    if ans.lower() == "and":
                       print("Good job!!")
                    else:
                       print("Nice try! The correct answer is: and")

                elif opt == "m":
                    break
                elif opt == "e":
                    print(f"\n                    THANK YOU FOR USING PYTHON TUTORIAL,{name}!!! ")
                    print("                                   HAPPY CODING :)")
                    print("""\nThe best way to learn a new programming language is by writing programs in it — one step at a time."
— Dennis Ritchie""")    
                    exit()
                elif opt == "n":
                    print("\n YOUR LESSON 6 NOTES")
                    print("-" * 40)
                    for i, note in enumerate(notes, 1):
                        print(f"{i}. {note}")
                    print("-" * 40)
                    new_note = input("Add a new note : ")
                    if new_note:
                      notes.append(new_note)
                      print("Note saved!")
                else:
                    print("Invalid input! Enter s, q, c, or m only.")
 
 
       
        elif num == 7:
            print("\n<><><> LESSON 7: INTRODUCTION TO ITERATION AND LOOPS <><><>")
            print("Iteration means repeating a set of instructions; every repeat is called an iteration. Loops make this easier instead of rewriting the same code many times. Python has two main loop types: for loop and while loop.")

            print("\n• for Loop")
            print("Used when you already know how many times to repeat. It runs for each item inside a sequence, like range().")
            print('Syntax: for variable in sequence: then your indented code. Example: for number in range(3): print("Welcome to Python!")')
            print("range(start, stop, step): stop value is excluded; you can count forward or backward.")

            print("\n• while Loop")
            print("Repeats only while a condition stays True. It checks the condition first before running the block.")
            print("while True makes an endless repeat; use break to stop it.")
            print("Example: keep asking for a name until the user types X to exit.")

            print("\nQuick guide:")
            print("  iteration = repetition of code")
            print("  for = fixed number of repeats")
            print("  while = repeat based on a condition")

            while True:
                opt = input("""\nPress [s] for summary,
      [q] for mixed quiz,
      [c] for mini code activity,
      [n]notes
      [m] back to main menu:   
      [e] Exit""").lower()
       

                if opt == "s":
                    print("""\n~~~~ SUMMARY ~~~~
• Iteration is repeating instructions; each repetition is one iteration.
• The for loop repeats for items in a sequence, best if you know the repeat count.
• The while loop runs while its condition is True. while True loops forever until break.
• Use colon after loop headers and indent the loop body.
• range lets you count forward or backward; its ending number will not be included.
""")

                elif opt == "q":
                    print("\n=== QUIZ:  (5 ITEMS) ===")
                    score = 0
                    total = 5

                    q1 = input("Q1: What do we call one single repetition of a loop? ")
                    if q1.lower() == "iteration":
                        print(" Correct!")
                        score += 1
                    else:
                        print(" Answer: iteration")

                    q2 = input("Q2: Which loop is best if you know exactly how many times to repeat? ")
                    if q2.lower() == "for":
                        print(" Correct!")
                        score += 1
                    else:
                        print(" Answer: for loop")

                    print("\nQ3: What will range(1,6) print?")
                    print("A. Numbers 1 to 6")
                    print("B. Numbers 1 to 5")
                    print("C. Only the number 6")
                    print("D. No numbers")
                    ans = input("Enter A/B/C/D: ").upper()
                    if ans == "B":
                        print(" Correct!")
                        score += 1
                    else:
                        print(" Wrong. The correct answer is: B [Numbers 1 to 5]")
                        

                    print("\nQ4: What statement stops an endless while True loop?")
                    print("A. print")
                    print("B. break")
                    print("C. for")
                    print("D. range")
                    ans = input("Enter A/B/C/D: ").upper()
                    if ans == "B":
                        print(" Correct!")
                        score += 1
                    else:
                        print(" Wrong.The correct answer is: B [break]")

                    print("\nQ5: When does a while loop stop running?")
                    print("A. Automatically after three times")
                    print("B. When its condition becomes False")
                    print("C. When you use for")
                    print("D. It never stops")
                    ans = input("Enter A/B/C/D: ").upper()
                    if ans == "B":
                        print(" Correct!")
                        score += 1
                    else:
                        print(" Wrong.The correct answer is: B [When its condition becomes False]")

                    print(f"\nQuiz Score: {score}/{total}")
                    if score >= 4:
                        print("       AMAZING WORK!")
                    elif score >= 2:
                        print("       GOOD JOB!")
                    else:
                        print("       Review loops again, you got this!")

                elif opt == "c":
                    print("\n=== MINI CODE ACTIVITY ===")
                    print("Fill in the blank:")
                    print("number = 5")
                    print("while number ____ 1:")
                    print("    print(number)")
                    print("    number -= 1")
                    ans = input("\nYour answer: ")
                    if ans in [">=", ">="]:
                       print("Good job!! ")
                    else:
                       print("Nice try! The correct answer is: >=")
                elif opt == "m":
                    break
                elif opt == "e":
                    print(f"\n                    THANK YOU FOR USING PYTHON TUTORIAL,{name}!!! ")
                    print("                                   HAPPY CODING :)")
                    print("""\nThe best way to learn a new programming language is by writing programs in it — one step at a time."
— Dennis Ritchie""")    
                    exit()
                elif opt == "n":
                    print("\n YOUR LESSON 7 NOTES")
                    print("-" * 40)
                    for i, note in enumerate(notes, 1):
                        print(f"{i}. {note}")
                    print("-" * 40)
                    new_note = input("Add a new note : ")
                    if new_note:
                      notes.append(new_note)
                      print("Note saved!")
                else:
                    print("Invalid input! Enter s, q, c, or m only.")
 
 
                                         