class EquationSolver:
    @staticmethod
    def solve_monomial():
        a = int(input("Enter coefficient a: "))
        b = int(input("Enter coefficient b: "))
        c = int(input("Enter constant c: "))
        result = (c + 2 * b) / a
        return result

    @staticmethod
    def solve_polynomial():
        a = int(input("Enter coefficient a: "))
        b = int(input("Enter coefficient b: "))
        c = int(input("Enter constant c: "))
        result = (c ** 2 - 2 * b) / a
        return result

if __name__ == '__main__':
    print("Solving Monomial Equation")
    monomial_result = EquationSolver.solve_monomial()
    print(f"The solution is: {monomial_result}")

    print("Solving Polynomial Equation")
    polynomial_result = EquationSolver.solve_polynomial()
    print(f"The solution is: {polynomial_result}")
