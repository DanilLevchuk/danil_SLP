def count_vowels_and_consonants(word):
    vowels = "УЕЭОАЫЯИЮуеэоаыяию"
    consonants = "ЙЦКНГШЩЗХЪФВПРЛДЖБТЬМСЧйцкнгшщзхъфвпрлджчсмтьб"

    vowel_count = sum(1 for char in word if char in vowels)
    consonant_count = sum(1 for char in word if char in consonants)

    return vowel_count, consonant_count


input_text = input("Введите строку текста: ")

if isinstance(input_text, str):
    vowels, consonants = count_vowels_and_consonants(input_text)
    print(f"{input_text}: Гласных - {vowels}, Согласных - {consonants}")
else:
    print("Введенное значение не является строкой.")
