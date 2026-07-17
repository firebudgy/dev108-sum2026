# Dev 108 - Dragan Tuip - 7/16/2026

print("Starting Salesbot...")
start = input("Hey, welcome to Salesbot V1! Would you like to continue? [Y/N] ")
price = int(1500000)
if start == "Y":
    print("Now introducing, the Urbanmech!")
    print("This product consists of several notable features:\nEnough armor to withstand heavy fire from the mightiest of foes.\nThe latest in 360-degree gyros to grant you perfect accuracy where necessary.\nAn engine reaching a whopping speed of 'SLOW' on the field!")
    print("All of this is available in one neat package.")
    salesstart = input("Are you interested in purchasing our product? [Y/N] ")
    
    if salesstart == "Y":
        print("Unit price is 1,500,000 C-Bills.")
        name = input("Please enter your NAME here: ")
        email = input("Please enter your EMAIL here: ")
        address = input("Please enter your MAILING ADDRESS here: ")
        qty = int(input("Please enter HOW MANY UNITS you would like to buy, as a number: "))

        finalprice = (price * qty) * 1.1

        print("Your final total is:" ,finalprice) 
        print("10 percent tax has been added to allow for shipping and handling costs.")

        reciept = input("Would you like a receipt for your order? This will confirm your order. [Y/N] ")
        if reciept == "Y":
            print("QuicSell Corporation Receipt")
            print("Name: ",name)
            print("Email: ", email)
            print("Address: ", address)
            print("Quantity ordered: ", qty)
            print("Final Total: ", finalprice)
        else:
            print("Thank you for your time!")

    else:
        print("Thank you for your time!")
elif start == "N":
    print("Stopping!")
else:
    print("That wasn't a valid input!")