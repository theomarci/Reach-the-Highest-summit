import random
# import matplotlib.pyplot as plt
# import numpy as np

my_dict = {}

num = random.randint(1,9)

def fun(x):
    li = [random.randint(1,100) + random.randint(1,100) - random.randint(1,100) for i in range(100)]
    # ls = []
    # for v in range(len(li)):
    #     ls.append(v)
    # xl = ls
    # yl = np.array(li)
    # plt.plot(xl, yl)
    # plt.show()
    di = {}
    for v in range(len(li)) :
        di[f"{v}"] = li[v]
    max_val = max(di.values())
    key_max = [key for key, val in di.items() if val == max_val]
    print(f"The key of {max_val} is {' '.join(map(str, key_max))}")
    

fun(2)