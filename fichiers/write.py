

student_list = ["Otman","Jack","Jones","Jane","Jade"]

with open("students.txt","a+") as file:
    for student in student_list:
      file.write(student + "\n") 
    file.close()