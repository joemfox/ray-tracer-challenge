from features.Tuple import Tuple
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