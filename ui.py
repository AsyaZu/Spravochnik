
def import_file():
    with open('spravochnik.txt', encoding='UTF8') as file:
        a = file.read()
        return a

def save_txt():
    file1 = import_file()
    with open('new_spravochnik.txt', 'w', encoding='UTF8') as file:
        file.write(file1)

def inp():
    print('Операции со справочником: \n1 - вывести в консоль\n2 - сохранить в файл txt')
    return input('Введите команду: ')


def output(file):
    print(file)
