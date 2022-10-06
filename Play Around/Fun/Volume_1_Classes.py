


class Employee:
    pass

emp_1 = Employee()

emp_1.firstname = "Shak"
emp_1.lastname = "Simons"
emp_1.email = "s.simons@gmail.com"
emp_1.password = "1234"

emp_2 = Employee()

emp_2.firsname = "Sarah"
emp_2.lastname = "Jane"
emp_2.email = "s.j@gmail.com"
emp_2.password = "Funtimes99"

print('Welcome', emp_1.firstname, emp_1.lastname,'!', 'can you confirm that this is your email address:', emp_1.email, '?')