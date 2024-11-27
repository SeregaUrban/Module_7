def custom_write(file_name: str , strings: list):
    res= {}
    line_number = 1
    file = open(file_name, 'w',encoding = 'utf-8')

    for one_string in strings:
        line_byte = file.tell()
        file.write(f'{one_string}\n')
        res[(line_number, line_byte)] = one_string
        line_number += 1
    file.close()
    return res
if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)