# 2. поиск самого длинного слова в строке через ;
text = input("Введите строку (слова через ';'): ")
words = text.split(";")
# переменная для хранения самого длинного слова
longest = ""
# перебираем каждое слово из списка
for w in words:
    word = w.strip()
    if len(word) > len(longest):
        longest = word
print("Самое длинное слово:", longest)

