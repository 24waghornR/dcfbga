import time

while True:
    print('Package File:')
    package = input()

    print("Is this the correct file?")
    print(package)
    verify = input("Y/N (Default: Y):").upper()

    if verify == "Y" or verify == "":
        break
    else:
        print("Please try again.")
        
autho = input("Would you like to verify this package? Unauthorised patches can harm your device. Y/N (Default: Y): \n").upper()
if verify == "Y" or verify == "":
        print("Verifying...")
        time.sleep(4)
        
print("Connect your device to the computer.")
time.sleep(3)
print("iPad 9th Generation")
time.sleep(0.9)
print("Please verify that "+package+" is the correct patch for your device.")
