# How to run:
# python3 calculator.py
from decimal import Decimal

def readNumber(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1

    # Consider the case that the index points to the the last element.
    if index >= len(line):
        token = {'type': 'NUMBER', 'number': int(number)}
        index += 1
        return token, index

    # Consider a float number.
    if line[index] == '.':
        count = 1
        index += 1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * ( 10 ** ( - count) )
            index += 1
            count += 1
        # Set it as string type if to set it as decimal below.
        number = str(number) 
        token = {'type': 'NUMBER', 'number': float(number)} # Replace float() with Decimal() if needed.
    else:
        token = {'type': 'NUMBER', 'number': int(number)}
    #print(token)
    return token, index

def readPlus(index):
    token = {'type': 'PLUS'}
    return token, index + 1

def readMinus(index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readAsterisk(index):
    token = {'type': 'MULTIPLY'}
    return token, index + 1

def readSlash(index):
    token = {'type': 'DIVIDE'}
    return token, index + 1

def readBracket(line, index):
    if line[index] == '(':
        token = {'type': 'LEFT_BRACKET'}
    else:
        token = {'type': 'RIGHT_BRACKET'}
    return token, index + 1

def addAndSubstructNumber(answer, tokens, index):
    if tokens[index - 1]['type'] == 'PLUS':
        answer += tokens[index]['number']
    elif tokens[index - 1]['type'] == 'MINUS':
        answer -= tokens[index]['number']
    else:
        print('Invalid syntax')
    #print(answer)
    return answer, index + 1

def multiplyPrevAndNext(index, tokens):
    prev = tokens[index - 1]['number']
    next = tokens[index + 1]['number']
    number = prev * next
    if isinstance(number, int):
        token = {'type': 'INTEGER', 'number': int(number)}
    else:
        token = {'type': 'FLOAT', 'number': float(number)}
    tokens[index] = token
    del tokens[index - 1]
    del tokens[index]

    return tokens, index + 1

def dividePrevIntoNext(index, tokens):
    prev = tokens[index - 1]['number']
    next = tokens[index + 1]['number']
    number = prev / next

    if isinstance(number, int):
        token = {'type': 'NUMBER', 'number': int(number)}
    else:
        token = {'type': 'NUMBER', 'number': float(number)}
    tokens[index] = token
    del tokens[index - 1]
    del tokens[index]

    return tokens, index + 1

def tokenize(line):
    # Tokenize every operand and operator.
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit(): 
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(index)
        elif line[index] == '-':
            (token, index) = readMinus(index)
        elif line[index] == '*':
            (token, index) = readAsterisk(index)
        elif line[index] == '/':
            (token, index) = readSlash(index)
        elif line[index] == '(' or line[index] == ')':
            (token, index) = readBracket(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)

    return tokens

def evaluateMuiltiplicationAndDivision(tokens):
    # Calculate * and /.
    index = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    while index < len(tokens):
        if tokens[index]['type'] == 'MULTIPLY':
            tokens, index = multiplyPrevAndNext(index, tokens)
        elif tokens[index]['type'] == 'DIVIDE':
            tokens, index = dividePrevIntoNext(index, tokens)
        else:
            index += 1

    return tokens

def evaluateAdditionAndSubstruction(tokens):
    # Calculate + and -. 
    answer = 0
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            answer, index = addAndSubstructNumber(answer, tokens, index)
        else:
            index += 1
    return answer

def evaluate(tokens):
    tokens = evaluateMuiltiplicationAndDivision(tokens)
    if len(tokens) == 2:
        answer = tokens[1]['number']
        return answer
    answer = evaluateAdditionAndSubstruction(tokens)

# test
# python3 calculator.py

def test(line):
    line = line.replace(' ', '') # eliminate blank
    tokens = tokenize(line)
    tokens = evaluateMuiltiplicationAndDivision(tokens)
    actual_answer = evaluateAdditionAndSubstruction(tokens)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))

def run_test():
  print("==== Test started! ====")
  # My intention is ...
    # Try the three cases: 
    # 1 digit number, operator, 1 digit number
    # 2 digits number, operator, 1 digit number
    # 1 digit number, operator, 2 digit number
    # Try big digit number 
  test("1+1")
  test("1.5+1")
  test("1+1.5")
  test("1.5+1.5")
  test("20+1")
  test("1+20")
  test("55+55")
  test("30.5+1")
  test("1+30.5")
  test("15.5+15.5")
  test("12.2233+126.99980")
  test("1-1")
  test("10-1")
  test("1-10")
  test("1.5-1")
  test("1-1.5")
  test("5.59-12.4")
  test("12.22288-1999.48")
  test("2*2")
  test("2*44")
  test("44*2")
  test("12.5*3")
  test("45.2*2.3")
  test("6/3")
  test("3/9")
  test("52.2/3")
  test("89.7/20.1")
  test("1531/1237")
  # edge cases 
  test("1 + 10") # should return 11
  test("2++1") # should return "Invalid character found: "
  test("100 -- 5") # should return "Invalid character found: "
  print("==== Test finished! ====\n")

line = input()
tokens = tokenize(line)
answer = evaluate(tokens)
print(answer)

run_test()