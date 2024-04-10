


def menu():
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()


if __name__ == "__main__":
    menu()
    greenfn = int(input("Enter an option: "))
    encoded_string = ""
    if greenfn == 1:
        for i in len(greenfn):
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
            else:
                encoded_string += "2"

        password = str(input("password お願いいたします。"))
        print("I stored, and encoded dat bih")


