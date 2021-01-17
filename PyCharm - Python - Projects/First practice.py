#1----------------- Converting a binary number to integer ---------------------
print(int('1110',2))    # the result is 14
print(int('101',2))     # the result is 5

#2------------------ Converting a integer to binary ---------------------------
print(bin(14))          # the result is 0b1110 - b is binary,
print(bin(5))           # the result is 0b101

#3----------------------Python Bitwise Operators Example-----------------------
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

# Binary AND - Operator copies a bit to the result if it exists in both operands
c = a & b        # 12 = 0000 1100
print ("Line 1 - Value of c is ", c)

# Binary OR - It copies a bit if it exists in either operand
c = a | b       # 61 = 0011 1101
print ("Line 2 - Value of c is ", c)

# Binary XOR - It copies the bit if it is set in one operand but not both.
c = a ^ b       # 49 = 0011 0001
print ("Line 3 - Value of c is ", c)

# Binary NOT	It is unary and has the effect of 'flipping' bits.
c = ~a          # -61 = 1100 0011
print ("Line 4 - Value of c is ", c)

# Binary Left Shift	The left operands value
# is moved left by the number of bits specified by the right operand.
c = a << 2       # 240 = 1111 0000
print ("Line 5 - Value of c is ", c)

# Binary Right Shift	The left operands value
# is moved right by the number of bits specified by the right operand.
c = a >> 2       # 15 = 0000 1111
print ("Line 6 - Value of c is ", c)