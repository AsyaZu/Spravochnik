def file_reading():
    with open('spravochnik.txt') as file:
        a = file.readline()
        return a

def save():
    file1 = file_reading()
    with open('new_spravochnik.txt', 'w') as file:
        file.write(file1)
save()