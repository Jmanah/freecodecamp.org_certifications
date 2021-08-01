# turn a list of arythmatic problems into an array containing each problem as its own list     
def analyse(problems, solve = False):
    i = 0
    for problem in problems:
        problems[i] = problem.split(" ")
        i += 1
    # print (problems)
    
    # do the math or not
    if solve == True:
        for problem in problems:
            if problem[1] == "+":
                problem.append(str(int(problem[0]) + int(problem[2])))
            elif problem[1] == "-":
                problem.append(str(int(problem[0]) - int(problem[2])))
    else:
        for problem in problems:
            problem.append("")

# Formating logic
    for problem in problems:
        if len((problem[0])) >= (len(problem[2])):
            problem.append(len(problem[0])+2)
        elif len((problem[0])) < (len(problem[2])):
            problem.append(len(problem[2])+2)
    return problems


def arithmetic_arranger (problems, solve = False):
    ops = ["-","+"]
    problems = analyse(problems, solve)
    line1 = []
    line2 = []
    line3 = []
    line4 = []
    
    if len(problems)>5:
        return "Error: Too many problems." 
    
# generates line 1
    for problem in problems:
        if problem[0].isnumeric() == False:
            return "Error: Numbers must only contain digits."
        if len(problem[0]) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:
            print (problem)
            line1.append(problem[0].rjust((problem[4])))
            line1.append("    ")
    del line1[-1]
    line1.append("\n")

# generates line 2
    for problem in problems:
        if problem[1] not in ops:
            return "Error: Operator must be '+' or '-'."
        if problem[2].isnumeric() == False:
            return "Error: Numbers must only contain digits."
        if len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:
            line2.append(problem[1] + problem[2].rjust(problem[4] -1))
            line2.append("    ")
    del line2[-1]
    line2.append("\n")

# generates line 3
    for problem in problems:
        line3.append("".rjust((problem[4]), "-"))
        line3.append("    ")
    del line3[-1]

    if solve == False:
        print ("".join(line1) + "".join(line2) + "".join(line3))
        return "".join(line1) + "".join(line2) + "".join(line3)

    elif solve == True:
        line3.append("\n")

# generates line 4 if nessisary 
        for problem in problems:
            line4.append(problem[3].rjust((problem[4])))
            line4.append("    ")
        del line4[-1]

        print ("".join(line1) + "".join(line2) + "".join(line3) + "".join(line4))
        return "".join(line1) + "".join(line2) + "".join(line3) + "".join(line4)