def check_palindrom(str):
    for i in range(int(len(str)/2)):
        a = len(str) - i - 1
        print(i, str[i], a, str[a])
        if str[i] != str[a]:
            return False
    return True


print(check_palindrom("asdfsaf"))
print()
print(check_palindrom("asdf0fdsa"))

#  d = O * N
#  d = O * N/2
