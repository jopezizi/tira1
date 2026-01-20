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
    # 1 = alkutila
    # 2 = eka 0
    # 3 = eka 1 
    # 4 = etsi 0
    # 5 = etsi 1
    # 6 = palaa alkuun

    rules.append(("L", 1, "L", 1, "RIGHT"))

    rules.append(("0",1,"A",2, "RIGHT"))
    rules.append(("1",1,"A",3, "RIGHT"))

    rules.append(("0",3,"0",5, "RIGHT"))
    rules.append(("1",2,"1",4, "RIGHT"))

    rules.append(("0",4,"B",6, "LEFT"))
    rules.append(("1",5,"B",6, "LEFT"))

    rules.append(("0",6,"A",2, "RIGHT"))
    rules.append(("1",6,"A",3, "RIGHT"))

    rules.append(("A",2,"A",4, "RIGHT"))
    rules.append(("B",2,"B",4, "RIGHT"))

    rules.append(("A",3,"A",5, "RIGHT"))
    rules.append(("B",3,"B",5, "RIGHT"))

    rules.append(("0",5,"0",5, "RIGHT"))
    rules.append(("1",4,"1",4, "RIGHT"))
    
    rules.append(("L",6,"L",6,"ACCEPT"))

    return rules


if __name__ == "__main__":
    rules = create_rules()

    print(calculate("101101", rules)) # True