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

    # State 1: etsi vasemmalta ensimmäinen 0 tai 1
    rules += [
        ('L', 1, 'L', 1, 'RIGHT'),
        ('X', 1, 'X', 1, 'RIGHT'),
        ('0', 1, 'X', 2, 'RIGHT'),  # muista että haetaan 0-pari
        ('1', 1, 'X', 3, 'RIGHT'),  # muista että haetaan 1-pari
        ('R', 1, 'R', 6, 'RIGHT'),  # kaikki käsitelty → hyväksyntä
    ]

    # State 2: haetaan oikealta vastaava 0
    rules += [
        ('0', 2, '0', 2, 'RIGHT'),
        ('1', 2, '1', 2, 'RIGHT'),
        ('X', 2, 'X', 2, 'RIGHT'),
        ('R', 2, 'R', 4, 'LEFT'),
    ]

    # State 3: haetaan oikealta vastaava 1
    rules += [
        ('0', 3, '0', 3, 'RIGHT'),
        ('1', 3, '1', 3, 'RIGHT'),
        ('X', 3, 'X', 3, 'RIGHT'),
        ('R', 3, 'R', 5, 'LEFT'),
    ]

    # State 4: tarkista löytyykö viimeinen 0
    rules += [
        ('X', 4, 'X', 4, 'LEFT'),
        ('0', 4, 'X', 7, 'LEFT'),   # pari löytyi
        ('1', 4, '1', 8, 'LEFT'),   # väärä pari → reject
        ('L', 4, 'L', 8, 'LEFT'),   # ei löytynyt → reject
    ]

    # State 5: tarkista löytyykö viimeinen 1
    rules += [
        ('X', 5, 'X', 5, 'LEFT'),
        ('1', 5, 'X', 7, 'LEFT'),   # pari löytyi
        ('0', 5, '0', 8, 'LEFT'),   # väärä pari → reject
        ('L', 5, 'L', 8, 'LEFT'),   # ei löytynyt → reject
    ]

    # State 7: palaa alkuun uutta kierrosta varten
    rules += [
        ('0', 7, '0', 7, 'LEFT'),
        ('1', 7, '1', 7, 'LEFT'),
        ('X', 7, 'X', 7, 'LEFT'),
        ('L', 7, 'L', 1, 'RIGHT'),
    ]

    # State 6: ACCEPT
    rules += [
        ('R', 6, 'R', 6, 'ACCEPT')
    ]

    # State 8: REJECT
    rules += [
        ('L', 8, 'L', 8, 'REJECT'),
        ('0', 8, '0', 8, 'REJECT'),
        ('1', 8, '1', 8, 'REJECT'),
        ('X', 8, 'X', 8, 'REJECT'),
        ('R', 8, 'R', 8, 'REJECT'),
    ]

    return rules





if __name__ == "__main__":
    rules = create_rules()

    print(calculate("00", rules)) # True
    print(calculate("001001", rules)) # True
    print(calculate("10111011", rules)) # True
    print(calculate("01", rules)) # False
    print(calculate("00100", rules)) # False
    print(calculate("10111101", rules)) # False