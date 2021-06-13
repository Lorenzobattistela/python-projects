from werkzeug.security import check_password_hash, generate_password_hash
import random, string

def main():
    limit_low = 0
    limit_high = 100000
    random_number = random.randint(limit_low, limit_high)
    random_word = randomword(10)
    randomized_password = str(random_number) + random_word
    hashed_password = generate_password_hash(randomized_password)
    print(hashed_password)
    print(randomized_password)

def randomword(length):
   letters = string.ascii_lowercase #transform letters in ascii values
   return ''.join(random.choice(letters) for i in range(length))

if __name__ == '__main__':
    main()