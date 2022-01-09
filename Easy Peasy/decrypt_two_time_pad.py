encrypted_flag      = "645b565a7a66704c4a575f53694257504054464c3c"
user_input          = "000000000000000000000000000000000000000000000000000000000000000000000000" # 32 0s
encrypted_user_input = "020709050207050205010501090807090105070702060607050109050304080706060708080209040201040503050906030807070309030201010208040803050303050808040404"

# to get the key from the two time pad we must apply xor to the unecryped user input and the encyrpted user 



print("{}".format(chr(49)))

# find out the the what the key is 
key_chars = []
ui_index = 0
for i in range(0, len(encrypted_user_input), 2):
    hexed = encrypted_user_input[i:i+2] # get the next two chars
    unhexed = int(hexed, 16) # read hexadecimal as a int
    #print("{} = {:08b} = {:d}".format(hexed, unhexed, unhexed)) 
    ui = ord(user_input[ui_index])
    ui_index+=1
    key_value = ui ^ unhexed
    print("ui: {:08b} ^ {:08b} = {:08b}".format(ui, unhexed, key_value))
    key_chars.append(key_value)
key = "".join(list(map(lambda hex: chr(hex), key_chars)))
print("\nthe key is {}".format("".join(key)))

# use Key to decrypt flag
flag_values = []
kindex = 0
for i in range(0, len(encrypted_flag), 2):
    hexed = encrypted_flag[i:i+2] # get the next two chars
    unhexed = int(hexed, 16) # read hexadecimal as a int
    #print("{} = {:08b} = {:d}".format(hexed, unhexed, unhexed)) 
    key_value = key_chars[kindex]
    kindex += 1
    flag_value = unhexed ^ key_value
    print("unhexed: {:08b} ^ Key: {:08b} = flag: {:08b} : {}"
            .format(unhexed, key_value, flag_value, flag_value))
    flag_values.append(chr(flag_value))
flag = "".join(flag_values)
print("\nthe flag is {}".format("".join(flag)))

