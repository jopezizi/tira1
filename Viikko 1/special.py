def check_year(year):
    year = list(str(year))
    sum = 0
    for num in year:
        sum += int(num) ** 2

    num_1 = str(sum)[0]
    for num in str(sum):
        if num != num_1:
            return False
    
    return True

if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2000)) # True
    print(check_year(2026)) # True
    print(check_year(2029)) # False
    print(check_year(9215)) # True