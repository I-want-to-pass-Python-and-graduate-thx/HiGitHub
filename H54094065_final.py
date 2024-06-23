def parse_matrix(input_str):
    """Parses the input string to create a matrix stored in a dictionary."""
    rows = input_str.split('|') #assure the different row split into different strings
    matrix = {} #start with an empty dictionary
    for i, row in enumerate(rows):
        elements = list(map(int, row.split(','))) #split the elements by ,
        for j, elem in enumerate(elements):
            matrix[(i, j)] = elem
    return matrix

def multiply_matrices(U, V, n):
    """Multiplies two matrices U and V."""
    M = {} #start with an empty dictionary
    for i in range(n):
        for j in range(n):
            M[(i, j)] = sum(U[(i, k)] * V[(k, j)] for k in range(n))
    return M

def print_matrix(M, n):
    """Prints the matrix M in the desired format."""
    for i in range(n):
        row = [M[(i, j)] for j in range(n)]
        print(row)

def main():
    # Input matrices
    U_str = input("Enter matrix U: ")
    V_str = input("Enter matrix V: ")
    
    # Determine matrix size
    n = len(U_str.split('|'))
    
    # Parse matrices
    U = parse_matrix(U_str)
    V = parse_matrix(V_str)
    
    # Multiply matrices
    M = multiply_matrices(U, V, n)
    
    # Print the result
    print("M = U x V")
    print_matrix(M, n)

if __name__ == "__main__":
    main()
