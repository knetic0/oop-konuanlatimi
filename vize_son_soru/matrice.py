class Matrices:
    def __init__(self, row_size, col_size):
        self.row_size = row_size
        self.col_size = col_size
        self.matrice = []
        for index in range(self.row_size):
            temp_matrice = []
            for j_index in range(self.col_size):
                temp_matrice.append(index * j_index)
            self.matrice.append(temp_matrice)
            
    def __add__(self, other):
        add_result = []
        for index in range(self.row_size):
            for j_index in range(self.col_size):
                add_result.append(self.matrice[index][j_index] + other.matrice[index][j_index])
        return f"Answer of Add : {add_result}"
    
    def __mul__(self, other):
        mul_result = []
        for index in range(self.row_size):
            temp_result = []
            for j_index in range(self.col_size):
                temp_result.append(0)
            mul_result.append(temp_result)
        
        for index in range(len(self.matrice)):
            for j_index in range(len(other.matrice[0])):
                for k_index in range(len(other.matrice)):
                    mul_result[index][j_index] += self.matrice[index][k_index] * other.matrice[k_index][j_index]
        return f"Answer of Multiple : {mul_result}"
    
    def __len__(self):
        return len(self.matrice)
            
    def __repr__(self):
        return f"First Matrice : {self.matrice}"