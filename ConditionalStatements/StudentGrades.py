# Calculate student grade based on marks.
marks=int(float(input("enter a marks:")))
if marks>90:
    print("Grade A")
elif marks>80:
    print("Grade B")
elif marks>70:
    print("Grade C")
elif marks>60:
    print("Grade D")
else:
    print("Invalid marks")