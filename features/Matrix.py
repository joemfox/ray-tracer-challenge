from features.Tuple import Tuple
from features.util import equals
class Matrix(list):
    def __init__(self, w, h, m=None):
        if(not m):
            self += [[0 for i in range(w)] for j in range(h)]

        else:
            assert len(m) == h, f"Matrix instantiated with {h} rows, data has {len(m)}"
            for x in range(len(m)):
                assert len(m[x]) == w, f"Matrix instantiated with {w} rows, data has {len(m)[0]}"
            self += m

    def size(self):
        return [len(self),len(self[0])]

    size = property(size)

    def __eq__(self,other):
        eq_flag = True
        if not isinstance(other,list):
            return False

        if len(self) != len(other):
            return False
        for row in range(self.size[0]):
            if not isinstance(other[row],list):
                return False
            if len(self[row]) != len(other[row]):
                return False
            for col in range(self.size[1]):
                if not equals(self[row][col], other[row][col]):
                    eq_flag == False
        return eq_flag

    def __mul__(self, other):
        if isinstance(other,Matrix):
            a = self
            b = other

            v = [[sum(i*j for i,j in zip(a_row,b_col)) for b_col in zip(*b)] for a_row in a]
            
            return Matrix(max(a.size[0],b.size[0]),max(a.size[1],b.size[1]),v)
        elif isinstance(other, Tuple):
            a = self
            b = other
            v = [sum(i*j for i,j in zip(a_row,b.coords)) for a_row in a]
            return Tuple(*v)

    def transpose(self):
        a = Matrix(*self.size)

        for y in range(self.size[0]):
            for x in range(self.size[1]):
                a[x][y] = self[y][x]

        return a

    def determinant(self):
        if(self.size == [2,2]):
            return (self[0][0] * self[1][1]) - (self[0][1] * self[1][0])
        else:
            return sum([self[0][j] * self.cofactor(0,j) for j in range(self.size[1])])

    determinant = property(determinant)

    def submatrix(self,row,col):
        a = [row.copy() for row in self]
        for r in a:
            del r[col]
        del a[row]
        return Matrix(len(a),len(a[0]),a)
    
    def minor(self,row,col):
        sub = self.submatrix(row,col)
        return sub.determinant

    def cofactor(self,row,col):
        minor = self.minor(row,col)
        if (row+col) % 2 != 0:
            minor *= -1
        return minor

    def is_invertible(self):
        if self.determinant == 0:
            return False
        else: return True

    is_invertible = property(is_invertible)

    def inverse(self):
        assert self.is_invertible, "Matrix is not invertible"
        a = Matrix(*self.size)
        for row in range(len(a)):
            for col in range(len(a[0])):
                c = self.cofactor(row,col)
                a[col][row] = c/self.determinant
        return a