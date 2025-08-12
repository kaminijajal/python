p = float(input("Enter Percentage "))

if p > 95 and p <=100:
    print("Grade A+")
elif p >80 and p <= 94:
    print("Grade A")
elif p>70 and p <= 81:
    print("Grade B")
elif p>50 and p <= 71:
    print("Grade C")
elif p>35 and p <= 51:
    print("Grade D")
else :
    print("Fail")