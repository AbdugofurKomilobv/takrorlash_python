



# juft yoki toq soni aniqlash
# a = int(input('a: '))


# if a % 2 == 0:
#     print('juft son')
# else:
#     print('toq')

# ===========================================================
# a = int(input('a: '))
# b = int(input('b: '))

# x = a >=0 or b <-2
# print(x)

# ===========================================================
# bittasi yoki 2lasi toq son bolishi kere
# a = int(input('a: '))
# b = int(input('b: '))

# x = a % 2 == 1 or b % 2 == 1

# print(x)


# =================================================================
# 2 lasixam juft yoki toq bolishi kere
# a = int(input('a: '))
# b = int(input('b: '))

# x = a % 2 == 0 and b % 2 == 0 or a % 2 == 1 and b % 2 == 1
# print(x)
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("⬜", end=" ")
        else:
            print("⬛", end=" ")
    print()
