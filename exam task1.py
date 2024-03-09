def check_character(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1

print(check_character('Order of the Phoenix', 'o'))