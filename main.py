import os
import sqlite3

# حقوق المطور تظهر في الواجهة
DEV_INFO = "تطوير المطور: أسد محمد العامري"

def menu():
    while True:
        # مسح الشاشة لجعل المنظر احترافياً
        os.system('clear')
        print("="*40)
        print(f"   نظام الحضور المدرسي الذكي")
        print(f"   {DEV_INFO}")
        print("="*40)
        print("1. إضافة طالب جديد")
        print("2. بدء رصد الحضور والغياب")
        print("3. عرض تقارير الحضور")
        print("4. إصلاح النظام / تحديث (عن بُعد)")
        print("5. خروج")
        print("="*40)
        
        choice = input("اختر رقم العملية: ")

        if choice == '1':
            os.system('python add_students.py')
        elif choice == '2':
            os.system('python take_attendance.py')
        elif choice == '3':
            os.system('python reports.py')
        elif choice == '4':
            print("\n🔍 جاري الفحص عن بعد...")
            # هنا سنضع أمر التحديث لاحقاً
            print("النظام يعمل بأحدث إصدار حالياً.")
            input("\nاضغط Enter للعودة...")
        elif choice == '5':
            print("وداعاً!")
            break
        else:
            print("اختيار خاطئ، حاول مرة أخرى.")
            input()

if __name__ == "__main__":
    menu()

