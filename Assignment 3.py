def calculate_student_grade():
    print("\n=== 1. Student Grade Calculator ===")
    try:
        # Input marks for 5 subjects
        print("Enter the marks obtained in 5 subjects (out of 100 each):")
        sub1 = float(input("Subject 1: "))
        sub2 = float(input("Subject 2: "))
        sub3 = float(input("Subject 3: "))
        sub4 = float(input("Subject 4: "))
        sub5 = float(input("Subject 5: "))

        # Calculate total and percentage
        total_marks = sub1 + sub2 + sub3 + sub4 + sub5
        percentage = (total_marks / 500) * 100

        # Conditional logic to determine the grade
        if percentage >= 60:
            grade = 'A'
        elif percentage >= 50:
            grade = 'B'
        elif percentage >= 40:
            grade = 'C'
        elif percentage >= 33:
            grade = 'D'
        else:
            grade = 'Fail'

        # Display results neatly
        print("-" * 30)
        print(f"Total Marks: {total_marks:.1f} / 500")
        print(f"Percentage:  {percentage:.2f}%")
        print(f"Final Grade: {grade}")
        print("-" * 30)
    except ValueError:
        print("Error: Please enter valid numerical values for marks.")


def generate_multiplication_table():
    print("\n=== 2. Multiplication Table Generator ===")
    try:
        num = int(input("Enter a number between 2 and 50: "))
        
        # Validation range check
        if num < 2 or num > 50:
            print("Notice: The number is outside the required range (2 to 50).")
        else:
            print(f"\nMultiplication Table for {num}:")
            print("-" * 20)
            for i in range(1, 11):
                # The :2d alignment ensures columns line up beautifully
                print(f"{num} x {i:2d} = {num * i}")
            print("-" * 20)
    except ValueError:
        print("Error: Please enter a valid integer.")


def check_palindrome_number():
    print("\n=== 3. Palindrome Number Checker ===")
    try:
        user_input = input("Enter an integer to check: ")
        original_num = int(user_input)
        
        # We only perform mathematical reversal on non-negative integers
        if original_num < 0:
            print("Negative numbers are not palindromes due to the minus sign.")
            return

        # Step 1: Find the reverse of the given number mathematically
        temp = original_num
        reverse_num = 0
        
        while temp > 0:
            remainder = temp % 10
            reverse_num = (reverse_num * 10) + remainder
            temp = temp // 10

        # Step 2 & 3: Compare and print the results
        print("-" * 30)
        print(f"Original Number: {original_num}")
        print(f"Reverse Number:  {reverse_num}")
        print("-" * 30)

        if original_num == reverse_num:
            print("Result: It is a Palindrome Number.")
        else:
            print("Result: It is NOT a Palindrome Number.")
    except ValueError:
        print("Error: Please enter a valid integer.")


def main():
    while True:
        print("\n================ MAIN MENU ================")
        print("1. Calculate Student Grade")
        print("2. Generate Multiplication Table (Range 2-50)")
        print("3. Check Palindrome Number")
        print("4. Exit Program")
        print("===========================================")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            calculate_student_grade()
        elif choice == '2':
            generate_multiplication_table()
        elif choice == '3':
            check_palindrome_number()
        elif choice == '4':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a number from 1 to 4.")


if __name__ == "__main__":
    main()

