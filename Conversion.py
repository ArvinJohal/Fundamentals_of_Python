# decimal = int(input("Please enter a number to convert"))
# binary = ""
# while decimal > 0:
#     r = decimal%2
#     binary = str(r)+binary
#     decimal = decimal//2
# print (binary)

# binary = input("Please enter a binary number to convert")
# denary = 0
# power = 0
# for digit in binary[::-1]:
#     if digit == "1":
#         denary = denary + 2**power
#     power = power+1
        
# print (denary)

binary = input("Please enter a binary number")
binary_to_hex = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F"
}

while len(binary)%4 != 0:
    binary = "0"+binary
hexadecimal = ""
for i in range(0, len(binary), 4):
    print (binary[i:i+4])
    hexadecimal+=binary_to_hex[binary[i:i+4]]
print (hexadecimal)