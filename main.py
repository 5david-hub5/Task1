
def find_new_list():
    print("введите кол-во элементов 1-го списка:")
    n = int(input())
    print("введите значения 1-го списка:")
    list1 = [int(input()) for i in range(n)]
    print("введите кол-во элементов 2-го списка:")
    m = int(input())
    print("введите значения 2-го списка:")
    list2 = [int(input()) for i in range(m)]

    new_list = []
    if len(list1) < len(list2):
        length = len(list1)
    else:
        length = len(list2)

    for i in range(length):
        if list1[i] == list2[i]:
            new_list.append(list1[i])
    return new_list

x=1

print(find_new_list())
