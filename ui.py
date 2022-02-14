
def import_file():
    with open('spravochnik.txt', encoding='UTF8') as file:
        return file.read()


def import_file_2_dict(adr):
    with open(adr, encoding='UTF8') as file:
        tmp = [line.strip() for line in file.readlines() if line != '\n']
        pb = {}
        for i in range(0, len(tmp), 4):
            pb.update({tmp[i+2]: [tmp[i], tmp[i+1], tmp[i+3]]})
    return pb

def d_item_2_csv(v):
    st = ''
    for i in range(len(v)):
        st += ',' + v[i]
    return st

def save_2_csv(f):
    export_to = 'new_spravochnik.txt'
    with open(export_to, 'w', encoding='UTF8') as file:
        for k,v in f.items():
            file.write(f'{k}{d_item_2_csv(v)}\n')
    print(f"Файл {export_to} сохранён.")


def inp():
    print('Операции со справочником: \n1 - вывести в консоль\n2 - сохранить в файл txt')
    return input('Введите команду: ')


def output(f):
    print()
    for k,v in f.items():
            print(f'{k} : {v}\n')
