a=input().split(',')

def fanck_1(x):
    sum=0
    for i in x:
        sum+=int(i)
    return sum/len(x)
print(fanck_1(a))
     
#Function 3

def get_length_of_list(numbers):
    return len(numbers)

def calculate_average(numbers):
    if not numbers:  
        return 0
    total = sum(numbers)  
    length = get_length_of_list(numbers)  
    average = total / length  
    return average

numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("Average of the list:", average)
# Function 2
def get_length_of_list(numbers):
    return len(numbers)

numbers = [1, 2, 3, 4, 5]
length = get_length_of_list(numbers)
print("Length of the list:", length)
