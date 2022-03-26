students = ["Vipin", "Veda", "Yatheen", "Pradeep"]


def printIndex(student_name):
    try:
        idx1 = students.index(student_name)
        print(f"List Index of {student_name} is {idx1}")
    except ValueError:
        print(f"{student_name} not found in the list")

printIndex("Yatheen")
printIndex("Rajan")

# ============================================================================

class DivideByZero(Exception):
    def __str__(self):
        return "Divisor cannot be Zero"

class N2IsGreater(Exception):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def __str__(self):
        return f"N1 ({self.n1}) must be greater than N2 ({self.n2})"

def calculate(n1, n2, op):
    if (op == "/"):
        if (n2 == 0):
            raise DivideByZero()
        else:
            return n1 / n2

    if (op == "-"):
        if (n1 < n2):
            raise N2IsGreater(n1, n2)
        else:
            return n1 - n2

def callCalculate(n1, n2, op):
    try:
        print(calculate(n1, n2, op))
    except DivideByZero as dze:
        print("Error: " + str(dze))
    except N2IsGreater as n2g:
        print("Error:" + str(n2g))

callCalculate(100, 10, "/")
callCalculate(90, 0, "/")
callCalculate(60, 40, "-")
callCalculate(50, 70, "-")

# ============================================================================


