import sqlite3

# إنشاء الاتصال بالملف
connection = sqlite3.connect('school.db')
cursor = connection.cursor()

# إنشاء جدول الطلاب
cursor.execute('''CREATE TABLE IF NOT EXISTS students 
               (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, class TEXT)''')

# إنشاء جدول الحضور
cursor.execute('''CREATE TABLE IF NOT EXISTS attendance 
               (id INTEGER PRIMARY KEY AUTOINCREMENT, student_name TEXT, status TEXT, date TEXT)''')

connection.commit()
connection.close()
print("✅ تم إنشاء نظام تخزين البيانات بنجاح!")

