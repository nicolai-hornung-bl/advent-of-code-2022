def findPacket(chars, length):
    for c in list(enumerate(chars))[:-length]:
        if len(set(chars[c[0]:c[0]+length])) == length:
            return (c[0]+length, chars[c[0]:c[0]+length])

with open('door-6/input.txt', 'r') as input:
    chars = input.read()
    input.close()
    print(f"start-of-packet {findPacket(chars, 4)}")
    print(f"start-of-message {findPacket(chars, 14)}")
