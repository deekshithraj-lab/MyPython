"""
PyLearn quiz bank: 15 questions per topic.
Keeps the Question, Quiz, and evaluate() interface used by app.py.
"""

class Question:
    def __init__(self, prompt, options, correct_answer, explanation):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation


class Quiz:
    def __init__(self, title, questions):
        self.title = title
        self.questions = questions

    def evaluate(self, answers):
        score, feedback = 0, []
        for index, question in enumerate(self.questions):
            selected = answers.get(index, "")
            correct = selected == question.correct_answer
            score += int(correct)
            feedback.append({
                "question": question.prompt,
                "selected": selected or "Not answered",
                "correct_answer": question.correct_answer,
                "correct": correct,
                "explanation": question.explanation,
            })
        return score, feedback


def q(prompt, options, answer, why):
    return Question(prompt, options, answer, why)


# Each topic below contains 15 questions, mixing output prediction,
# debugging, syntax, and concept checks.
BANK = {
"Introduction": [
("What is Python?", ["A programming language","A browser","A database","An operating system"],"A programming language","Python is a general-purpose programming language."),
("What displays text in Python?", ["echo()","print()","show()","display_text()"],"print()","print() displays values."),
("Output of print('Hello')?", ["Hello","'Hello'","print(Hello)","Error"],"Hello","Quotes mark the string but are not printed."),
("Python file extension?", [".py",".pt",".python",".p"],".py","Python source files commonly end in .py."),
("Which is valid Python?", ["print('Hi')","PRINT('Hi')","print 'Hi'","show('Hi')"],"print('Hi')","Python is case-sensitive and print() uses parentheses."),
("Output of print(2 + 3)?", ["23","5","2 + 3","Error"],"5","Addition is evaluated before printing."),
("What starts a single-line comment?", ["//","#","<!--","**"],"#","Python comments start with #."),
("Output of print(10 // 3)?", ["3.33","3","1","4"],"3","// performs floor division."),
("Which function reads user input?", ["input()","print()","len()","type()"],"input()","input() reads text from the user."),
("Output of print('Py' + 'thon')?", ["Python","Py thon","Py+thon","Error"],"Python","The + operator joins strings."),
("Find the error: print('Welcome'", ["Missing closing parenthesis","Missing variable","Wrong comment symbol","No error"],"Missing closing parenthesis","The function call needs a closing parenthesis."),
("What does # TODO mean?", ["A comment for a future task","A Python keyword","A loop","A data type"],"A comment for a future task","Comments are ignored by Python."),
("Output of print(type(7).__name__)?", ["str","float","int","number"],"int","The type name for 7 is int."),
("Which is a valid variable name?", ["first-name","2name","first_name","class"],"first_name","Underscores are allowed; keywords and leading digits are not."),
("Why are comments useful?", ["Explain code to readers","Run faster than code","Create variables","Fix all errors"],"Explain code to readers","Comments help humans understand code."),
],
"Variables": [
("Which symbol assigns a value?", ["==","=","!=","+"],"=","A single equals sign assigns a value."),
("Output of x = 5; print(x)?", ["x","5","Error","None"],"5","x stores 5."),
("Output of x=4; x=x+3; print(x)?", ["4","3","7","43"],"7","The stored value increases by three."),
("Which is a valid variable name?", ["user-name","user_name","3users","for"],"user_name","Underscores are allowed in identifiers."),
("Value after a=8; a=2?", ["8","2","10","Error"],"2","The second assignment replaces the first."),
("Output of name='Mia'; print(name)?", ["name","Mia","'Mia'","Error"],"Mia","print displays the string value."),
("Which stores a decimal number?", ["price='2.5'","price=2.5","price==2.5","price=float"],"price=2.5","2.5 without quotes is a float."),
("Find the error: 2value = 10", ["Name cannot start with a digit","Number is too small","Equals is forbidden","No error"],"Name cannot start with a digit","Identifiers cannot begin with a digit."),
("Output of a=3; b=a; print(b)?", ["a","3","b","Error"],"3","b receives the value of a."),
("What does total += 4 mean?", ["Set total to 4","Add 4 to total","Compare total with 4","Convert total to text"],"Add 4 to total","+= adds to the existing value."),
("Output of print(2, 5)?", ["25","2 5","2,5","Error"],"2 5","print separates arguments with spaces by default."),
("Which is a Python keyword?", ["score","student_age","while","my_score"],"while","while is reserved for loop syntax."),
("Output of count=1; count=count*4; print(count)?", ["1","4","5","14"],"4","The new value is one times four."),
("What error occurs when printing an undefined variable?", ["NameError","SyntaxError","IndentationError","KeyError"],"NameError","Python cannot find the variable name."),
("Output of a='5'; print(a*2)?", ["10","55","5 5","Error"],"55","String multiplication repeats the text."),
],
"Data Types": [
("Which type represents whole numbers?", ["str","int","bool","list"],"int","int represents integers."),
("What is the type of 'Hello'?", ["int","float","str","bool"],"str","Quoted text is a string."),
("Type name of 3.14?", ["int","float","str","decimal"],"float","A decimal literal is a float."),
("Which is a Boolean value?", ["'True'","1.0","True","'False'"],"True","True without quotes is a bool."),
("Output of int('12') + 3?", ["123","15","'123'","Error"],"15","int converts '12' to integer 12."),
("Which collection is ordered and changeable?", ["tuple","list","int","bool"],"list","Lists are ordered and mutable."),
("Type of (1, 2, 3)?", ["list","tuple","dict","set"],"tuple","Parentheses and commas create a tuple."),
("Which is a dictionary literal?", ["[1, 2]","{'a': 1}","(1, 2)","{1, 2}"],"{'a': 1}","A dictionary stores key-value pairs."),
("Output of bool(0)?", ["True","False","0","None"],"False","Zero is falsy."),
("What does str(25) return?", ["Integer 25","Text '25'","25.0","Error"],"Text '25'","str converts an integer to text."),
("Which represents no value?", ["0","False","None","''"],"None","None is Python's null-like value."),
("Output of len('cat')?", ["2","3","4","cat"],"3","The string has three characters."),
("Find the error: 'age' + 2", ["Cannot directly combine str and int","Strings cannot print","Integers need quotes","No error"],"Cannot directly combine str and int","Convert one value to a compatible type first."),
("Which type is immutable?", ["list","dict","tuple","set"],"tuple","Tuple items cannot be reassigned."),
("Type name of [1, 2]?", ["tuple","list","dict","set"],"list","Square brackets create a list."),
],
"User Input": [
("Which function reads keyboard input?", ["print()","input()","type()","len()"],"input()","input reads user-entered text."),
("What type does input() return by default?", ["int","float","str","bool"],"str","input returns a string."),
("How do you convert input to an integer?", ["int(input())","input(int)","str(input())","integer(input())"],"int(input())","int converts numeric text to an integer."),
("If input is '8', what is input()*2?", ["16","88","8 8","Always error"],"88","String multiplication repeats the text."),
("User enters 6: n=int(input()); print(n+1). Output?", ["61","7","6","Error"],"7","The input is converted to integer 6."),
("Which line displays a prompt?", ["name=input('Name: ')","name=print('Name: ')","input=name('Name: ')","read('Name: ')"],"name=input('Name: ')","The argument to input is shown as a prompt."),
("Find the issue: age=input(); print(age+1)", ["age is str, not int","input cannot read digits","print cannot display variables","No issue"],"age is str, not int","Convert age with int(age) before arithmetic."),
("Which reads a decimal?", ["float(input())","decimal(input())","input(float)","int('float')"],"float(input())","float converts text to a floating-point value."),
("User types Sam; print('Hi', name) after name=input(). Output?", ["Hi name","Hi Sam","SamHi","Error"],"Hi Sam","The entered value is stored in name."),
("int('hello') raises which exception?", ["TypeError","ValueError","NameError","KeyError"],"ValueError","The text cannot be parsed as an integer."),
("Which is appropriate for a name?", ["name=input('Name: ')","name=int(input())","name=float(input())","name=bool(input())"],"name=input('Name: ')","Names are normally kept as strings."),
("What does input('Choice: ') do?", ["Shows prompt and waits","Prints the answer","Converts to int","Stops the program"],"Shows prompt and waits","The prompt is displayed before reading input."),
("How can invalid integer input be handled?", ["try/except around int(input())","Assume all input is numeric","Use print instead of int","Rename input"],"try/except around int(input())","ValueError can be handled with try/except."),
("What does input().isdigit() return for '12'?", ["True","False","12","Error"],"True","The string contains only digit characters."),
("Why convert input before numeric calculations?", ["input returns text","input returns a list","print changes types","Python has no numbers"],"input returns text","Convert the input string to the intended numeric type."),
],
"Operators": [
("Output of 4 + 3 * 2?", ["14","10","11","9"],"10","Multiplication happens before addition."),
("What does == test?", ["Assignment","Equality","Division","Identity only"],"Equality","== compares values."),
("Output of 10 // 3?", ["3.33","3","1","4"],"3","// performs floor division."),
("Output of 10 % 3?", ["3","1","0","3.33"],"1","% returns the remainder."),
("Output of 2 ** 3?", ["6","8","9","5"],"8","** is exponentiation."),
("Output of 5 != 5?", ["True","False","5","Error"],"False","The values are equal, so != is false."),
("Output of not True?", ["True","False","None","Error"],"False","not reverses a Boolean."),
("Output of True and False?", ["True","False","0","None"],"False","and requires both operands to be true."),
("Output of 3>1 and 2<5?", ["True","False","3","Error"],"True","Both comparisons are true."),
("Which adds to an existing variable?", ["=+","+=","==","++"],"+=","+= adds the right-side value."),
("Output of 7 / 2 in Python 3?", ["3","3.5","4","1"],"3.5","/ performs true division."),
("Output of (2 + 3) * 4?", ["14","20","24","9"],"20","Parentheses are evaluated first."),
("Find the issue: if x = 3:", ["Use comparison == in a condition","Colon is invalid","x cannot be a variable","No issue"],"Use comparison == in a condition","Use x == 3 to test equality."),
("Output of 4 in [2, 4, 6]?", ["True","False","4","Error"],"True","in checks membership."),
("Output of 'a' + 'b'?", ["ab","a b","Error","a+b"],"ab","+ concatenates strings."),
],
"If Statements": [
("Which keyword begins a condition?", ["for","def","if","return"],"if","if begins a conditional branch."),
("What does == check?", ["Assignment","Equality","Addition","A loop"],"Equality","== compares values."),
("Output if x=5 and x>3: print('Yes')?", ["Yes","No","5","Nothing"],"Yes","The condition is true."),
("Which keyword checks another condition?", ["elseif","elif","else if","then"],"elif","Python uses elif."),
("What does else do?", ["Runs if earlier conditions are false","Always runs first","Defines a function","Repeats a block"],"Runs if earlier conditions are false","else is the fallback branch."),
("If condition is False, which branch runs?", ["if branch","else branch","both always","neither always"],"else branch","The else branch runs when the condition is false."),
("Find the syntax error: if x > 0 print(x)", ["Missing colon","x must be text","print needs no parentheses","No error"],"Missing colon","An if header ends with a colon."),
("What defines a Python code block?", ["Indentation","Capital letters","Semicolons only","Comments"],"Indentation","Indentation shows which statements belong to a block."),
("If age=20 and age>=18, is Adult printed?", ["Yes","No","20 only","Nothing"],"Yes","20 is at least 18."),
("Condition for x from 1 through 10 inclusive?", ["1 <= x <= 10","1 < x < 10 only","x=1..10","x>=1 or x<=10"],"1 <= x <= 10","Chained comparison includes both endpoints."),
("Output of 'A' if 2>3 else 'B'?", ["A","B","2","Error"],"B","The condition is false."),
("Which operator means logical OR?", ["||","or","|>","either"],"or","Python uses the keyword or."),
("If 0: print('yes') else: print('no'), output?", ["yes","no","0","Error"],"no","Zero is falsy."),
("For passing score >=50, which condition is right?", ["score > 50","score >= 50","score < 50","score == 100"],"score >= 50","The rule includes a score of exactly 50."),
("If x=7, if x<5 A; elif x<10 B; else C, which prints?", ["A","B","C","Nothing"],"B","7 is less than 10 but not less than 5."),
],
"Loops": [
("Which loop iterates over a sequence?", ["if","for","def","return"],"for","for iterates over an iterable."),
("What values does range(3) produce?", ["1,2,3","0,1,2","0,1,2,3","3 only"],"0,1,2","range stops before its endpoint."),
("Output of for i in range(2): print(i)?", ["1 then 2","0 then 1","0 then 1 then 2","2 only"],"0 then 1","range(2) yields 0 and 1."),
("Which loop repeats while a condition is true?", ["while","if","class","try"],"while","while repeats while its condition remains true."),
("What does break do?", ["Exits nearest loop","Skips one iteration","Restarts program","Defines function"],"Exits nearest loop","break terminates the nearest enclosing loop."),
("What does continue do?", ["Ends program","Skips to next iteration","Exits loop permanently","Returns a value"],"Skips to next iteration","continue skips the rest of the current iteration."),
("Sum of values in [1,2,3]?", ["3","5","6","123"],"6","1 + 2 + 3 equals 6."),
("What if a while condition stays true and x never changes?", ["Possible infinite loop","Syntax error always","print changes x","No issue"],"Possible infinite loop","The condition may never become false."),
("How many iterations in range(4)?", ["3","4","5","1"],"4","range(4) yields 0, 1, 2, and 3."),
("Output of list(range(2,5))?", ["[2, 3, 4]","[2, 3, 4, 5]","[1, 2, 3, 4]","[5]"],"[2, 3, 4]","The stop value 5 is excluded."),
("Best direct loop over a list?", ["for item in items","while True only","if item","def item"],"for item in items","for visits each item in the list."),
("Output of range(1,4) printed with spaces?", ["0 1 2","1 2 3","1 2 3 4","4"],"1 2 3","The start is included and stop is excluded."),
("Why update a while-loop counter?", ["Help condition eventually become false","Make print optional","Create class","Import module"],"Help condition eventually become false","Updating state can prevent infinite loops."),
("Output of for ch in 'hi': print(ch, end='')?", ["hi","h i","'hi'","Error"],"hi","The characters are printed without a separator."),
("Find the syntax error: for i in range(3) print(i)", ["Missing colon","range needs four arguments","i must be a string","No error"],"Missing colon","A for header ends with a colon."),
],
"Functions": [
("Which keyword defines a function?", ["func","function","def","class"],"def","def defines a function."),
("Which statement sends a result back?", ["print","return","input","break"],"return","return sends a value to the caller."),
("What is add(2,3) if add returns a+b?", ["23","5","add","None"],"5","The function returns 2 + 3."),
("What is a parameter?", ["Name in definition receiving a value","Printed result only","Keyword","Loop"],"Name in definition receiving a value","Parameters are named in the function header."),
("What is an argument?", ["Value passed to a function call","Function name only","Comment","return keyword"],"Value passed to a function call","Arguments supply values to parameters."),
("What happens when greet() prints 'Hi' and is called?", ["Hi","greet","None only","Error"],"Hi","Calling the function executes its body."),
("What does a function return without return?", ["0","False","None","Empty string"],"None","Python functions return None by default."),
("Find the syntax error: def greet() print('Hi')", ["Missing colon","Names must be uppercase","print is invalid","No error"],"Missing colon","The function header needs a colon."),
("If double(x) returns x*2, double(4) is?", ["4","6","8","44"],"8","Four multiplied by two is eight."),
("Which is a keyword argument call?", ["greet('Sam')","power(base=2, exponent=3)","print()","len([1])"],"power(base=2, exponent=3)","Keyword arguments specify parameter names."),
("What is recursion?", ["Function calling itself","Loop with no condition","Assignment","Import"],"Function calling itself","Recursive functions call themselves."),
("Why does recursion need a base case?", ["To stop recursive calls","Make values global","Create a list","Print each line"],"To stop recursive calls","The base case prevents endless recursion."),
("If def f(x=3): return x, what does f() return?", ["0","3","None","Error"],"3","The default value is used."),
("What is a local variable?", ["Variable defined within a function scope","Internet variable","Keyword","List item"],"Variable defined within a function scope","Local variables are available within their scope."),
("If f() returns 2, what is f()+1?", ["2","3","21","None"],"3","The returned number 2 plus 1 equals 3."),
],
"Lists": [
("Which syntax creates a list?", ["(1, 2)","[1, 2]","{'a': 1}","1, 2 only"],"[1, 2]","Square brackets create a list."),
("Output of [4,5,6][0]?", ["4","5","6","0"],"4","List indexes start at zero."),
("Output of len([2,4,6])?", ["2","3","6","12"],"3","There are three elements."),
("Which method adds an item at the end?", ["append()","add_end()","push_back()","insert_end_only()"],"append()","append adds one item at the end."),
("After a=[1,2]; a.append(3), what is a?", ["[1,2]","[1,2,3]","[3,1,2]","3"],"[1,2,3]","append adds 3 to the end."),
("Output of [10,20,30][-1]?", ["10","20","30","Error"],"30","Index -1 refers to the last item."),
("What is [0,1,2,3][1:3]?", ["[0,1,2]","[1,2]","[1,2,3]","[2,3]"],"[1,2]","Slice end index is excluded."),
("Which method removes and returns the last item by default?", ["pop()","clear()","sort()","copy()"],"pop()","pop() removes and returns the final item."),
("What does list.sort() return?", ["Sorted list","None","Original length","Error"],"None","sort changes the list in place and returns None."),
("What error for [1,2][2]?", ["IndexError","KeyError","NameError","No error"],"IndexError","Index 2 is outside the two-item list."),
("Output of [1,2] + [3]?", ["[1,2,3]","[1,2,[3]]","6","Error"],"[1,2,3]","List addition concatenates the lists."),
("How do you test if 5 is in nums?", ["5 inside nums","5 in nums","nums has 5","contains(nums,5)"],"5 in nums","in checks membership."),
("After nums=[1,2,3]; nums[1]=9, what is nums?", ["[1,2,3]","[1,9,3]","[9,2,3]","Error"],"[1,9,3]","Lists are mutable and can be changed by index."),
("What does nums.clear() do?", ["Removes all items","Sorts list","Copies list","Removes only last item"],"Removes all items","clear empties the list."),
("Output of list(range(3))?", ["[1,2,3]","[0,1,2]","(0,1,2)","{0,1,2}"],"[0,1,2]","list converts the range to a list."),
],
"Dictionaries": [
("What does a dictionary store?", ["Sequence only","Key-value pairs","Numbers only","Function body"],"Key-value pairs","Dictionaries map keys to values."),
("Which creates a dictionary?", ["[1,2]","(1,2)","{'name':'Ana'}","{1,2}"],"{'name':'Ana'}","A colon separates key and value."),
("Output of {'x':4}['x']?", ["x","4","{'x':4}","Error"],"4","Key x maps to 4."),
("Which method safely retrieves a missing key with a default?", ["get()","append()","push()","index()"],"get()","get can return a supplied default."),
("Output of {'a':1}.get('b',0)?", ["None","0","1","KeyError"],"0","The default is returned for a missing key."),
("How do you set key age to 20?", ["d['age']=20","d.add('age',20)","d.append('age',20)","d[20]='age' only"],"d['age']=20","Assignment adds or updates a key."),
("What does 'name' in d check?", ["Whether name is a key","Whether name is a value only","Whether d is empty","Whether d is a list"],"Whether name is a key","Dictionary membership tests keys."),
("Output of len({'a':1,'b':2})?", ["1","2","3","4"],"2","There are two key-value pairs."),
("Which method provides dictionary keys?", ["keys()","items_only()","values_key()","index()"],"keys()","keys returns a view of keys."),
("After d={'n':1}; d['n']=5, d['n'] is?", ["1","5","6","Error"],"5","The assignment updates the existing value."),
("What error for d={'a':1}; print(d['b'])?", ["KeyError","IndexError","TypeError","No error"],"KeyError","Key b does not exist."),
("What does d.items() provide?", ["Key-value pairs","Only keys","Only values","Sorted dictionary"],"Key-value pairs","items returns key-value pairs."),
("Can a list be a dictionary key?", ["Yes always","No, lists are unhashable","Only if empty","Only for integers"],"No, lists are unhashable","Dictionary keys must be hashable."),
("Output of 'x' in {'x':2}?", ["True","False","2","Error"],"True","x is a key."),
("What does d.pop('x') do if x exists?", ["Removes x and returns its value","Sorts dictionary","Returns key count","Copies dictionary"],"Removes x and returns its value","pop removes the key and returns its value."),
],
"Classes and Objects": [
("What is a class?", ["Loop","Blueprint for objects","Variable","Print statement"],"Blueprint for objects","Classes define attributes and behavior."),
("Which method commonly initializes an object?", ["start()","__init__()","main()","create()"],"__init__()","__init__ is called during normal instance creation."),
("What does self refer to?", ["Current instance","Parent only","Global variable","Interpreter"],"Current instance","self refers to the instance receiving the method call."),
("How is an instance usually created?", ["Dog()","new Dog","class Dog","make Dog()"],"Dog()","Calling the class creates an instance."),
("What is an attribute?", ["Data associated with an object","Loop","Syntax error","Import"],"Data associated with an object","Attributes store object data or behavior references."),
("What is type(A()).__name__ if class A: pass?", ["A","obj","class","None"],"A","The instance type is A."),
("Where is an instance attribute commonly initialized?", ["In __init__ with self","After program ends","In comment","In import"],"In __init__ with self","For example, self.name = name."),
("What is wrong if a method is not indented inside its class?", ["The method is outside the class body","Class names must be lowercase","Methods cannot print","Nothing"],"The method is outside the class body","Class members must be indented."),
("If __init__ sets self.size=3, what is obj.size?", ["size","3","Box","None"],"3","The attribute stores the value 3."),
("What is a method?", ["Function defined in a class","Dictionary key","Comment","File extension"],"Function defined in a class","Methods define behavior for objects/classes."),
("What is a class attribute?", ["Value defined in class body","Always local variable","Argument only","List index"],"Value defined in class body","Class attributes are associated with the class."),
("If class A has x=7, what is A.x?", ["A","x","7","None"],"7","x is a class attribute."),
("Why are objects useful?", ["Bundle state and behavior","Remove every variable","Make Python case-insensitive","Prevent every bug"],"Bundle state and behavior","Objects group data and methods."),
("What does obj.method() do?", ["Calls a method on obj","Creates keyword","Deletes obj","Imports from internet"],"Calls a method on obj","Dot notation accesses and calls a method."),
("What does pass do in an empty class?", ["Acts as a placeholder","Creates object automatically","Prints class name","Raises exception"],"Acts as a placeholder","pass satisfies Python's need for a block."),
],
"Encapsulation": [
("What does encapsulation do?", ["Repeats code","Groups data and methods in a class","Creates loop","Imports module"],"Groups data and methods in a class","Encapsulation bundles related data and behavior."),
("What does a leading underscore in _balance signal?", ["Intended non-public detail by convention","Invalid name","Encryption","A loop"],"Intended non-public detail by convention","A single underscore is a convention."),
("What does __balance in a class trigger?", ["Name mangling","Encryption","File saving","Looping"],"Name mangling","Double-leading underscores trigger name mangling."),
("Why use a method to update balance?", ["Validate changes in one place","Convert to text automatically","Disable methods","Skip objects"],"Validate changes in one place","Methods can enforce rules before changing state."),
("What are properties useful for?", ["Controlled attribute access","Creating loops","Importing modules","Replacing classes"],"Controlled attribute access","Properties allow attribute-style access with getter/setter logic."),
("What does @property do?", ["Defines a managed attribute accessor","Creates child class","Prints value","Catches errors"],"Defines a managed attribute accessor","A property method can be accessed like an attribute."),
("Can a single-underscore attribute be accessed externally?", ["Never","Yes, it is a convention","Only Windows","Only strings"],"Yes, it is a convention","Python does not enforce privacy for a single underscore."),
("Best description of encapsulation?", ["Hide implementation behind a clear interface","Put every statement in one function","Use global variables only","Avoid methods"],"Hide implementation behind a clear interface","Encapsulation controls how object state is used."),
("What design issue arises if all code changes balance directly?", ["State changes are not controlled centrally","Classes cannot store numbers","Methods cannot take values","Python forbids attributes"],"State changes are not controlled centrally","A method can validate changes consistently."),
("If set_x(9) assigns self.x=9, what is c.x?", ["9","value","x","None"],"9","The method stores 9 on the instance."),
("Best way to protect a bank balance?", ["Validate deposits and withdrawals in methods","Let every caller set any balance","Store it in a comment","Use print"],"Validate deposits and withdrawals in methods","Methods can reject invalid changes."),
("Difference between _x and __x in a class?", ["Double underscore triggers name mangling","They are always identical","Single underscore encrypts","Double underscore makes it global"],"Double underscore triggers name mangling","Name mangling helps avoid accidental name clashes."),
("Why hide internal details behind methods?", ["Implementation can change while interface remains stable","Makes code impossible to test","Guarantees zero bugs","Removes documentation"],"Implementation can change while interface remains stable","A stable interface reduces coupling."),
("What does encapsulation help reduce?", ["Uncontrolled access to internal state","Python keywords","Integer size","Need for objects"],"Uncontrolled access to internal state","Controlled interfaces reduce accidental misuse."),
("Is Python encapsulation strict private access like some languages?", ["Yes always","No, it mostly uses conventions and name mangling","Only for integers","Only in functions"],"No, it mostly uses conventions and name mangling","Python does not generally enforce strict private access."),
],
"Inheritance": [
("What is inheritance?", ["Reuse and extend class behavior","Repeat loops","Data type","Print statement"],"Reuse and extend class behavior","A child class can inherit parent behavior."),
("How does Dog inherit Animal?", ["class Dog(Animal):","class Dog inherits Animal:","Dog -> Animal","class Dog = Animal"],"class Dog(Animal):","The base class goes in parentheses."),
("What is a parent class also called?", ["Base class","Loop class","Input class","Local class"],"Base class","Base class is another name for parent class."),
("What is a child class also called?", ["Derived class","Comment class","Primitive class","Input class"],"Derived class","A derived class inherits from another class."),
("What does super() help with?", ["Access parent-class behavior","Stop Python","Create loop","Convert text"],"Access parent-class behavior","super provides access to methods in the parent lookup order."),
("If B(A) has no speak method, where can it find speak?", ["In A if A defines it","Nowhere always","Only builtins","Random module"],"In A if A defines it","B can inherit methods from A."),
("If B inherits A's hi method, what can B().hi() return?", ["Hi","B","None always","Error always"],"Hi","The child inherits the parent's method."),
("Why override a method?", ["Specialize behavior in a subclass","Delete parent classes","Change syntax","Prevent objects"],"Specialize behavior in a subclass","A subclass can replace an inherited implementation."),
("Find the syntax error: class Child Parent:", ["Missing parentheses around Parent","Parent must be lowercase","Classes cannot inherit","No error"],"Missing parentheses around Parent","Use class Child(Parent):."),
("Can a child class add its own methods?", ["Yes","No","Only without a parent","Only in comments"],"Yes","Subclasses can define extra behavior."),
("If B(A) defines x=5 and A defines x=2, what is B.x?", ["2","5","7","Error"],"5","B's own class attribute takes precedence."),
("What is multiple inheritance?", ["Inheriting from more than one base class","Many objects from one class","Loop runs many times","Method returns list"],"Inheriting from more than one base class","Python allows multiple base classes."),
("What does MRO determine?", ["Order Python searches classes for methods/attributes","File save order","Loop speed","Number of arguments"],"Order Python searches classes for methods/attributes","Method resolution order defines attribute lookup."),
("One benefit of inheritance?", ["Reuse common behavior","Eliminate all testing","Make all attributes private","Avoid all functions"],"Reuse common behavior","Common behavior can be implemented in a base class."),
("When may composition be better?", ["When an object contains/uses another without being its subtype","Whenever variable is integer","Only when printing","Never"],"When an object contains/uses another without being its subtype","Composition models a has-a relationship."),
],
"Polymorphism": [
("What does polymorphism allow?", ["Different objects share an interface","Only one class","Only integers","Automatic file saving"],"Different objects share an interface","Different objects can respond differently to the same method call."),
("What is method overriding?", ["Subclass provides its own inherited-method implementation","Calling twice","Renaming variable","Adding comment"],"Subclass provides its own inherited-method implementation","Overriding customizes inherited behavior."),
("If Cat.speak returns meow and Dog.speak returns woof, what can a loop do?", ["Call each object's matching behavior","Always return meow","Always error","Convert pets to strings"],"Call each object's matching behavior","The object's implementation runs."),
("What is duck typing based on?", ["Supported behavior rather than declared type","Object color","Variable name only","Database"],"Supported behavior rather than declared type","Python often focuses on available operations."),
("If A.f returns 1 and B.f returns 2, what is [o.f() for o in (A(),B())]?", ["[1, 2]","[1, 1]","[2, 2]","Error"],"[1, 2]","Each object calls its own f method."),
("Which demonstrates polymorphism?", ["Different shapes implement area()","Only one function accepts integers","Classes have unrelated names","Convert all objects to text"],"Different shapes implement area()","A shared method can have class-specific implementations."),
("Why use a shared method name?", ["Calling code can handle different object types","Guarantees same result","Prevents subclasses","Removes arguments"],"Calling code can handle different object types","The caller uses a common operation."),
("What if obj.draw() is called but obj has no draw method?", ["The object does not meet expected interface","Methods must be static","draw must be uppercase","No issue"],"The object does not meet expected interface","The expected method is missing."),
("Must polymorphic implementations return the same value?", ["Yes always","No, behavior may differ","Only strings","Only with inheritance"],"No, behavior may differ","Polymorphism permits different behavior through a common operation."),
("What do len('cat') and len([1,2,3]) return?", ["3 and 3","3 and 2","cat and 3","Error"],"3 and 3","len works on strings and lists."),
("Which is operator polymorphism?", ["+ adds numbers and joins strings","if checks only strings","def defines a class","input returns int"],"+ adds numbers and joins strings","The same operator behaves according to operand types."),
("What does overriding enable?", ["Specialized subclass behavior","Infinite memory","Disable calls","Convert lists to tuples"],"Specialized subclass behavior","A subclass can customize an inherited method."),
("Why use render() across different classes?", ["Client code can call render on varied object types","Every render must do same thing","render is a keyword","Avoid objects"],"Client code can call render on varied object types","A shared interface simplifies client code."),
("What object can fit a function expecting .read()?", ["Any object with a compatible .read() method","Only object named File","Only string","Only integer"],"Any object with a compatible .read() method","Duck typing focuses on supported behavior."),
("Best description of polymorphism?", ["One operation can have different implementations","Every object has identical data","Only applies to loops","Forbids overriding"],"One operation can have different implementations","A common operation can behave differently by type."),
],
"Abstraction": [
("Which module supports abstract classes?", ["math","random","abc","os"],"abc","abc provides abstract base class tools."),
("What is abstraction?", ["Expose essential behavior, hide implementation details","Write every detail twice","Use only numbers","Avoid functions"],"Expose essential behavior, hide implementation details","Abstraction focuses on what something does."),
("Which decorator marks an abstract method?", ["@property","@abstractmethod","@classmethodonly","@hidden"],"@abstractmethod","abstractmethod marks methods subclasses must implement."),
("What can an abstract base class define?", ["Required interface for subclasses","Loop counter","File extension","Global variable"],"Required interface for subclasses","Subclasses are expected to implement abstract methods."),
("Can a class with unimplemented abstract methods normally be instantiated?", ["Yes always","No","Only with print","Only from a list"],"No","Python prevents normal instantiation of abstract classes."),
("How do you import abstractmethod?", ["from abc import abstractmethod","import abstractmethod from python","from math import abstractmethod","import class"],"from abc import abstractmethod","abstractmethod is in the abc module."),
("What runs when a concrete object calls an implemented abstract method?", ["Concrete implementation","Always None","Always error","Source code"],"Concrete implementation","The subclass supplies the actual method body."),
("Benefit of abstraction?", ["Clear interface without exposing every detail","Removes all code","Makes every method private","Guarantees no bugs"],"Clear interface without exposing every detail","Callers need not understand implementation internals."),
("A subclass omits a required abstract method. What happens?", ["It remains abstract and cannot normally be instantiated","Python fills it automatically","Parent disappears","Object becomes list"],"It remains abstract and cannot normally be instantiated","Unimplemented abstract methods prevent instantiation."),
("An abstract method usually describes what?", ["Behavior subclasses must provide","Completed loop","Global constant","File path"],"Behavior subclasses must provide","It defines part of the required interface."),
("Useful abstraction for payment types?", ["Common pay() interface","Unrelated variable names","One hard-coded payment","Comment containing price"],"Common pay() interface","Payment implementations can share a common operation."),
("Is abstraction the same as making every variable private?", ["Yes","No, it is about interfaces and details","Only Python 2","Only strings"],"No, it is about interfaces and details","Privacy conventions and abstraction are different concepts."),
("Role of a concrete subclass?", ["Implement required abstract behavior","Delete base class","Turn methods into comments","Prevent inheritance"],"Implement required abstract behavior","Concrete subclasses implement required methods."),
("Why is an interface useful?", ["Callers need not depend on internal implementation","It reveals every detail","All methods internally identical","Prevents testing"],"Callers need not depend on internal implementation","Callers can rely on a stable contract."),
("Which statement about abstract base classes is true?", ["Use ABC and abstractmethod from abc","Must be named Abstract","Cannot contain concrete methods","Created by input()"],"Use ABC and abstractmethod from abc","Python's abc module supports abstract base classes."),
],
"Exception Handling": [
("Which keyword begins exception handling?", ["try","catch","error","excepting"],"try","try wraps code that may raise an exception."),
("Which block handles an exception?", ["except","finally","elseif","repeat"],"except","except handles matching exceptions."),
("What can int('hello') raise?", ["ValueError","IndexError","KeyError","NameError"],"ValueError","The text is not a valid integer."),
("What does finally do?", ["Runs during normal cleanup flow whether error occurs or not","Runs only without errors","Defines function","Repeats loop"],"Runs during normal cleanup flow whether error occurs or not","finally is often used for cleanup."),
("What prints when ZeroDivisionError is caught and handler prints Oops?", ["Oops","0","1","Nothing"],"Oops","The handler runs after division by zero."),
("Which exception means list index is out of range?", ["IndexError","KeyError","ValueError","ImportError"],"IndexError","The requested sequence index is invalid."),
("Which exception can occur for a missing dictionary key?", ["KeyError","IndexError","ZeroDivisionError","SyntaxError"],"KeyError","Direct lookup of an absent key raises KeyError."),
("Find the issue: try: print('hi') with no except/finally", ["try needs except or finally","print cannot be inside try","quotes invalid","No error"],"try needs except or finally","A try statement must include except or finally."),
("Why catch specific exceptions?", ["Avoid hiding unrelated errors","Make all code faster","Prevent all exceptions","Remove testing"],"Avoid hiding unrelated errors","Specific handlers make problems clearer."),
("What does raise do?", ["Raises an exception","Catches every exception","Restarts computer","Creates class automatically"],"Raises an exception","raise signals an exception deliberately."),
("What order is printed by try print('A') finally print('B')?", ["A then B","B then A","Only A","Only B"],"A then B","finally runs after the try block."),
("Which exception can occur for an undefined name?", ["NameError","TypeError","OSError","StopIteration"],"NameError","Python cannot find the referenced name."),
("When does try/except else run?", ["else runs if try raised no exception","else runs only on error","before try","replaces finally"],"else runs if try raised no exception","The else block follows a successful try."),
("What exception can occur when opening a missing file for reading?", ["FileNotFoundError","IndexError","SyntaxError","ZeroDivisionError"],"FileNotFoundError","The file path cannot be found."),
("Why avoid bare except everywhere?", ["It can hide unexpected problems","Required for every program","Only catches syntax errors","Makes errors impossible"],"It can hide unexpected problems","Handle expected exceptions specifically."),
],
"File Handling": [
("Which function opens a file?", ["open()","file()","readfile()","load()"],"open()","open returns a file object."),
("Which mode reads a file?", ["'r'","'w'","'a'","'x'"],"'r'","r mode is for reading."),
("Which mode overwrites or creates a file?", ["'r'","'w'","'a'","'read'"],"'w'","w mode truncates an existing file."),
("Which mode appends content?", ["'r'","'w'","'a'","'x'"],"'a'","Append mode writes at the end."),
("What does file.read() do?", ["Reads file content","Deletes file","Renames file","Closes file"],"Reads file content","read returns file data."),
("Why use with open(...) as file?", ["Closes file automatically when block exits","Makes file read-only","Deletes file","Prevents all errors"],"Closes file automatically when block exits","with manages the file resource."),
("Which method reads one line?", ["readline()","append()","writeline_only()","closeall()"],"readline()","readline reads a line."),
("Which method writes text?", ["write()","printfile()","input()","appendline()"],"write()","write writes a string to the file."),
("Opening a missing file with 'r' may raise?", ["FileNotFoundError","IndexError","NameError always","No error"],"FileNotFoundError","The requested path does not exist."),
("What does file.close() do?", ["Closes file object","Deletes content","Reads first line","Renames file"],"Closes file object","Closing releases the resource."),
("Does f.write('Hi') automatically print Hi on screen?", ["Yes","No, it writes to the file","It deletes the file","It always raises an error"],"No, it writes to the file","write writes to the file, not the terminal."),
("Which mode fails if a file already exists and creates exclusively?", ["'x'","'r'","'w'","'a'"],"'x'","Exclusive creation mode errors if the path exists."),
("After reading the whole file once, what does read() usually return on a second call?", ["Empty string","Same content forever","Filename","File object list"],"Empty string","The file cursor is already at the end."),
("Why might a relative path not be found?", ["It is resolved from current working directory","Python cannot read text","Needs web connection","Must contain drive letter"],"It is resolved from current working directory","Relative paths depend on the working directory."),
("Which exception can indicate file access permission is denied?", ["PermissionError","SyntaxError","StopIteration","ZeroDivisionError"],"PermissionError","The operating system can deny access."),
],
}

# The first seven and OOP/error-handling topics are defined above.
# Operators, conditions, loops, functions, lists and dictionaries have their
# own dedicated banks above as well; this list ensures the complete curriculum.

# Convert each question's data tuple into a Question object.
# app.py expects question.prompt, question.options, and other attributes.
for topic, question_rows in BANK.items():
    BANK[topic] = [
        row if isinstance(row, Question) else q(*row)
        for row in question_rows
    ]

ALIASES = {
    "Intro": "Introduction",
    "Python Introduction": "Introduction",
    "Introduction to Python": "Introduction",
    "Classes/Objects": "Classes and Objects",
    "Class and Objects": "Classes and Objects",
}

QUIZZES = {topic: Quiz(f"{topic} Quiz", questions) for topic, questions in BANK.items() if questions}
for alias, original in ALIASES.items():
    QUIZZES[alias] = QUIZZES[original]
