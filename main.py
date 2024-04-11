# Khizar Khan

num = input("give number")
num2 = ""

def encode(num_string : str) -> str:
    encoded = ""
    for char in num_string:
        encoded += str(int(char) + 3 % 10)
        return encoded

def main():
    op = 1
    while op in range(1,3):
        print("Encoder")
        print("------------------")
        print("0. Exit")
        print("1. Encode")
        print("2. Decode")

        op = int(input("Select an option: "))
