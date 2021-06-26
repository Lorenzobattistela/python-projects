
def main():
    email = input('Type your email: ')
    length = len(email)
    user = searchUser(email, length)
    user_length = len(user)
    domain = searchDomain(email, length, user_length)
    show_results(user, domain)
    

def searchUser(email, length):
    user = []
    for i in range(length):
        if email[i] == '@':
            break
        user.append(email[i])
    user = ''.join(user)
    return user

def searchDomain(email, length, user_length):
    domain = []
    counter = 0
    for i in range(length):
        if counter > user_length:
            domain.append(email[i])
        counter += 1
    domain = ''.join(domain)
    return domain

def show_results(user, domain):
    print('The username is: ' + user)
    print('The domain of this email is: ' + domain)
    return

if __name__ == '__main__':
    main()
