most_powerful_word_counter = 0
most_powerful_word = ''

while True:
    words = input()

    if words == "End of words":
        break

    current_counter_of_chars = 0

    for ch in words:
        current_counter_of_chars += ord(ch)

    if words[0].lower() in 'aeiouy':
        current_counter_of_chars *= len(words)
    else:
        current_counter_of_chars = int(current_counter_of_chars / len(words))
    if current_counter_of_chars > most_powerful_word_counter:
        most_powerful_word_counter = current_counter_of_chars
        most_powerful_word = words

print(f"The most powerful word is {most_powerful_word} - {most_powerful_word_counter}")
