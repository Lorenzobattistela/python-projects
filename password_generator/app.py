from werkzeug.security import check_password_hash, generate_password_hash
import random
import string


def main():
    limit_low = 0
    limit_high = 100000
    random_number = random.randint(limit_low, limit_high)
    random_word = randomword(10)
    randomized_password = str(random_number) + random_word
    print(randomized_password)


def randomword(length):
    chars = list("".join(chr(x) for x in range(32, 127)))
    return ''.join(random.choice(chars) for i in range(length))


if __name__ == '__main__':
    main()
