# Чтение файлов разных форматов
import chardet

def read_file(file_name):
    with open("./texts/" + file_name, "rb") as f:
        data = f.read()
        result = chardet.detect(data)
        result_str = (data.decode(result["encoding"]))
        result_str.lower()
        list_str = result_str.split(" ")

        word_dict = {}
        for word in list_str:
            if word in word_dict and len(word) > 6:
                word_dict[word] +=1
            else:
                word_dict[word] = 1

        s = [(k, word_dict[k]) for k in sorted(word_dict, key=word_dict.get, reverse=True)[:10]]

        print(s)

#
read_file('newsafr.txt')
read_file('newscy.txt')
read_file('newsfr.txt')
read_file('newsit.txt')

# Перевод в читаемый формат
# Преобразование текста в список
# Создание словаря слово: количество раз встречи в тексте
# Пройтись циклом по полученному словарю, отсортировать по значениям и вывести на печать первые десять элементов отсор
# тированного словаря