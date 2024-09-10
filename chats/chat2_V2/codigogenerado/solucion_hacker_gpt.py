def decode_name(name, shift):
    decoded_name = ""
    for letter in name:
        if letter.isalpha():
            if letter.islower():
                decoded_letter = chr(((ord(letter) - ord('a') + shift) % 26) + ord('a'))
            else:
                decoded_letter = chr(((ord(letter) - ord('A') + shift) % 26) + ord('A'))
        else:
            decoded_letter = letter
        decoded_name += decoded_letter
    return decoded_name

def decode_phone_number(phone_number):
    binary_string = phone_number.split()[0]
    decoded_number = ""
    for i in range(0, len(binary_string), 7):
        binary_digit = binary_string[i:i+7]
        decimal_digit = int(binary_digit, 2)
        decoded_number += str(decimal_digit)
    return decoded_number

def decode_entry(shift, entry):
    name, phone_number = entry.split()
    decoded_name = decode_name(name, shift)
    decoded_phone_number = decode_phone_number(phone_number)
    return decoded_name + " " + decoded_phone_number

def main():
    p = int(input())
    entry = input().strip()
    print(decode_entry(p, entry))

if __name__ == "__main__":
    main()
