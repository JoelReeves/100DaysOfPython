import math

def greet():
    print("Hello")
    print("Good morning")
    print("Good bye")

greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Good morning {name}")
    print(f"Good bye {name}")

greet_with_name("Joel")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Joel and Jeanette", "Oregon")
# using keyword arguments - putting argument before parameter
greet_with(location= "Oregon", name="Joel and Jeanette")

# Paint Area Calculator
def paint_calc(height, width, cover):
    calculation = math.ceil((height * width) / cover)
    print(f"You'll need {calculation} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# Prime Number Checker
def prime_checker(number):
    is_prime_number = True
    is_prime = "It's a prime number."
    not_prime = "It's not a prime number."

    for num in range(2, number):
        if number % num == 0:
            is_prime_number = False
            break

    if is_prime_number:
        print(is_prime)
    else:
        print(not_prime)

n = int(input("Check this number: "))
prime_checker(number=n)

# Caesar Cypher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_length = len(alphabet)

def caesar(text, shift_amount, direction):
    caesar_text = ""
    is_encode = direction == "e"

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if is_encode:
                shifted_position = position + shift_amount
                if shifted_position >= alphabet_length:
                    shifted_position = shifted_position % alphabet_length
                caesar_text += alphabet[shifted_position]
            else:
                shifted_position = position - shift_amount
                if shifted_position < 0:
                    shifted_position = alphabet.index(alphabet[-1]) - shift_amount + 1
                caesar_text += alphabet[shifted_position]
        else:
            caesar_text += letter

    if is_encode:
        print(f"The encoded text is {caesar_text}")
    else:
        print(f"The decoded text is {caesar_text}")

from art import logo # instead of using import art statement
print(logo)

continue_cipher = True
while continue_cipher:
    direction = input("Type 'e' to encrypt, type 'd' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    shift = shift % len(alphabet)
    caesar(text, shift, direction)

    result = input("Type 'y' if you want to play again. Otherwise type 'n': ").lower()
    if result == "n":
        print("Thanks for playing!")
        continue_cipher = False
