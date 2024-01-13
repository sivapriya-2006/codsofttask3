import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    # Prompt the user to specify the desired length of the password
    try:
        password_length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Check if the password length is at least 6 characters
    if password_length < 6:
        print("Password length must be at least 6 characters.")
        return

    # Generate and display the password
    password = generate_password(password_length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
