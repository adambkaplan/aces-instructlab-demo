# This script is a simple greeting program for Abbotts Creek Elementary Students.
# It prompts the user for their name and asks if they are enjoying the career fair.

# Code written with the assistance of GitHub Copilot.

def main():
    print("Hello, Abbotts Creek Elementary!")

    response = input("Are you enjoying the career fair? (yes/no): ")
    if response.lower() == "yes":
        print("That's great to hear!")
    elif response.lower() == "no":
        print("I'm sorry to hear that. I hope it gets better!")
    else:
        print("Thanks for sharing!")

if __name__ == "__main__":
    main()
