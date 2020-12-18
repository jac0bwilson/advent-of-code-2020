def evaluate(expression, question):
    parsed = []

    for part in expression.split(' '):
        if part.isnumeric():
            parsed.append(int(part))
        else:
            parsed.append(part)

    if question == 1:
        while len(parsed) >= 3:
            num = parsed[0]
            op = parsed[1]
            num2 = parsed[2]
            result = 0
            
            if op == '+':
                result = num + num2
            elif op == '*':
                result = num * num2
            
            parsed = [result] + parsed[3:] if len(parsed) > 3 else [result]

        return parsed[0]
    
    elif question == 2:
        for char in ['+', '*']:
            while char in parsed:
                location = parsed.index(char)
                num = parsed[location - 1]
                num2 = parsed[location + 1]
                result = 0

                if char == '+':
                    result = num + num2
                else:
                    result = num * num2
                parsed = parsed[:location - 1] + [result] + parsed[location + 2:]        
        
        return parsed[0]

def resolveBrackets(expression, part):
    openPairs, start, end = 0, None, None

    for i in range(len(expression)):
        if expression[i] == '(':
            if openPairs == 0:
                start = i

            openPairs += 1
        elif expression[i] == ')':
            openPairs -= 1
            
            if openPairs == 0:
                end = i

    if start != None and end != None:
        subexp = expression[start + 1:end]

        beforeBracket = expression[:start]
        afterBracket = expression[end + 1:]
        
        return str(resolveBrackets(beforeBracket + str(resolveBrackets(subexp, part)) + afterBracket, part))
    else:
        return evaluate(expression, part)

def solve(expressions, part):
    results = []

    for expression in expressions:
        while '(' in expression:
            expression = resolveBrackets(expression, part)

        results.append(evaluate(expression, part))

    print(sum(results))

expressions = [line.strip() for line in open('day18/input.txt', 'r')]
solve(expressions, 1)
solve(expressions, 2)