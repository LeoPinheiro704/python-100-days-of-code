from caesar_cipher import logo, alphabet

end_decoding = False

def caesar(text, shift, direction):
  encoded = ''
  if direction == 'decode':
    shift *= -1
  for char in text:
    if char not in alphabet:
      encoded += char
    else:
      position = alphabet.index(char)
      new_position = (position + shift) % 26
      encoded += alphabet[new_position]
  print(f"The {direction}d text is {encoded}")

print(logo)
while not end_decoding:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n")) % 26
  caesar(text, shift, direction)
  end = input("Do you want to stop this system? yes or no?\n").lower()
  if end == 'yes':
    end_decoding = True
    