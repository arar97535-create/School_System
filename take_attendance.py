import sqlite3
from datetime import datetime

# حقوق المطور
DEV_NAME = "أسد محمد العامري"

def record():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    
    # جلب جميع الطلاب من القاعدة
    cursor.execute("SELECT name FROM students")
    students = cursor.fetchall()
    
    if not students:
        print("❌ لا يوجد طلاب مضافين حالياً!")
        return

    date_today = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n--- رصد الحضور ليوم: {date_today} ---")
    print(f"بإشراف المطور: {DEV_NAME}\n")

    for student in students:
        name = student[0]
        # المدرس يضغط 1 للحضور و 0 للغياب لسرعة الإدخال
        status_input = input(f"الطالب [{name}] -> (1 للحضور، 0 للغياب): ")
        
        status = "حاضر" if status_input == '1' else "غائب"
        
        # حفظ السجل في جدول الحضور
        cursor.execute("INSERT INTO attendance (student_name, status, date) VALUES (?, ?, ?)", 
                       (name, status, date_today))
    
    conn.commit()
    conn.close()
    print("\n✅ تم رصد الحضور لجميع الطلاب وحفظه بنجاح!")

if __name__ == "__main__":
    record()

