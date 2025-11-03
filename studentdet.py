class stud:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
 
    def _grades_(self):
        if self.marks>=90:
            grade='A+'
        elif self.marks>=80:
            grade='A'
        elif self.marks>=70:
            grade='B'
        elif self.marks>=60:
            grade='C'
        elif self.marks>=50:
            grade='D'
        else:
            grade='E'
        print(f"Grade:{grade}")
        
    def _display_(self):
        print(f"Student Name: {self.name}")
        print(f"Student roll no: {self.roll_no}")
        print(f"Student mark: {self.marks}")
    

name=input("Enter student name:")
roll_no=input("Enter roll no:")
marks=float(input("Enter marks:"))
student1=stud(name,roll_no,marks)
print("\n---Student Details----")
student1._display_()
student1._grades_()

            
        
        
    