from models.Person import Person

class Student(Person):
      def __init__(self, firstname, middlename, lastname, birthday, address, phone, regno, gpa):
        super().__init__(firstname, middlename, lastname, birthday, address, phone)
        self.regno = regno
        self.gpa = float(gpa)

      def display_info(self):
        print(f"Registration No: {self.regno}")
        super().display_info()
        print(f"GPA: {self.gpa}")
      