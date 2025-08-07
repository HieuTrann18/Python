from data.sample_students import get_sample_students

class Student_Service:
      def __init__(self):
            self.students = get_sample_students()

      def create_student(self, student):
            self.students.append(student)

      def display_all_student(self):
            return self.students
      
      def filter_age_student(self, ageFilter):
            result = list(filter(lambda s: s.get_age() > ageFilter, self.students ))
            return result

      def filter_score_student(self, minScore, maxScore):
            result = list(filter(lambda s: minScore <= s.gpa <= maxScore, self.students))
            return result
      
      def write_students_to_file(self, student, file_name='students.txt'):
            data = [
                  student.get_fullname().replace(" ", ""),
                  str(student.get_age()),
                  student.birthday,
                  student.address,
                  student.phone
            ]
            line = ":".join(data)
            try:
                  with open(file_name, "a", encoding='utf-8') as f:
                        f.write(line + '\n')
                  print('Ghi file thanh cong')      
            except Exception as e:
                  print('Loi ghi file: ', e)
