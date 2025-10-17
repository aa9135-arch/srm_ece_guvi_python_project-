# input a single character and check if its an alphabet,digit,or special symbol

ch =input("enter a single charecter:")
if ch.isalpha():
    print("the given value is alphabets")
elif ch.isdigit():
    print("the given value is digit")
elif ch.isalnum():
    print("the given  value is invalide")

else:
    print("he given value is special symbol")