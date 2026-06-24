import string
alphabet_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]
def encrypt(plain_text, shift_key):
    cipher_text = ""

    for char in plain_text:
        position = alphabet_list.index(char)
        new_position = (position + shift_key)%26
        cipher_text = cipher_text + alphabet_list[new_position]

    print(f"here is the text after encryption: {cipher_text}")

def decrypt(cipher_text, shift_key):
    plain_text = ""

    for char in cipher_text:
        position = alphabet_list.index(char)
        new_position = (position - shift_key)%26
        plain_text = plain_text + alphabet_list[new_position]

    print(f"here is the text after encryption: {plain_text}")
end=False
while not end:
    what_to_do=input("type encrypt or decrpt")
    text=input("ur msg")
    key=int(input("enter key:\n"))
    if what_to_do=="encrypt":
        encrypt(text,key)
    elif what_to_do=="decrypt":
        decrypt(text,key)
    play_again=input("yes than continous other no mean exit")
    if play_again=='no':
        end=True
        print("have a nice day")
        