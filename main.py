# Khizar Khan


def encode(num_string: str) -> str:
    encoded = ""
    for char in num_string:
        encoded += str((int(char) + 3) % 10)
    return encoded


def main():
    op = 1
    while op in range(1, 3):
        print("Encoder")
        print("------------------")
        print("0. Exit")
        print("1. Encode")
        print("2. Decode")

        op = int(input("Select an option: "))

        if op == 0:
            break
        elif op == 1:
            num_string = input("enter a password to encode: ")
            print(f"Original password: {num_string}")
            print("New password: " + encode(num_string))
        elif op == 2:
            num_string = input("enter a password to decode: ")
            print(f"Orignal password : {num_string}")
            # print(f"Decoded password: " + decode(num_string))


if __name__ == "__main__":
    main()
