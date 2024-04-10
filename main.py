


def menu():
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()


def main():
    encoded_string = ""
    while True:
        menu()
        greenfn = int(input("Enter an option: "))
        if greenfn == 1:
            password = str(input("password お願いいたします。"))
            for i in password:
                if i == "0":
                    encoded_string += "3"
                if i == "1":
                    encoded_string += "4"
                if i == "2":
                    encoded_string += "5"
                if i == "3":
                    encoded_string += "6"
                if i == "4":
                    encoded_string += "7"
                if i == "5":
                    encoded_string += "8"
                if i == "6":
                    encoded_string += "9"
                if i == "7":
                    encoded_string += "0"
                if i == "8":
                    encoded_string += "1"
                if i == "9":
                    encoded_string += "2"
            print("I stored, and encoded dat bih")

        if greenfn == 2:
            #subtract 3 from each of the given numbers but it's kinda redundant
            #Sebastien added this function
            print(f"The encoded password is {encoded_string}, and the original password is {password}")

        if greenfn == 3:
            #Sebastien also added this function
            break
if __name__ == "__main__":
    main()




