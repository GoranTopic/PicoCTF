#!/usr/bin/python3 -u
import os.path

KEY_LEN = 100
KEY_FILE = "key"
FLAG_FILE = "flag"


def startup(key_location):
	flag = open(FLAG_FILE).read()
	kf = open(KEY_FILE, "rb").read()

	start = key_location
	stop = key_location + len(flag)

	key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
	print("This is the encrypted flag!\n{}\n".format("".join(result)))

	return key_location

def encrypt(key_location):
    ui = input("What data would you like to encrypt? ").rstrip()
    if len(ui) == 0 or len(ui) > KEY_LEN:
        return -1

    start = key_location
    stop = key_location + len(ui)
    print("Key_location: {} + len(ui): {} = {}".format(key_location, len(ui), stop))
    print("stop: {} %  KEY_LEN: {} = {}".format(stop, KEY_LEN, stop % KEY_LEN))

    kf = open(KEY_FILE, "rb").read()

    if stop >= KEY_LEN:
        stop = stop % KEY_LEN
        key = kf[start:] + kf[:stop]
    else:
        key = kf[start:stop]
    key_location = stop

    print("user input: {}".format(ui))
    print("key: {}".format(key))

    print("{} ^ {} = {}".format(3, 2, 3 ^ 2))
    print("ord({}) = {}".format("y", ord("y")))

    result1 = []
    for i in range(0, len(ui)): 
        print("user input letter: {}".format(ui[i]))
        print("key letter: {}".format(key[i]))
        print("ord({0}): {1}".format(ui[i], ord(ui[i]) ))
        print("ord({0}) ^ {1}: {2}".format(ui[i], key[i], ord(ui[i]) ^ key[i]))
        print("{:08b} ^ {:08b} = {:08b}".format(ord(ui[i]), key[i], ord(ui[i])^key[i]))
        print("{:02x}".format(ord(ui[i])^key[i]))
        print("\n")
        result1.append("{:02x}".format(ord(ui[i])^key[i]))


    #result1 = map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key)
    #print("Result1: " + str(list(result1)))

    result2 = map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key)
    #print("Result2: " + str(list(result2)))

    #print("are they the same? {}".format(result1 == result2))

    print("Here ya go!\n{}\n".format("".join(result1)))

    return key_location


print("******************Welcome to our OTP implementation!******************")
c = startup(0)
while c >= 0:
	c = encrypt(c)
