s = input().strip()

kyTu = s.split()

normalized_words = []

for word in kyTu:
    normalized_word = word.capitalize()
    normalized_words.append(normalized_word)
# normalized_words = [word.capitalize() for word in words]

kq = ' '.join(normalized_words)
print(kq)
