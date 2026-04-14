from db import connect_db

def add_student():
    conn = connect_db()
    cursor = conn.cursor()

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    query = "INSERT INTO students (name, age, marks) VALUES (%s, %s, %s)"
    values = (name, age, marks)

    cursor.execute(query, values)
    conn.commit()

    print("Student added successfully!")

    cursor.close()
    conn.close()


def view_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()

    print("\n--- Student Records ---")
    for row in results:
        print(row)

    cursor.close()
    conn.close()


def delete_student():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = int(input("Enter student ID to delete: "))

    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()

    print("Student deleted successfully!")

    cursor.close()
    conn.close()

def update_student():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = int(input("Enter student ID to update: "))
    new_marks = float(input("Enter new marks: "))

    query = "UPDATE students SET marks = %s WHERE id = %s"
    cursor.execute(query, (new_marks, student_id))
    conn.commit()

    print("Student updated successfully!")

    cursor.close()
    conn.close()


def menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Update Student")
    print("5. Exit")


def main():
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

