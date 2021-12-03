import sys

student_info = {}
f = open(sys.argv[1], "r", encoding="utf-8")


for line in f:
    name = line.split(":")[0]
    student_info[name] = (line.split(":")[1]).split(",")

for item in sys.argv[2].split(","):
    try:
        university = student_info[item][0]
        department = student_info[item][1]
        print("Name: " + str(item) + "\nUniversity: " + str(university) + "\nDepartment: " + str(department))

        except KeyError:
        print("\nNo record of '{}' was found".format(item))


