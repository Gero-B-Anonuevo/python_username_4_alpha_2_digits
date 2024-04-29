username = input("Input a username: ")
if not username[0:3].isalpha() and not username[4:5].isdigit():
    print("First four characters of username should be from alphabet, while the fifth and sixth characters should be digit")
elif not username[0:3].isalpha():
    print("First four characters of username should be from alphabet")
elif not username[4:5].isdigit():
    print("The fifth and sixth characters of username should be digits")
else:
    print("Good username")
