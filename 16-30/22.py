#Найти расстояние между точками в пространстве 2D/3D

def GLenght(num1, num2):
    i = 0
    index = 0
    while i < len(num1):
        index += (num2[i]-num1[i])**2
        i += 1
        return index ** 0.5

print(GLenght([1,1], [-1, 1]))

