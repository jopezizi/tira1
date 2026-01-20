def calculate(input, rules):
    rules_d = {}
    for rule in rules:
        rules_d[(rule[0],rule[1])] = (rule[2],rule[3],rule[4])

    input = 'L'+ input + 'R'
    new_char = 0
    char = 0
    state = 1
    acceptance = False
    operations = {"LEFT":-1, "RIGHT":1, "ACCEPT":True, "REJECT": False}

    counter = 0
    max_counter = 1000
    while char < len(input):
        counter += 1
        if counter > max_counter:
            break

        key = (input[char],state)
        if key not in rules_d:
            break
        
        operation = rules_d[key][2]
        if operation == "LEFT" or operation == "RIGHT":
            new_char = operations[operation]
        elif operation == "ACCEPT" or operation == "REJECT":
            acceptance = operations[operation]
        new_input = input[:char] + rules_d[key][0] + input[char+1:]
        state = rules_d[key][1]
        char += new_char
        input = new_input
    return acceptance


if __name__ == "__main__":
    rules = []

    rules.append(("L", 1, "L", 2, "RIGHT"))
    rules.append(("L", 3, "L", 2, "RIGHT"))

    rules.append(("0", 2, "X", 4, "RIGHT"))
    rules.append(("1", 4, "X", 5, "RIGHT"))
    rules.append(("1", 2, "X", 6, "RIGHT"))
    rules.append(("0", 6, "X", 7, "RIGHT"))

    rules.append(("0", 4, "0", 4, "RIGHT"))
    rules.append(("0", 5, "0", 5, "RIGHT"))
    rules.append(("0", 7, "0", 7, "RIGHT"))
    rules.append(("1", 6, "1", 6, "RIGHT"))
    rules.append(("1", 5, "1", 5, "RIGHT"))
    rules.append(("1", 7, "1", 7, "RIGHT"))

    rules.append(("X", 2, "X", 2, "RIGHT"))
    rules.append(("X", 4, "X", 4, "RIGHT"))
    rules.append(("X", 5, "X", 5, "RIGHT"))
    rules.append(("X", 6, "X", 6, "RIGHT"))
    rules.append(("X", 7, "X", 7, "RIGHT"))

    rules.append(("R", 2, "R", 2, "ACCEPT"))
    rules.append(("R", 4, "R", 4, "REJECT"))
    rules.append(("R", 6, "R", 6, "REJECT"))

    rules.append(("R", 5, "R", 3, "LEFT"))
    rules.append(("R", 7, "R", 3, "LEFT"))
    rules.append(("0", 3, "0", 3, "LEFT"))
    rules.append(("1", 3, "1", 3, "LEFT"))
    rules.append(("X", 3, "X", 3, "LEFT"))

    print(calculate("0", rules)) # False
    print(calculate("00", rules)) # False
    print(calculate("01", rules)) # True
    print(calculate("0110", rules)) # True
    print(calculate("0101", rules)) # True
    print(calculate("1000", rules)) # False
    print(calculate("00110101", rules)) # True
    print(calculate("00111101", rules)) # False