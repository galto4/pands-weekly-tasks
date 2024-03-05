# Weekly Task 3 of 'Programming & Scripting'.
# A program that reads a 10 character account number and outputs the account number with only the last 4 digits showing
# Author: Mark Gallagher

# Part 1 - Verify that the account number is 10 digits

def mask_account_number(account_number):
    if len(account_number) != 10:
        return "Invalid account number. It should be exactly 10 characters long."
    
    masked_number = "X" * 6 + account_number[-4:]
    return masked_number

# Part 2 - Input Account Number

def main():
    account_number = input("Enter your 10-character account number: ")
    masked_account_number = mask_account_number(account_number)
    print("Masked account number:", masked_account_number)

if __name__ == "__main__":
    main()