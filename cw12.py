#Function 1,2,3
numbers=input().split(',')

def get_length_of_list(numbers):
    return len(numbers)

def calculate_average(numbers):
    sum=0
    for i in numbers:
        sum+=int(i)
    return sum/get_length_of_list(numbers)

average = calculate_average(numbers)
length = get_length_of_list(numbers) 
print("Length of the list:", length) 
print("Average of the list:", average)

