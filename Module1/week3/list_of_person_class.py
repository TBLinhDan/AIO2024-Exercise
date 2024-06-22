'''
Một Ward (phường) gồm có name (string) và danh sách của mọi người trong Ward.
- Một người person có thể là student, doctor, hoặc teacher. Một student gồm có name, yob (int) (năm sinh), và grade (string). 
- Một teacher gồm có name, yob, và subject (string). 
- Một doctor gồm có name, yob, và specialist (string). 
Lưu ý cần sử dụng a list để chứa danh sách của mọi người trong Ward.

(a) Cài đặt các class Student, Doctor, và Teacher theo mô tả trên. 
    Thực hiện phương thức describe() method để in ra tất cả thông tin của các object.
(b) Viết add_person(person) method trong Ward class để add thêm một người mới với nghề
    nghiệp bất kỳ (student, teacher, doctor) vào danh sách người của ward. 
    Tạo ra một ward object, và thêm vào 1 student, 2 teacher, và 2 doctor. 
    Thực hiện describe() method để in ra tên ward (name) và toàn bộ thông tin của từng người trong ward.
(c) Viết count_doctor() method để đếm số lượng doctor trong ward.
(d) Viết sort_age() method để sort mọi người trong ward theo tuổi của họ với thứ tự tăng dần.
    (hint: Có thể sử dụng sort của list hoặc viết thêm function đều được)
(e) Viết compute_average() method để tính trung bình năm sinh của các teachers trong ward.
'''

class Person:
    def __init__(self, name:str, yob:int):
        self._name = name
        self._yob = yob

    def get_name(self):
        return self._name
    def get_yob(self):
        return self._yob
    def describe(self):
        return f"Name: {self._name}, yoB: {self._yob}"

class Student(Person): 
    def __init__(self, name:str, yob:int, grade:int):
        super().__init__(name, yob)
        self._grade = grade
    
    def get_name(self):
        return super().get_name()
    def get_yob(self):
        return super().get_yob()
    def get_grade(self):
        return self._grade

    def describe(self):
        student = super().describe()
        print(f"Student - {student} - Grade: {self._grade}")

class Teacher(Person):
    def __init__(self, name:str, yob:int, subject:str):
        super().__init__(name, yob)
        self._subject = subject
    
    def get_name(self):
        return super().get_name()
    def get_yob(self):
        return super().get_yob()
    def get_subject(self):
        return self._subject
        
    def describe(self):
        teacher = super().describe()
        print(f"Teacher - {teacher} - Subject: {self._subject}")

class Doctor(Person):
    def __init__(self, name:str, yob:int, specialist:str):
        super().__init__(name, yob)
        self._specialist = specialist
        
    def get_name(self):
        return super().get_name()
    def get_yob(self):
        return super().get_yob()
    def get_specialist(self):
        return self._specialist
    
    def describe(self):
        doctor = super().describe()
        print(f"Doctor - {doctor} - Specialist: {self._specialist}")

class Ward:
    def __init__(self, name:str):
        self.__name = name
        self.__list_person = []
    
    def add_person(self, person:Person):
        self.__list_person.append(person)
    
    def describe(self):
        print(f"Ward Name: {self.__name}")
        for person in self.__list_person:
            person.describe()

    def count_doctor(self):
        count = 0
        # duyệt qua list person, xem person nào có kiểu dữ liệu Doctor thì đếm
        for person in self.__list_person:
            if isinstance(person, Doctor):
                count += 1
        return count

    def count_teacher(self):
        count = 0
        for person in self.__list_person:
            if isinstance(person, Teacher):
                count += 1
        return count

    def sort_age(self):
        self.__list_person.sort(key=lambda x: x.get_yob())
    
    # tính trung bình năm sinh của các Teacher có trong List
    def compute_average_age(self, count_teacher):
        self.count_teacher = count_teacher
        total_age = 0
        for person in self.__list_person:
            if isinstance(person, Teacher):
                total_age += person.get_yob()
                average_age = total_age / self.count_teacher
        return average_age
    
student1 = Student(name = "studentA", yob = 2010, grade = "7")
teacher1 = Teacher(name = "teacherA", yob = 1969, subject = "Math")
teacher2 = Teacher(name ="teacherB", yob =1995, subject = "History")
doctor1 = Doctor(name = "doctorA", yob = 2045, specialist = "Endocrinologists")
doctor2 = Doctor(name = "doctorB", yob = 1975, specialist = "Cardiologists")
ward1 = Ward(name = "Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
assert ward1.count_doctor() == 1
ward1.add_person(doctor2)
ward1.describe()
count_doctor = ward1.count_doctor()
print(f"\nNumber of Doctor: {count_doctor}\n")
print("Sort people in ward by their age in ascending order:\n")
ward1.sort_age()
ward1.describe()
print("\nCalculate the average year of birth of the Teachers in the ward:")
count_teacher = ward1.count_teacher()
print(f"\nNumber of Teacher: {count_doctor}")
average_age = ward1.compute_average_age(count_teacher)
print(f"Average year of birth: {average_age}")

'''
Ward Name: Ward1
Student - Name: studentA, yoB: 2010 - Grade: 7
Teacher - Name: teacherA, yoB: 1969 - Subject: Math
Teacher - Name: teacherB, yoB: 1995 - Subject: History
Doctor - Name: doctorA, yoB: 2045 - Specialist: Endocrinologists
Doctor - Name: doctorB, yoB: 1975 - Specialist: Cardiologists   

Number of Doctor: 2

Sort people in ward by their age in ascending order:

Ward Name: Ward1
Teacher - Name: teacherA, yoB: 1969 - Subject: Math
Doctor - Name: doctorB, yoB: 1975 - Specialist: Cardiologists
Teacher - Name: teacherB, yoB: 1995 - Subject: History
Student - Name: studentA, yoB: 2010 - Grade: 7
Doctor - Name: doctorA, yoB: 2045 - Specialist: Endocrinologists

Calculate the average year of birth of the Teachers in the ward:

Number of Teacher: 2
Average year of birth: 1982.0
'''