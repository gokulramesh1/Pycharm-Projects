# Given two alien number systems and a number from the first system.
# Convert the number first to decimal
# Convert the decimal result to second system


def to_dec(sys, num):
    base = len(sys)

    # map alien number to a list of decimal values each corresponding to a digit position
    d = {sys[i]: i for i in range(base)}
    a = [d[char] for char in str(num)]

    # multiply each value with base^position, where position starts at 0 from the right.
    for i in range(len(a)-1, -1, -1):
        a[i] = a[i]*(base**(abs(len(a)-1)-i))

    return sum(a)


def from_dec(num, sys):
    base = len(sys)

    # Divide by base and update to quotient. Make a reversed list of the remainders.
    a = []
    while num > 0:
        a.append(num % base)
        num = num//base
    a.reverse()

    # Map list values to system characters
    d = {i: sys[i] for i in range(base)}
    a = [d[char] for char in a]
    return ''.join(a)


def alien(sys1, sys2, num):
    dec = to_dec(sys1, num)
    result = from_dec(dec, sys2)
    return result


print(alien('0123456789', '01', 25))
print(alien('o8F', 'qa23def', 'Fo88o'))
print(alien('9IJNYTFCHEWAZX', '2DM98765LBvZP01', 'XAC9WJI'))