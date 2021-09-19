import random

nQuiz = 10
data = []

f = open(file="out.txt", mode='w')

for i in range(nQuiz):
    
    # make quiz
    first = random.choice(range(1, 100000))
    second = random.choice(range(1, 100000))
    operator = random.choice(["+", "-", "*", "/", "%"])

    print(first, operator, second, sep=" ")

    # get python's answer
    pyAns = 0
    if operator == "+":
        pyAns = first + second
    if operator == "-":
        pyAns = first - second
    if operator == "*":
        pyAns = first * second
    if operator == "/":
        pyAns = first / second
    if operator == "%":
        pyAns = first % second

    # get c++'s answer
    cppAns = input()

    # compare with table
    data.append([first, operator, second, pyAns, cppAns])

for i in range(nQuiz):
    first, operator, second, pyAns, cppAns = data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]
    print(str(first)+" "+operator+" "+str(second)+" = (python: "+str(pyAns)+", cpp: "+cppAns+")")
    print(str(first)+" "+operator+" "+str(second)+" = (python: "+str(pyAns)+", cpp: "+cppAns+")", file=f)