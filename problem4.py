#pallindrome
text=input("enter a string")
reversed_text =""
for i in text:
    reversed_text = i+ reversed_text
if (text==reversed_text):
    print("pllindrome")
else:
    print("nota pallindrome")
print("reversed text :",reversed_text)
