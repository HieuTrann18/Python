
from models.Student import Student

class Student_Controller:
      def __init__(self, student_service):
            self.student_service = student_service

      
      def create_student(self):
            firstname = input('Nhap ten: ')
            middlename = input('Nhap ten dem: ')
            lastname = input('Nhap ho: ')
            birthday = input('Nhap ngay sinh (dd/mm/yyyy): ')
            address = input('Nhap đia chi: ')
            phone = input('Nhap sdt: ')
            regno = input('Nhap so dang ky (regno): ')
            gpa = float(input('Nhap điem GPA: '))

            new_student = Student(firstname,middlename,lastname,birthday,address,phone,regno,gpa)

            self.student_service.create_student(new_student)
            self.student_service.write_students_to_file(new_student)

            print(f'Them sinh vien {firstname} {middlename} {lastname} thanh cong!\n')
            new_student.display_info()
      
      def get_all_student(self):
            results = self.student_service.display_all_student()
            if not results:
                  print('Khong co sinh vien nao')
            else:
                  print('===Danh sach sinh vien===')
                  for s in results:
                        s.display_info()
                  print('=========================')

      def filter_age_student(self):
            result = self.student_service.filter_age_student()
            if not result:
                  print("Khong co sinh vien nao lon hon 22 tuoi")
            else:
                  print("===== Danh sach sinh vien co tuoi lon hon 22 =====")
                  for s in result:
                        s.display_info()
                        print("-------------")
                  print("==================================================")

      def filter_score_student(self):
            minScore = float(input('Nhap diem toi thieu: '))
            maxScore = float(input('Nhap diem toi da: '))
            
            if minScore > maxScore:
                  print("Diem toi thieu phai nho hon diem toi da!")
                  return
                  

            result = self.student_service.filter_score_student(minScore, maxScore)
            if not result:
                  print(f"Khong co sinh vien nao co diem trong khoang {minScore} toi {maxScore}")
            else:
                  print(f"===== Danh sach sinh vien co diem trong khoang {minScore} toi {maxScore} =====")
                  for s in result:
                        s.display_info()
                        print("-------------")
                  print("==================================================")


