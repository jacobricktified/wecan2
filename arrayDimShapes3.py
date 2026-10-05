# 2D array
students = [
    ["Jacob", 20],
    ["Brian", 21],
    ["Mary", 19]
]


students.append(["Ann", 22])

students[0][1] = 21

del students[1]
print(students)

# 3D array
students_3d = [
    [
        ["Jacob", 20],
        ["Brian", 21]
    ],
    [
        ["Mary", 19],
        ["Ann", 22]
    ]
]


# Add
students_3d[0].append(["Peter", 23])

# Edit
students_3d[0][0][1] = 21

# Delete
del students_3d[1][1]

print(students_3d)
