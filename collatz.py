# Weekly Task 4 of 'Programming & Scripting'.
# Author: Mark Gallagher

def calculate_successive_values(n):
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)  # Print the final value of 1


def main():
    while True:
        try:
            num = int(input("Enter a positive integer: "))
            if num <= 0:
                raise ValueError("Please enter a positive integer.")
            calculate_successive_values(num)
            break
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    main()