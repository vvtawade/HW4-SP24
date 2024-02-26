import numpy as np
from numpy.linalg import solve, inv


def matrix_solver(A, b):

    """
    Function to solve linear matrix system

    :param A: Matrix A
    :param b: Matrix B

    :return: Answer to linear matrix system
    """

    answer = solve(A, b)  # Solves the linear matrix system using solve function
    checkit1 = np.matmul(A, answer)  # Matrix product of A and answer
    checkit2 = np.dot(A, answer)  # Dot product of A and answer

    I = inv(A)  # Inverse matrix of matrix A
    checkit3 = np.matmul(I, b)  # Matrix product of inverse matrix A and b

    # Checks if checkit1 = checkit2
    if not np.allclose(checkit1, checkit2, atol=1e-8):
        print("Check 1 does not equal Check 2")
    # Checks if answer = checkit3
    elif not np.allclose(answer, checkit3, atol=1e-8):
        print("Answer does not equal Check 3")
    else:
        return answer
        # Returns answer if all checks are good


def print_equations(matrix_A, vector_b):

    """
    Function to print the matrices in a formatted way

    :param matrix_A: Matrix A
    :param vector_b: Matrix B

    :return: Formatted matrices
    """

    for i in range(len(matrix_A)):
        equation = " ".join(map(str, matrix_A[i]))
        print(f"[{equation}] [x{i + 1}] = [{vector_b[i]}]")


# Main function
def main():
    # Question 1
    A = [[3, 1, -1],
         [1, 4, 1],
         [2, 1, 2]]
    b = [2, 12, 10]

    print("For the following Linear System:")
    print_equations(A, b)  # Runs print_equation to format matrix A and b
    print()
    print("The Solution is: ")

    # Prints the solution
    answer = matrix_solver(A, b)
    print("x1 = ", round(answer[0], 3))
    print("x2 = ", round(answer[1], 3))
    print("x3 = ", round(answer[2], 3))
    print()

    # Question 2
    A = [[1, -10, 2, 4],
         [3, 1, 4, 12],
         [9, 2, 3, 4],
         [-1, 2, 7, 3]]
    b = [2, 12, 21, 37]

    print("For the following Linear System:")
    print_equations(A, b)  # Runs print_equation to format matrix A and b
    print()
    print("The Solution is: ")

    # Prints the solution
    answer = matrix_solver(A, b)
    print("x1 = ", round(answer[0], 3))
    print("x2 = ", round(answer[1], 3))
    print("x3 = ", round(answer[2], 3))
    print("x4 = ", round(answer[3], 3))


# Runs main function
main()
