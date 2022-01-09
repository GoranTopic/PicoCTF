bytestr = bytes(b'abc') # byt data type as a string 
print(bytestr)
print(bytestr[2])

print(ord('c'))

# two difrent binary values can be read in difrent ways
print(b'\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83'.decode('utf-8'))
print(b'\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83'.decode('latin-1'))

bytesArr = bytearray(b'\x00\x0f') # byarry allows modifications 
#bytesArr[1] = 200
#bytesArr.append(125)
print(bytesArr)
bytesArr.decode('utf-8')



# Code to demonstrate bitwise operations
# Some bytes to play with
byte1 = int('11110000', 2)  # 240
byte2 = int('00001111', 2)  # 15
byte3 = int('01010101', 2)  # 85
byte4 = int('00000000', 2)  # 0?

print('byte4= {:08b}\n'.format(byte4))
  

print('Ones Complement (Flip the bits)')
print(~byte1)
print('{:8b}\n'.format(~byte1))
  
# AND
print('AND')
print(byte1 & byte2)
print('{:08b}\n'.format(byte1 & byte2))
print('{:02x}\n'.format(byte1 & byte2))
  
# OR
print('OR')
print(byte3 | byte2)
print('{:08b}\n'.format(byte3 | byte2))
  
# XOR
print('XOR, true xor true = false')
print(byte3 ^ byte3)
print('{:08b}\n'.format(byte3 ^ byte2))
  

print("j: {:2x}".format(ord('j')))
print(chr(125))
