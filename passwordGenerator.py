import string
import random

def main():
    password = ''
    numChar = input("How many characters do you want?: ")
    for i in range(0,int(numChar)) :
        password = password + random.choice(string.ascii_letters)
    print(password)

if __name__ == "__main__":
    main()

