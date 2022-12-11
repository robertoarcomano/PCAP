import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(np.__version__)
arr = np.array(
    [
        [
            [1, 2, 3],
            [4, 5, 6]
        ],
        [
            [1, 2, 3],
            [4, 5, 6]
        ]
    ]
)

big = []
# for i in range(100000000):
#     big.append(i)

big_numpy = np.array([])
for i in range(1000):
    np.append(big_numpy,i)