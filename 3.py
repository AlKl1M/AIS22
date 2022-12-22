x = 38
for i in range(1, x):
    for k in range(0, x):
        for l in range(0, x):
            for m in range(0, x):
                if 3**k * 5**l * 7**m == i:
                    print(i)