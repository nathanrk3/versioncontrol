# Nathan King
# COP3502C
# Section 30145
# version control
def encode_password(user_input):
    empty_string = ''
    for x in user_input:
        # add 3, make case of > 7
        empty_string += str((int(x)+3) % 10)
    return empty_string


# Manato Igawa
# decode the encoded password
def decode(data):
    encoded_list = [int(digit) for digit in data]
    decoded_list = [(digit + 7) % 10 for digit in encoded_list]
    decoded_pw = ''.join(map(str, decoded_list))
    return decoded_pw


def main():

    # make while loop
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()  # Manato Igawa

        # make input
        user_choice = input("Please enter an option: ")
        if user_choice == '1':
            non_coded = input("Please enter your password to encode: ")

            # encode the password
            password = encode_password(non_coded)
            print("Your password has been encoded and stored!")
            print()  # Manato Igawa

        #  Manato Igawa
        elif user_choice == '2':
            # decode the encoded password
            print(f'The encoded password is {encode_password(non_coded)}, and the original password is {decode(password)}.')
            print()

        elif user_choice == '3':
            break


if __name__ == "__main__":
    main()
