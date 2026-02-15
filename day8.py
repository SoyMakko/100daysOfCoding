# #functions with no inputs

# def greet():
#     for i in range(3):
#         print(f"Statement {i + 1}")

# greet()

# #function with inputs
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# name = input("What is your name?")
# greet_with_name(name)

# def life_in_weeks(age):
    
#     remaining_weeks = (52 * 90) - (age * 52)
    
#     print(f"You have {remaining_weeks} weeks left.\n")
    
# life_in_weeks(20)


# def calculate_love_score(name1, name2):
#     combined_names = (name1 + name2).lower()
#     true_count = 0
#     love_count = 0
    
#     for letter in "true":
#         true_count += combined_names.count(letter)
#     for letter in "love":
#         love_count += combined_names.count(letter)
    
#     love_score = int(str(true_count) + str(love_count)) 
#     print(love_score)


# calculate_love_score("Kanye West", "Kim Kardashian")


#Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def encrypt(original_text,shift_amount):

#     shifted_word = list(original_text)

#     for i in range(len(shifted_word)):
#         if shifted_word[i] in alphabet:
#             index = alphabet.index(shifted_word[i])
#             new_index = (index + shift_amount) % len(alphabet)
#             shifted_word[i] = alphabet[new_index]


#     print(f"encrypted string is {shifted_word}")

# def decrypt(original_text,shift_amount):
#     deshifted_word = list(original_text)

#     for i in range(len(deshifted_word)):

#         if deshifted_word[i] in alphabet:
#             index = alphabet.index(deshifted_word[i])
#             new_index = (index - shift_amount) % len(alphabet)
#             deshifted_word[i] = alphabet[new_index]


#     print(f"decrypted string is {deshifted_word}")   

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

