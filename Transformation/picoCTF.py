flag = "picoCTF{16_bits_inst34d_of_8_75d4898b}" 


final_enc = ''.join( [chr( (ord(flag[i]) << 8) + ord(flag[i + 1]) ) for i in range(0, len(flag), 2)])


myEncode = ''
print("for every two characters in: " + flag)
for i in range(0, len(flag), 2):
        first_int = ord(flag[i])
        print("\nthe selected letter transform to a int")
        print( flag[i] + " -> " + str(first_int))
        second_int = ord(flag[i + 1])
        print("and the one after that")
        print( flag[i + 1] + " -> " + str(second_int))
        print("\nbit shift 8 to the left")
        bit_shifted = first_int << 8 
        print( str(bin(first_int)) + " <<8 = " + str(bin(bit_shifted)))
        print('\nadd the next letter with the curent one')
        added_value = bit_shifted + second_int
        print(str(bit_shifted) + " + " + str(second_int) + " = " + str(added_value))
        print("or in binary:")
        print( bin(bit_shifted) + " + " + bin(second_int) + " = " + bin(added_value))
        encoded = chr(added_value) 
        print("\nthen encode the value into unicode")
        print( str(added_value) + " -> " + encoded)
        myEncode += encoded # add to list




final_enc = ''.join( [chr( (ord(flag[i]) << 8) + ord(flag[i + 1]) ) for i in range(0, len(flag), 2)])

print("\nThus " + flag + " -> " + myEncode)
print('\n') 
print(myEncode + " == " + final_enc + "?")

if(myEncode == final_enc):
    print("they are the same")
else:
    print("they are not the same")

decoded = ''
print("\nNow let revese it!")
for enc_char in final_enc:
    print("\nFirst let's convet it back into a int")
    added_value = ord(enc_char)
    print( enc_char + " -> " + str(added_value))
    print("\n get the first 8-bits")
    first_int = added_value >> 8
    print( str(bin(added_value)) + " >>8 = " + str(bin(first_int)))
    print("\n get the last 8-bits")
    second_int = added_value & 255
    print( str(bin(added_value)) + " & 255 = " + str(bin(second_int)))
    print("\n Now we encode to unicode both ints")
    first_char = chr(first_int)
    print( str(first_int) + " -> " + first_char)
    second_char = chr(second_int)
    print( str(second_int) + " -> " + second_char)
    decoded += first_char
    decoded += second_char


print("\nThus " + myEncode + " -> " + decoded)
    



