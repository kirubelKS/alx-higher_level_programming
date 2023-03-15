#!bin/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
        a function that returns the square value of all elements in a multi dimentional list been passed as arguments.
        Returns a new matrix that is of the same size as the size of the matrix pased to it as arguments.
        You are allowed to use regular loops, maps, etc
    '''
    new_list = []
    if len(matrix) == 0:
        return new_list
    
    new_list = [[i*i for i in j]for j in matrix]
    return new_list