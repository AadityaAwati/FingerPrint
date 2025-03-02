from fingerprint_scanner import FingerPrint

def scan_fingerprint():
    print("Place your finger on the sensor ...")
    my_fingerprint.open()

    print("Starting Identification Process ...\n")
    my_fingerprint.identify()

    print("Success! Finger-Print has been stored temporarily.")
    print("Please Place A Finger On the Sensor, to check whether it is the same one or not ...\n")

    if my_fingerprint.verify():
        print("Welcome! Authorized User.")
    else:
        print("Sorry! You have not been authorized.")


print("\n\n\n!!! IN-ORDER FOR THE PROGRAM TO FUNCTION, THIS PROGRAM MUST ME EXECUTED IN A CMD PROMPT RUN AS AN ADMIN !!!\n\n\n")
print("\t\t\t\t\t\t\t\t\tFINGER-PRINT SENSOR READ PROGRAM\n\n")

my_fingerprint = FingerPrint()
my_fingerprint.print_data = True

if my_fingerprint.print_data:
    print("The program has been set to print_data = 'True' Mode. To change this, change the variable's value in the main.py program to 'False' Mode.\n")

try:
    scan_fingerprint()
except SystemError as error_message:
    if my_fingerprint.print_data:
        print(f"\nprint_data logs -> ERROR OCCURRED: '{error_message}'")

    print("Sorry! There was a problem, while attempting to identify/verify the fingerprint. The program will run once again.\n\n")
    scan_fingerprint()
finally:
    my_fingerprint.close()
