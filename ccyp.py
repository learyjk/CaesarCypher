def encode(msg, num):
    """ Encode msg by + num """
    result = []
    for letter in msg:
        letter = letter.lower()
        result += chr(((ord(letter) - ord('a') + num) % 26) + ord('a'))
        new_str = "".join(result)
    print(f"Encoded Result: {new_str}")


def decode(msg, num):
    """ Decode msg by - num """
    result = []
    for letter in msg:
        letter = letter.lower()
        result += chr(((ord(letter) - ord('a') - num) % 26) + ord('a'))
        new_str = "".join(result)
    print(f"Encoded Result: {new_str}")


if __name__ == "__main__":
    while True:
        action = input("Type \"encode\" or \"decode\": ")
        is_invalid = False

        if not (action == "encode" or action == "decode"):
            print("Invalid Action!")
            is_invalid = True
        if is_invalid:
            continue

        message = input("Type your message: ")
        for letter in message:
            if not letter.isalpha():
                print("Invalid message!")
                is_invalid = True
        if is_invalid:
            continue

        shift_number = input("Type the shift number: ")

        try:
            shift_number = int(shift_number)
        except:
            print("Invalid shift number!")
            is_invalid = True
        if is_invalid:
            continue

        if action == "encode":
            encode(message, shift_number)

        else:
            decode(message, shift_number)
