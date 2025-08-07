from models.Student import Student

def get_sample_students():
      return [
            Student("Nguyen", "Van", "A", "01/01/2000", "123 Street", "0123456789", "REG001", 3.5),
            Student("Tran", "Thi", "B", "02/02/2001", "456 Avenue", "0987654321", "REG002", 3.8),
            Student("Le", "Van", "C", "03/03/2002", "789 Boulevard", "1234567890", "REG003", 3.2),
            Student("Pham", "Thi", "D", "04/04/2003", "321 Road", "0987654321", "REG004", 3.9),
            Student("Hoang", "Van", "E", "05/05/2004", "654 Street", "0123456789", "REG005", 3.6)
      ]