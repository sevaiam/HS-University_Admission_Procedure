# write your code here

departments = {'Biotech': [2, 3], 'Chemistry': [3], 'Engineering': [4, 5], 'Mathematics': [4], 'Physics': [2, 4]}
max_per_dept = int(input())
applicant_list = []
applicant_dict = {}
second_chance = []
last_chance = []
with open('applicants.txt', 'r', encoding='utf-8') as file:
    for line in file:
        applicant_list.append(line.split())

applicant_list.sort(key=lambda x: (-float(x[2]), x[0], x[1]))
# applicant_list = applicant_list[:(len(departments) * max_per_dept)]

for dept, gpa in departments.items():
    applicant_dict.setdefault(dept, [])

for dept, gpa in departments.items():
    for applicant in sorted(applicant_list, key=lambda x: (x[7], -max(((float(x[gpa[0]]) + float(x[gpa[-1]])) / 2), int(x[6])), x[0], x[1])):
        if applicant[7] == dept:
            if len(applicant_dict[applicant[7]]) < max_per_dept:
                applicant_dict[applicant[7]].append(applicant)
            else:
                second_chance.append(applicant)

# print(second_chance)
for dept, gpa in departments.items():
    for applicant in sorted(second_chance, key=lambda x: (-max(((float(x[gpa[0]]) + float(x[gpa[-1]])) / 2), int(x[6])), x[8], x[0], x[1])):
        if applicant[8] == dept:
            if len(applicant_dict[applicant[8]]) < max_per_dept:
                applicant_dict[applicant[8]].append(applicant)
            else:
                last_chance.append(applicant)

# print(last_chance)

for dept, gpa in departments.items():
    for applicant in sorted(last_chance, key=lambda x: (-max(((float(x[gpa[0]]) + float(x[gpa[-1]])) / 2), int(x[6])), x[9],  x[0], x[1])):
        if applicant[9] == dept:
            if len(applicant_dict[applicant[9]]) < max_per_dept:
                applicant_dict[applicant[9]].append(applicant)
#
# for dept, gpa in departments.items():
#
#
# for applicant in second_chance:
#     if len(applicant_dict[applicant[4]]) < max_per_dept:
#         applicant_dict[applicant[4]].append(applicant)
#     else:
#         last_chance.append(applicant)
#
# last_chance.sort(key=lambda x: (-float(x[2]), x[0], x[1]))
# for applicant in last_chance:
#     if len(applicant_dict[applicant[5]]) < max_per_dept:
#         applicant_dict[applicant[5]].append(applicant)
# applicant_list = []
# for i in departments:
#     while len(applicant_dict[i]) > max_per_dept:
#         applicant_list.append(applicant_dict[i].pop())


# applicant_list.sort(key=lambda x: (x[3], -float(x[2])))
# for dept in departments:
#     for _ in range(max_per_dept):


# print(len(applicant_list))
# print(applicant_list)
# print(last_chance)
for dept, gpa in departments.items():
    print()
    print(dept)
    applicant_dict[dept].sort(key=lambda x: (-max(((float(x[gpa[0]]) + float(x[gpa[-1]])) / 2), int(x[6])), x[0], x[1]))
    with open(f'{dept.lower()}.txt', 'w', encoding='utf-8') as file:
        for x in applicant_dict[dept]:
            line = f'{x[0]} {x[1]} {max(((float(x[gpa[0]]) + float(x[gpa[-1]])) / 2), int(x[6]))}'
            print(line)
            file.write(line + '\n')

