#Creating input for number of EC2 isntanes#
ec2_instances = int(input ('How many unique EC2 instance names do you want? '))

#Creating input for department name#
department_name = input ('What is the name of your department?')

#creating variable to assign random numbers#
import random

def assign_random_number():
    random_number = random.randint(1, 100)  # Generates a random number between 1 and 100
    
    return f"{department_name} {random_number}" #create a human-readable string instead of a tuple

# Example of generating multiple outputs with random numbers
for _ in range(ec2_instances):  
    print(assign_random_number())

