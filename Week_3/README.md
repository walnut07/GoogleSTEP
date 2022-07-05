# **The program description of calculator.py** 

## Summary 
This program can add, substruct, multiply, and divide either integer or float numbers. 

## How it works
This program can broadly be devided into two parts: `tokenize` and `evaluate`.

### `tokenize(line)`:
It tokenizes every operand and operator in input `line`.
It traverses `line` and generates a `token`. Finally returns `tokens` that has all the `token`s.

```python
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
    else:
        print('Invalid character found: ' + line[index])
        exit(1)
    tokens.append(token)
return tokens
```
`readNumber`, `readMinus`, `readPlus`, `readAsterisk`, and `readSlash` return a `token` and a new `index`.

The `token` of an integer 1 looks like this.

```
 {'type': 'INTEGER', 'number': 1}
```

The `tokens` of `1+1` looks like this.
```
 [{'type': 'INTEGER', 'number': 1},  {'type': 'PLUS'}, {'type': 'INTEGER', 'number': 1}
```

### `evaluate(line)`:
It returns the answer after calculating all the numbers. <br>
In the first while loop, it traverses `tokens` and does only multiplication and division. 

```python
# Calculate * and /.
index = 0
tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
while index < len(tokens):
    if tokens[index]['type'] == 'MULTIPLY':
        tokens, index = multiplyPrevAndNext(line, index, tokens)
    elif tokens[index]['type'] == 'DIVIDE':
        tokens, index = dividePrevIntoNext(line, index, tokens)
    else:
        index += 1
if len(tokens) == 2:
    answer = tokens[1]['number']
    return answer
```

`multiplyPrevAndNext` multiplies the previous and next number of the asterisk `*` mark and returns a new `tokens`. 
It modifies `tokens`. Firstly, it makse `index` of `tokens` the answer of multiplication. Nextly, it deletes the operator the previous and next number of it. 

```python
def multiplyPrevAndNext(line, index, tokens):
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
```

`devidePrevIntoNext` divide the preavious number into the next number of the slash `/` mark and returns a new `tokens`
It modifies `tokens` as well and make `index` of `tokens` the answer of division.

```python
def dividePrevIntoNext(line, index, tokens):
    prev = tokens[index - 1]['number']
    next = tokens[index + 1]['number']
    number = prev / next

    if isinstance(number, int):
        token = {'type': 'INTEGER', 'number': int(number)}
    else:
        token = {'type': 'FLOAT', 'number': float(number)}
    tokens[index] = token
    del tokens[index - 1]
    del tokens[index]

    return tokens, index + 1
```

In the second while loop of `evaluate(line)`, it does addition and substraction.

```python
# Calculate + and -.  
answer = 0
index = 1
while index < len(tokens):
    if tokens[index]['type'] == 'INTEGER':
        answer, index = addAndSubstructInteger(answer, tokens, index)
    elif tokens[index]['type'] == 'FLOAT':
        answer, index = addAndSubstructFloat(answer, tokens, index)
    index += 1
return answer
```
