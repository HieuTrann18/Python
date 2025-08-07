
from controllers.student_controller import Student_Controller
from services.student_service import Student_Service
from charts.chart_students import draw_gpa_chart

def menu():
      print("\n===== MENU QUAN LY SINH VIEN =====")
      print("1. Them sinh vien")
      print("2. Hien thi danh sach sinh vien")
      print("3. Loc sinh vien lon hon 22 tuoi")
      print("4. Loc sinh vien co diem tu 80-100 va nho hon 22 tuoi")
      print("5. Hien thi bieu do diem GPA")
      print("6. Thoat")
      print("===================================")


if __name__ == '__main__':
      std_srv = Student_Service()
      std_ctrl = Student_Controller(std_srv)
     

      while True:
            menu()

            choice = input("Nhap lua chon cua ban: ")

            match(choice):
                  case '1':
                        std_ctrl.create_student()
                  case '2':
                        std_ctrl.get_all_student()
                  case '3':
                        std_ctrl.filter_age_student()
                  case '4':
                        std_ctrl.filter_score_student()
                  case '5':
                        students = std_ctrl.get_all_student()
                        draw_gpa_chart(students)
                  case '6':
                        break
                        

  