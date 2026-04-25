import sqlite3

def add_student(name, student_class):
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, class) VALUES (?, ?)", (name, student_class))
    conn.commit()
    conn.close()
    print(f"✅ تم تسجيل الطالب: {name}")

# واجهة بسيطة لك كمطور
print("--- إضافة طالب جديد ---")
s_name = input("اسم الطالب: ")
s_class = input("الفصل: ")
add_student(s_name, s_class)

