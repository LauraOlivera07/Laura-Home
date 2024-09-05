"""
You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n.
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.

"""

def generate_coordinates(x_range, y_range, z_range, n):
    return [[i, j, k] for i in x_range for j in y_range for k in z_range if i + j + k != n]

x = range(int(input())+1)
y = range(int(input())+1)
z = range(int(input())+1)
n = int(input())

result = generate_coordinates(x, y, z, n)
print(result)
