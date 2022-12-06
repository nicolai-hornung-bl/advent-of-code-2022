with open('door-6/input.txt', 'r') as input:
    marker = set()
    chars = input.read()
    input.close()
    for c in list(enumerate(chars))[:-4]:
        if len(set(chars[c[0]:c[0]+4])) == 4:
            print(f"start-of-packet loc: {c[0]+4} marker: {chars[c[0]:c[0]+4]}")
            break
    for c in list(enumerate(chars))[:-14]:
        if len(set(chars[c[0]:c[0]+14])) == 14:
            print(f"start-of-message loc: {c[0]+14} marker: {chars[c[0]:c[0]+14]}")
            break