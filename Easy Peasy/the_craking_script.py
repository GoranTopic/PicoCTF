import nclib
PAD_LEN = 50000

def unhex_to_int_list(hex_input): 
    unhexed = []
    for i in range(0, len(hex_input), 2):
        # get the next two chars in encrypted ui
        hexed = hex_input[i:i+2] 
        # get the unencrypted ui char
        unhexed.append( int(hexed, 16) )
    return unhexed

# connect to nc mercury.picoctf.net 41934
nc = nclib.Netcat(('mercury.picoctf.net', 41934), verbose=False)

# recive the initial message form server with the encrypted key
recived_message = nc.recv_until("What data would you like to encrypt?")

# get the key from the message 
hexed_flag = recived_message.splitlines()[2].decode('ascii').strip()
# messure the length of the encrypted flag and does how much of the pad it has used
print("ecrpted flag: {}".format(hexed_flag))
# get the length from the message
encrypted_flag_len = int(len(hexed_flag) / 2)
print(encrypted_flag_len)

# create filling to sen tot server
filling = "a" * (PAD_LEN - encrypted_flag_len)
print("filling length: {}".format(len(filling)))

# send filling to move the the stop counte back to the begining
nc.send_line(filling) 

# recive message
nc.recv_until("What data would you like to encrypt?")

# creatte user input
user_input = 'a' * encrypted_flag_len

# send the user input 
nc.send_line(user_input) 
recived_message = nc.recv_until("What data would you like to encrypt?")

# get encrypted user input 
encrypted_user_input = str(recived_message.splitlines()[1], "ascii").strip()

print("ecrypt user input: {}".format(encrypted_user_input))

# use the encrypted ui and the user input to get the pad in the position where the flag was previously encrypted.
encrypted_user_input = unhex_to_int_list(encrypted_user_input)

# find out the the what the key is 
key_arr = [] # arr to store the key integers
for i in range(0, len(user_input)):
    # get the unencrypted ui char
    ui_int = ord(user_input[i]) 
    eui_int = encrypted_user_input[i]
    # read hexadecimal as a int
    # calculate the key with the unhexed value and the ui_int
    key_int = eui_int ^ ui_int
    print("\
            {:08b} <- ui\n\
            {:08b} <- ecrypted ui\n\
            ------------\n\
            {} <- key value\n".format(ui_int, eui_int, key_int))
    # add to the key array of ints
    key_arr.append(key_int)
# make ints into a string
key = "".join(list(map(lambda num: chr(num), key_arr)))
print("\nThe key is: {}".format(key))


# unhex the flag so that you can have it 
encrypted_flag = unhex_to_int_list(hexed_flag)

# use the found key to decrypt the flag
flag_values = []
for i in range(0, len(encrypted_flag)):
    key_value = key_arr[i]
    encry_flag_value = encrypted_flag[i]
    print("key_value: {}".format(key_value))
    
    flag_value = encry_flag_value ^ key_value
    print("\
            {0:08b} {0} <- encry Flag\n\
            {1:08b} {1} <- key\n\
            ----------\n\
            {2:08b} {2} <- flag\n\
            ".format(encry_flag_value, key_value, flag_value, flag_value))
    flag_values.append(chr(flag_value))
flag = "".join(flag_values)
print("\nthe flag is picoCTF{%s}" % flag)


nc.close()



