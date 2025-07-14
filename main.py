from user_data_generator import generate_user_data
from form_filler import automate_gmail_signup
from validation import validate_response

def main():
    user_data = generate_user_data()
    print(f"Generated User Data: {user_data}")
    result = automate_gmail_signup(user_data)
    validate_response(result)

if __name__ == "__main__":
    main()
