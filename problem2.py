#calculate total electricity bill based on unit consumed
#upto 100 units rs.



unit = int(input("enter total unit of electricity :"))
if (unit<=100):
    bill= unit *5
elif unit <= 200:
    bill= unit*7
else:
    bill=unit*10
    print("total bill=₹",bill)
           
