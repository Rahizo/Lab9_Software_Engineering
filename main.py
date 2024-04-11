# Khizar Khan


def encode(num_string: str) -> str:
    encoded = ""
    for char in num_string:
        encoded += str((int(char) + 3) % 10)
    return encoded


def main():
    op = 1
    while op in range(1, 3):
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")

        op = int(input("Please enter an option: "))

        if op == 0:
            break
        elif op == 1:
            num_string = input("Please enter your password to encode:  ")
            # print(f"Original password: {num_string}")
            newString = encode(num_string)
            print("Your password has been encoded and stores!")
            # print("New password: " + encode(num_string))
        elif op == 2:
            num_string = input("enter a password to decode: ")
            # print(f"Orignal password : {num_string}")
            # print(f"Decoded password: " + decode(num_string))
            decodedString = decode(num_string)
            print("The encoded password is " + num_string + ", and the original password is " +
                  decode(num_string))
        else:
            break

#Quang Dat Hoang
def decode(num_string: str) -> str:
    decoded = ""
    for char in num_string:
        decoded += str((int(char) - 3) % 10)
    return decoded
    
if __name__ == "__main__":
    main()
