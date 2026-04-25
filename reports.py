import sqlite3
import pandas as pd
from datetime import datetime
import os

def generate_report():
    try:
        # الاتصال بقاعدة البيانات
        conn = sqlite3.connect('school_data.db')
        
        # قراءة جدول الحضور
        df = df = pd.read_sql_query("SELECT * FROM attendance", conn)

        
        if df.empty:
            print("⚠️ لا توجد بيانات حضور مسجلة حتى الآن!")
            return

        # اسم الملف مع التاريخ
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"تقرير_مدرسة_الأسد_{date_str}.xlsx"
        
        # حفظ الملف بصيغة إكسل
        df.to_excel(filename, index=False)
        
        print(f"✅ تم إنشاء الملف: {filename}")
        
        # نقل الملف لمجلد التحميلات ليظهر في الجوال
        os.system(f"cp {filename} ~/storage/downloads/")
        print(f"📂 التقرير الآن موجود في مجلد Downloads بجوالك!")
        
        conn.close()
    except Exception as e:
        print(f"❌ حدث خطأ: {e}")

if __name__ == "__main__":
    generate_report()

