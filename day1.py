def main():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]

    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)

    new_list = []

    for i in range(len(sorted_list1)):
        number = abs(sorted_list1[i] - sorted_list2[i])
        new_list.append(number)

    print(sum(new_list))


if __name__ == "__main__":
    main()
