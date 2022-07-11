from project_euler12_functions import triangle_at_n, test_factors

if  __name__ == '__main__':

    triangles = [triangle_at_n(i) for i in range(20000)]
    for i in triangles:
        if test_factors(i) >=500:
            anwser = i
            break
    print(anwser, triangles.index(anwser))