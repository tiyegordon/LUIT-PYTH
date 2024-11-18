import random  # Importing random library at the top of the script

# Create input for number of EC2 instances
ec2_instance = int(input('How many unique EC2 instance names do you want? '))

def get_department_name(): #loop function
    valid_department_names = ['Accounting', 'Marketing', 'FinOps'] #an array of strings for comparison with department_name variable. This was more effeceint than assigning each string to a variable.

    # Create input for department name using while/if/else statement 
    while True:
        department_name = input('What is the name of your department? ')

        # Check if the department name is valid
        if department_name in valid_department_names:
            # Function to assign a random number
            def assign_random_number():
                return random.randint(1, 100)  # Generates a random number between 1 and 100
            
            # Generate multiple EC2 instance names with random numbers
            for _ in range(ec2_instance):
                random_number = assign_random_number()  # Get a random number
                print(f"{department_name}-{random_number}")  # f-string with brakcets for embeding Python expressions directly inside a string.

            break  # Stops the loop if the department name is correct/statement is true

        else: #directive if statment is falsel will continue in loop, no program exit
            print('You are prohibited from using the Name Generator.\nIf you have received this message in error, please try again.\nRemember the system is case sensitive.')

get_department_name() #close function
