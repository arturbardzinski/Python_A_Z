class Student:

  lista_studentow = []

  def __init__(self,imie, nazwisko, wiek):
    self.imie = imie
    self.nazwisko = nazwisko
    self.wiek = wiek
    self.lista_studentow.append(self)

  @staticmethod
  def liczba_studentow():
      print('Liczba studentów to: ',len(Student.lista_studentow))

student_1 = Student('Artur', 'Bardzinski', 38)
student_2 = Student('Magdalena', 'Krok', 37)

Student.liczba_studentow()
