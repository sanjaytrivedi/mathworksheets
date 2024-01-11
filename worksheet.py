import random
#Author - Sanjay Trivedi

def count_digits(number):
    # Handle the case when the number is 0 separately
    if number == 0:
        return 1
    
    # Initialize a counter for digits
    digit_count = 0
    
    # Iterate until the number becomes 0
    while number != 0:
        # Divide the number by 10 and update it
        number = number // 10
        # Increment the digit count
        digit_count += 1
    return digit_count

def get_padding(count):
    pad = ""
    for _ in range(count): 
        pad = pad+" "
    return pad

def typeStr(type):
    if type == "+":
        return "Addition" 
    
    if type == "-":
        return "Substraction" 

    if type == "x":
        return "Multipication" 

    if type == "/":
        return "Division"

def get_integers_tuple(num_digit, operator):

    if num_digit == "1" and operator == '/':
        return (1, 9) 
        
    if num_digit == "1":
        return (0, 9)   
        
    if num_digit == "2":
        return (1, 99)            
        
    if num_digit == "3":
      return (1,999)

def seperator(num_digit):
    if num_digit == "1":
        return " " 
    if num_digit == "2":
        return "  " 
    if num_digit == "3":
        return "   " 

def answer_space(num_digit):
    if num_digit == "1":
        return "--" 
    if num_digit == "2":
        return "---" 
    if num_digit == "3":
        return "----" 


def generate_worksheet(filename, num_problems, num_digit, operator):

    if ((int)(num_digit) < 1) or ((int)(num_digit) > 3) :
        raise ValueError("Cannot have zero digits or more than 3 digits")
    
    if operator not in ['+','-','x','/'] :
        raise ValueError("invalid operator")

    with open(filename, 'w') as file:
        msg =  str(int(num_digit))+ "-Digit "+typeStr(operator)+" Worksheet\n\n"
        file.write(msg)
        margin = "   "        
        count = (int)(((int)(num_problems))/10)
        rangeNum = get_integers_tuple(num_digit, operator)
        for _ in range(count):
            problem_L1 = " "
            problem_L2 = ""
            problem_L3 = " "
            problem_L4 = ""
            problem_L5 = ""
          
            for _ in range(10):
                num1 = random.randint(rangeNum[0], rangeNum[1])
                num2 = random.randint(rangeNum[0], rangeNum[1])
                num1_pad=""
                num2_pad=""
                
                if operator == '-' :
                    # Ensure the result of subtraction is non-negative
                    num1, num2 = max(num1, num2), min(num1, num2)
                    
                if operator == '/':
                    # Ensure non fractional division
                    num1, num2 = max(num1, num2), min(num1, num2)
                    num1 = ((int)(num1/num2)) * num2
                    
                num1_dg = count_digits(num1)
                num2_dg = count_digits(num2)
                
                
                if num1_dg != num2_dg :
                    if num1_dg > num2_dg :
                        num2_pad = get_padding(num1_dg-num2_dg)
                    else :
                        num1_pad = get_padding(num2_dg-num1_dg)

                problem_L1 = problem_L1 +num1_pad+ f"{num1}"+margin+" "
                problem_L2 = problem_L2 + operator+seperator(num_digit)+margin
                problem_L3 = problem_L3 +num2_pad+ f"{num2}"+margin+" "
                problem_L4 = problem_L4 + answer_space(num_digit)+margin
                problem_L5 = problem_L5 +"   "+seperator(num_digit)+margin
                
                
            problem_L1 = problem_L1 +"\n"
            problem_L2 = problem_L2 +"\n"
            problem_L3 = problem_L3 +"\n"
            problem_L4 = problem_L4 +"\n"
            problem_L5 = problem_L5 +"\n"
                
            file.write(problem_L1)
            file.write(problem_L2)
            file.write(problem_L3)
            file.write(problem_L4)
            file.write(problem_L5)
            file.write(problem_L4)
            file.write("\n") 
          


if __name__ == "__main__":
    worksheet_filename = input("Enter worksheet name: ")
    number_of_problems = input("Enter number of problem: ")
    type = input("Enter type (+, - , x , /): ")
    num_digit = input("Enter num digits: ")

    generate_worksheet(worksheet_filename, number_of_problems,num_digit,type)
    print(f"Worksheet generated and saved to {worksheet_filename}")
    with open(worksheet_filename, 'r') as f:
        content = f.read()
        print(content)  
    
