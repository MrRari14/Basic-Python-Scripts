# Ask the user to input the desired language.

lang = input("Please select your language of preference (EN, SP, FR): ")

# Create a function that selects the desired language determined by the user´s input.


def greet(lang):
    if lang == "EN" or lang == "en":
        print("Hello!")
    elif lang == "SP" or lang == "sp":
        print("Hola!")
    elif lang == "FR" or lang == "fr":
        print("Bonjour!")
    else:
        print("Language not available.")

# Call the function. Otherwise, it won´t run it.


greet(lang)
