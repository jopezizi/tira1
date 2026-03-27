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

def create_rules():
    rules = []

    rules.append(("L", 1, "L", 2, "RIGHT"))

    rules.append(("0", 2, "A", 3, "RIGHT"))
    rules.append(("1", 2, "B", 3, "RIGHT"))

    rules.append(("0", 3, "0", 3, "RIGHT"))
    rules.append(("1", 3, "1", 3, "RIGHT"))
    rules.append(("C", 3, "C", 4, "LEFT"))
    rules.append(("D", 3, "D", 4, "LEFT"))
    rules.append(("R", 3, "R", 4, "LEFT"))

    rules.append(("0", 4, "C", 5, "LEFT"))
    rules.append(("1", 4, "D", 5, "LEFT"))
    rules.append(("A", 4, "A", 11, "REJECT"))
    rules.append(("B", 4, "B", 11, "REJECT"))

    rules.append(("0", 5, "0", 5, "LEFT"))
    rules.append(("1", 5, "1", 5, "LEFT"))
    rules.append(("A", 5, "A", 6, "RIGHT"))
    rules.append(("B", 5, "B", 6, "RIGHT"))

    rules.append(("0", 6, "A", 3, "RIGHT"))
    rules.append(("1", 6, "B", 3, "RIGHT"))
    rules.append(("C", 6, "C", 7, "LEFT"))
    rules.append(("D", 6, "D", 7, "LEFT"))

    rules.append(("A", 7, "A", 7, "LEFT"))
    rules.append(("B", 7, "B", 7, "LEFT"))
    rules.append(("C", 7, "C", 7, "LEFT"))
    rules.append(("D", 7, "D", 7, "LEFT"))
    rules.append(("X", 7, "X", 7, "LEFT"))
    rules.append(("L", 7, "L", 8, "RIGHT"))

    rules.append(("X", 8, "X", 8, "RIGHT"))
    rules.append(("A", 8, "X", 9, "RIGHT"))
    rules.append(("B", 8, "X", 10, "RIGHT"))
    rules.append(("R", 8, "R", 12, "ACCEPT"))

    rules.append(("A", 9, "A", 9, "RIGHT"))
    rules.append(("B", 9, "B", 9, "RIGHT"))
    rules.append(("X", 9, "X", 9, "RIGHT"))
    rules.append(("C", 9, "X", 7, "LEFT"))
    rules.append(("D", 9, "D", 11, "REJECT"))

    rules.append(("A", 10, "A", 10, "RIGHT"))
    rules.append(("B", 10, "B", 10, "RIGHT"))
    rules.append(("X", 10, "X", 10, "RIGHT"))
    rules.append(("D", 10, "X", 7, "LEFT"))
    rules.append(("C", 10, "C", 11, "REJECT"))

    return rules
    




if __name__ == "__main__":
    rules = create_rules()

    print(calculate("00", rules)) # True
    print(calculate("001001", rules)) # True
    print(calculate("10111011", rules)) # True
    print(calculate("01", rules)) # False
    print(calculate("00100", rules)) # False
    print(calculate("10111101", rules)) # False