import emoji

try:
    response = input("Input: ").split()
    new_response = []
    for word in response:
        processed_word = emoji.emojize(word, language='alias')
        new_response.append(processed_word)
    final_response = ' '.join(new_response)
    print(final_response)
except ValueError:
    pass
