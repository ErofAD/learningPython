'''Найти максимальный и минимальный элемент последовательности [1, -3, -6, 2, 4, 0, -5, 5, 3]'''
def num5():
    my_list = [1, -3, -6, 2, 4, 0, -5, 5, 3]
    print("max = ", max(*my_list))
    print("min = ", min(*my_list))

if __name__ == "__main__":
    num5()