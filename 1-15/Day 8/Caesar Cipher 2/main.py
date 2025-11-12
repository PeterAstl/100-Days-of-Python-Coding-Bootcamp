alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift *= -1

    for letter in text:
        shifted_position = alphabet.index(letter) + shift
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    if encode_or_decode == "encode":
        print(f"Here is the encoded result: {output_text}")
    else:
        print(f"Here is the decoded result: {output_text}")

caesar(text, shift, encode_or_decode)
