from datetime import datetime

class Person:
      def __init__(self, firstname, middlename, lastname, birthday, address, phone):
            self.firstname = firstname
            self.middlename = middlename
            self.lastname = lastname
            self.birthday = birthday
            self.address = address
            self.phone = phone

      def get_fullname(self):
        return f"{self.firstname} {self.middlename} {self.lastname}"

      def get_age(self):
        birth = datetime.strptime(self.birthday.strip(), "%d/%m/%Y")
        today = datetime.today()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
      
      def get_info(self):
          return f"Name: {self.get_fullname()}, Age: {self.get_age()}, Birthday: {self.birthday}, Address: {self.address}, Phone: {self.phone}"

      def display_info(self):
        print(f"Name: {self.get_fullname()}")
        print(f"Age: {self.get_age()}")
        print(f"Birthday: {self.birthday}")
        print(f"Address: {self.address}")
        print(f"Phone: {self.phone}")