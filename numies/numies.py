def find_largest_smallest():
    largest = None
    smallest = None
    list_sqrs = []
    sum_nums = 0
    count = 0

    while True:
        user_input = input("Enter a number or (done): ")
        if user_input.lower() == 'done':
            print("\n")
            break
        try:
            
            num = int(user_input)
        except ValueError:
            print("Invalid input")
            continue

        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num

        sum_nums += num
        list_sqrs.append(num ** 2)

        if num % 2 == 0:
            count += 1


    print(f"Maximum is {largest}", )
    print(f"Minimum is {smallest}")
    print(f"Sum: {sum_nums}")
    print(f"{sorted(list_sqrs)}")
    print(f"Even numbers: {count}")


find_largest_smallest()
