numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
flag = "Not Equal"
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:  
            flag = "Equal"  
            break  
print(flag)