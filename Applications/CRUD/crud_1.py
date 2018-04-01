studentList = []
studentData = {}

def create():
    id = 1
    studentName = input("Enter student name : ")
    studentAge = int(input("Enter student age : "))
    studentCourse = input("Enter student course : ")

    studentData['Name'] = studentName
    studentData['Age'] = studentAge
    studentData['Course'] = studentCourse

    studentList.append(studentData.copy())

    for student in studentList:
        print(id,student)
        id += 1

def read():
    id = 1
    for student in studentList:
        print(id,student)
        id += 1

def update():
    pass

def delete():
    pass

def search():
    pass

def sort():
    sort_by = input("Sort by name or age ?")
    studentList.sort(key=lambda x : x[sort_by.capitalize()])
    print("Sorted List")
    read()

def save():
    pass

def load():
    pass

while True:
    print("""
    1. Create
    2. Read
    3. Update
    4. Delete
    5. Search
    6. Sort
    7. Save
    8. Load
    """)

    todo = {
        "1" : create,
        "2" : read,
        "3" : update,
        "4" : delete,
        "5" : search,
        "6" : sort,
        "7" : save,
        "8" : load
    }

    userChoice = input("Enter your choice : ")
    todo.get(userChoice)()