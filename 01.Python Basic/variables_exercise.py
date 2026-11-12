employee_id = 101
employee_name= "badri"
emeployee_age= 25
department ='QA'
salary= 20000
is_active= True
company_name='TT'
print(employee_id)
print(employee_name)
print(emeployee_age)
print(department)
print(salary)
print(is_active)
print(company_name)
print(type(is_active))
#============================================================
#Normally, print() moves to a new line,You can change that behavior
print("hello",end=" ")
print("python")

print("Badri", "QA", 25000,sep=" |")
#===========================================================
#input() allows the user to enter information.
name = input("Enter your name: ")
department = input("Enter your department: ")
badri_salary=input("Enter your salary: ")
badri_salary=int(badri_salary) # if you dont  do this types conversion the 25k is string 
#badri_salary=int(input("Enter your salary: ")) user enter 25k then input() ,its "25",int(),25
print("Name:", name)
print(department)

print(badri_salary+5000)
print(type(badri_salary))
#============================================================
# Python — f-strings
name="satish"
age="25"
print(f"i am {name} my age is {age}")

print(f"Employee name is{employee_name} his salary is {salary}")
#You can also put expressions inside {}
print(f"Next year I will be {emeployee_age + 1}.")