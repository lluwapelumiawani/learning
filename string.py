
sentence = input("Enter a sentence: ")


uppercase = sentence.upper()
print(f"Uppercase: {uppercase}")


lowercase = sentence.lower()
print(f"Lowercase: {lowercase}")

title_case = sentence.title()
print(f"Title Case: {title_case}")


char_count = len(sentence.replace(" ", ""))
print(f"Number of characters (excluding spaces): {char_count}")

