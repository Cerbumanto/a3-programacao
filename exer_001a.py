# Python Exercise
# Arithmetic average

# Develop a program that reads a student's grades, calculates and display his average.

#Escreva um programa python que solicita as 3
#notas de um aluno, calcula a média e informa se o aluno passou ou
#ficou em recuperação (a média para passar é 7)

n1 = float(input('First grade of the student: '))
n2 = float(input('Second grade of the student: '))
n3 = float(input('Third grade of the student: '))
average = (n1 + n2 + n3) / 3
if average >= 7:
    print("The student passed with the average "+str(average))
else:
    print("The student was not passed with the average "+str(average))