def saddle_points(matrix):
    #Validate matrix
    if any(len(row) != len(matrix[0]) for row in matrix): raise ValueError("The supplied matrix is invalid.")
    
    #search for saddle points
    rows, cols = matrix, list(zip(*matrix))
    return [ 
            {"row": x+1, "column": y+1} 
            for x, row in enumerate(matrix) 
            for y, value in enumerate(row) 
            if max(rows[x]) == min(cols[y]) 
            ]
