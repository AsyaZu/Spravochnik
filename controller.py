import ui

def launсh(source):
    phone_book = ui.import_file_2_dict(source) # импорт файла
    crud = ui.inp() # цифровое меню 1 - вывести в консоль, 2 - сохранить в файл txt
    if crud == '1':
        ui.output(phone_book) # печать в консоль
    elif crud == '2':
        ui.save_2_csv(phone_book) # сохранить в csv

