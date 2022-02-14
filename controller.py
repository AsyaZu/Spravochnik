import ui

def launсh():
    file = ui.import_file() # импорт файла
    crud = ui.inp() # цифровое меню 1 - вывести в консоль, 2 - сохранить в файл txt
    if crud == '1':
        ui.output(file) # печать в консоль
    elif crud == '2':
        ui.save_txt(file) # сохранить в txt

