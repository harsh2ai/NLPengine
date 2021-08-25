from PIIDetection.common.get_card_details import *

PII_map = {'isCVVorOTP': 'cvv/otp_detected'}


class PIIDetection():

    def is_text_numeric(self, text):
        return text.isdigit()

    def is_text_alphanumeric(self, text):
        return text.isalnum()

    def detect_pii(self, text):

        pii_result = []
        # Check if Text is a Numeric Value
        if PIIDetection.is_text_numeric:

            # Check for OTP
            if isCVVorOTP(text):
                pii_result.append(PII_map[isCVVorOTP.__name__])

        elif PIIDetection.is_text_alphanumeric(text):
            print("alphanum detected")

        else:
            print("No PII Detected")
        return pii_result

if __name__=='__main__':
    pii_model = PIIDetection()
    print(pii_model.detect_pii('123'))
