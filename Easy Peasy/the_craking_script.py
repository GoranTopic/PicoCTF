import nclib
PAD_LEN = 50000
user_input = "00000000000000000000000000000000"


# connect to nc mercury.picoctf.net 41934
nc = nclib.Netcat(('mercury.picoctf.net', 41934), verbose=False)

# recive the initial message form server with the encrypted key
recived_message = nc.recv_until("What data would you like to encrypt?")

# get the key from the message 
encrypted_flag = recived_message.splitlines()[2].decode('utf-8')
# messure the length of the encrypted flag and does how much of the pad it has used
print("ecrpted flag: {}".format(encrypted_flag))
# get the length from the message
encrypted_flag_len = len(encrypted_flag) / 2
print(encrypted_flag_len)

filling = ""
for i in range(0, int(PAD_LEN - encrypted_flag_len)):
    filling += "a"
print("filling length: {}".format(len(filling)))

# send filling to move the the stop counte back to the begining
nc.send_line(filling) 

# recive message
nc.recv_until("What data would you like to encrypt?")

# send the user input 
nc.send_line(user_input) 
recived_message = nc.recv_until("What data would you like to encrypt?")

# get encrypted user input 
encrypted_user_input = recived_message.splitlines()[1].decode('utf-8')

print("ecrypt user input: {}".format(encrypted_user_input))
print(len(encrypted_user_input) == len(encrypted_flag))

# use the encrypted ui and the user input to get the pad in the position where the flag was previously encrypted.
#key = encrypted_user_input ^ hex_user_input

# find out the the what the key is 
key_arr = [] # arr to store the key integers
ui_index = 0
for i, j in zip(range(0, len(encrypted_user_input),2), range(0, len(user_input))):
    # get the next two chars in encrypted ui
    hexed = encrypted_user_input[i:i+2] 
    # get the unencrypted ui char
    ui_char = user_input[j] 
    # read hexadecimal as a int
    unhexed = int(hexed, 16) 
    # read the char as a int
    ui_int = ord(ui_char)
    # calculate the key with the unhexed value and the ui_int
    key_int = unhexed ^ ui_int
    print("     {:08b} <- ui\n \
xor {:08b} <- ecrypted ui\n\
    ------------\n\
     {:08b} <- key value\n".format(ui_int, unhexed, key_int))
    # add to the key array of ints
    key_arr.append(key_int)
# make ints into a string
key = "".join(list(map(lambda num: str(num), key_arr)))
print("\nthe key is: {}".format("".join(key)))



#print("{:08b} : ecnypted ui\n {:08b} : ui \n------------------------\n{:08b} : key".format(encrypted_ui, str(hex_ui, key)))




nc.close()



