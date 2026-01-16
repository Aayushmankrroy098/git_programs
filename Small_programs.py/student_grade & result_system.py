'''def compute_result(names, marksB):
    Obtained_marks = []
    percentages = []
    for i in range(len(names)):
        obtained_mark = sum(marksB[i])
        Obtained_marks.append(obtained_mark)
        percent = ((obtained_mark)/400)*100
        percentages.append(percent)

        print("\n--- RESULT ---")
        print(f"Student name: {names[i]}")
        print("Total Obtained Marks:", Obtained_marks[i])
        print(f"Percent: {percentages[i]}%")
    
        if percentages[i]>=90:
            print(f"Grade: A+")
        elif percentages[i]>=80:
            print("Grade: A")
        elif percentages[i]>=60:
            print("Grade: B+")
        elif percentages[i]>=50:
            print("Grade: B")
        elif percentages[i]>=40:
            print("Grade: C+")
        else:
            print("Grade: C (Fail)")
        if percentages[i]>=40:
            print("Status: Pass")
        else:
            print("Status: Fail")

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
compute=compute_result(names, marksB)'''

# ====================ALTERNATIVE AND PROFESSIONAL===========================

def get_grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 60:
        return "B+"
    elif percent >= 50:
        return "B"
    elif percent >= 40:
        return "C+"
    else:
        return "C (Fail)"


def compute_result(names, marksB):
    results = []

    for i in range(len(names)):
        total = sum(marksB[i])
        full_marks = len(marksB[i]) * 100
        percent = (total / full_marks) * 100

        grade = get_grade(percent)
        status = "Pass" if percent >= 40 else "Fail"

        results.append((names[i], total, percent, grade, status))

    return results


# ---------- MAIN PROGRAM ----------
n = int(input("Enter number of students: "))

names = []
marksB = []
subjects = ["English", "Nepali", "Maths", "Science"]

for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    names.append(name)

    marksA = []
    for sub in subjects:
        mark = int(input(f"Enter marks of {sub} = "))
        marksA.append(mark)

    marksB.append(marksA)


results = compute_result(names, marksB)

for r in results:
    print("\n--- RESULT ---")
    print("Student name:", r[0])
    print("Total Obtained Marks:", r[1])
    print(f"Percent: {r[2]:.2f}%") #:.2f = round and display the number to 2 decimal places
    print("Grade:", r[3])
    print("Status:", r[4])

#\\\\\\\\\\\\\dry_run\\\\\\\\\\\\\\\
# results= [
#           ("Ram", total0, percent0, grade0, status0),
#           ("Shyam", total1, percent1, grade1, status1),
#           ("Hari", total2, percent2, grade2, status2)
#          ]
