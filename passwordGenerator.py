import string
import random
def generateRandomPassword(n,symbols = 'N',capital = 'N'):
    password = ''
    for i in range(0,n):
        password = password + random.choice(string.ascii_letters)
    print(password)
    if symbols == 'Y':
        randInd = random.randrange(0,n-1)
        temp = random.choice(string.punctuation)
        password = password[:randInd-1]+ temp + password[randInd:]
        
    if capital == 'Y':
        randInd = random.randrange(0,n-1)
        password =''.join(c.upper() if i == randInd else c for i, c in enumerate(password))


    return password
        

def main():
    numChar = input("How many characters do you want?: ")
    symbols = input("Do you want to include symbols?: Y or N ")
    capital = input("Do you require a capital letter?: Y or N ")
    password = generateRandomPassword(int(numChar),symbols,capital)

    

if __name__ == "__main__":
    main()

