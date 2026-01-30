def analyze_marks(names, marksB):
    totals = []
    for i in range(len(names)):
        total = sum(marksB[i])
        totals.append(total)
        average = total / len(marksB[i])
        highest = max(marksB[i])
        lowest = min(marksB[i])

        print(f"\n For {names[i]}")
        print("\n--- RESULT ---")
        print("Total Marks:", total)
        print("Average Marks:", average)
        print("Highest Marks:", highest)
        print("Lowest Marks:", lowest)
    return totals    



# ---------- MAIN PROGRAM ----------
n = int(input("Enter number of students: "))

names = []
marksB = []
sub = ["English", "Nepali", "Maths", "science"]

for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    names.append(name)
    marksA = []
    for j in range(len(sub)):
        mark = int(input(f"Enter marks of {sub[j]} =  "))
        marksA.append(mark)
    marksB.append(marksA)
totals=analyze_marks(names, marksB)

print("\nPassed Students:")
for i in range(len(totals)):
    if totals[i] >= 160:
        print(f"{names[i]}'s total marks is {totals[i]}")