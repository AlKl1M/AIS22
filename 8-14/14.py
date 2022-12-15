# Дан текстовый файл с текстом на русском или английском произв. длины (организовать чтение).
# выбрав некоторую хеш-функцию, создать хеш-таблицу со списками.

# хеширование
def HashFunction(s):
    result = 0
    for i in range(len(s)):
        result += ord(s[i])
    result = result % 32
    return result

# вставка
def insert(mas, line):
    key = HashFunction(line)
    if mas[key] != []:
        first = line
        second = mas[key]
        flag = True
        i = 0
        while (first[i] == second[i]):
            i+=1
        else:
            flag = False
        if flag:
            return "This row is already in the table"
        else:
            k = 0
            mas[key].append(line)
    else:
        mas[key].append(line)

# удаление
def delete(mas, line):
    key = HashFunction(line)
    for i in range(len(mas[key])):
        if mas[key][i] == line:
            del mas[key][i]

# поиск
def find(mas, line):
    key = HashFunction(line)
    if mas[key] != []:
        for i in range(len(mas[key])):
            if mas[key][i] == line:
                return mas[key][i]
    else:
        return "None"

# тест
if __name__ == "__main__":
    mas = [[] for i in range(32)]
    file = open("input", 'r')
    for line in file:
        line = ' '.join(line.split())
        insert(mas, line)
    for i in range(len(mas)):
        print(i, mas[i])
    a = find(mas, "We all like different genres, but we never argue with each other.")
    print(a)
    b = find(mas, "We begin to prepare in advance.")
    delete(mas, "We all like different genres, but we never argue with each other.")
    a = find(mas, "We all like different genres, but we never argue with each other.")
    print(a)
    print(b)