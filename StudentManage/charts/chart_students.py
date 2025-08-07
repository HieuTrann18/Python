import matplotlib.pyplot as plt

def draw_gpa_chart(students):
      names = [s.get_fullname() for s in students]
      gpa = [s.gpa for s in students]
      plt.figure(figsize=(10, 6))
      plt.bar(names, gpa, color='skyblue')
      plt.xlabel('Ten sinh vien')
      plt.ylabel('Diem GPA')
      plt.title('Bieu do diem GPA cua sinh vien')
      plt.ylim(0, 4)
      plt.tight_layout()
      plt.show()