from features.Matrix import Matrix
from features.Tuple import Tuple
identity_matrix = Matrix(4,4,
        [[1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1]]
    )

a = Matrix(4,4,
    [[8,2,2,2],
    [3,-1,7,0],
    [7,0,5,4],
    [6,-2,0,5]]
)

b = Matrix(4,4,
        [[1,0,0,0],
        [0,1,0,4],
        [0,0,1,0],
        [0,0,0,1]]
    )

t = Tuple(4,3,2,1)

print(identity_matrix.inverse())
print(a * a.inverse())
print(a.inverse().transpose())
print(a.transpose().inverse())
print((identity_matrix * t).coords)
print((b * t).coords)
print((t * identity_matrix).coords)