

if __name__ == "__main__":

    f_array = []

    x = 1

    def my_closure(n):

        def result():
            print('int_closure x: %d, n: %d' % (x, n))
            return x*n*n

        return result

    for i in range(0, 3):
        f_array.append(my_closure(i))

    for i in range(0, 3):
        print(repr(f_array[i]) + '   ' + str(f_array[i]()))

    for i in range(0, 3):
        x += 1
        print(repr(f_array[i]) + '   ' + str(f_array[i]()))
