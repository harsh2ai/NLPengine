import re

# System Parameters
card_no_pattern_1 = "^4[0-9]{12}(?:[0-9]{3})?"
card_no_pattern_2 = "^(?=.*\d{4}( )\d{4}( )\d{4})(?=.*((0)[0-9])|((1)[0-2])(/)\d{2})(?=.*\d{3})"
cvv_pattern = "^(?=.*[0-9]{3})|(?=.*[0-9]{4})"
expiry_data_pattern = "^(?=.*((0)[0-9])|((1)[0-2])(/)\d{2})"


def isValidCardNo(string):
    # Regex to check valid Visa Card number
    # Check for card_no_pattern_1 first
    # Compile the ReGex
    p1 = re.compile(card_no_pattern_1)

    # If the string is empty return false
    if (string == ''):
        return "The string passed is empty"

    # Pattern class contains matcher() method to find matching between given string and regular expression.
    match1 = re.match(p1, string)

    # Return True if the string
    # matched the ReGex

    if match1 is None:
        # Check if card_no_pattern_2 exists or not
        p2 = re.compile(card_no_pattern_2)
        match2 = re.match(p2, string)
        if match2 is None:
            print("Card details not present")
            return None
        else:
            # value = re.search(card_no_pattern_2, string)
            print("Card details present")
            return True
    else:
        print("Card details present")
        # value = re.search(card_no_pattern_1, string)
        return True


def isCVVorOTP(string):
    # function to define validation of the card
    check_cvv = re.compile(cvv_pattern)
    if (re.match(check_cvv, string)):

        print("Detected cvv/otp")
        return True

    else:
        print("CVV/OTP not passed")
        return False


def isExpiryDate(string):
    # function to define validation of the card
    check_ex_date = re.compile(expiry_data_pattern)

    if (re.match(check_ex_date, string)):
        print("Detected expiry date")
        return True

    else:
        print("Expiry date not passed")
        return None


if __name__ == "__main__":
    text = "My credit card number is 1111 2222 3333, the cvv is 123 and the expiry date is 03/21."
    print(text)
    isValidCardNo(text)
    isCVVorOTP(text)
    isExpiryDate(text)
