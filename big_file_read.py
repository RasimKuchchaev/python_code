'''
Это ленивая функция, в этой функции она будет считывать часть данных размера chunk_size за один раз.
'''    
def read_file_in_chunks(file_object, chunk_size=3072):
    
    while True:
        # Просто прочитайте данные размера chunk_size.
        data = file_object.read(chunk_size)

        # Если он дойдет до конца файла.
        if not data:
            # Break the loop.
            break

        yield data


# Откройте большой файл данных журнала.
with open('big_log_file.dat') as f:

    # Вызовите указанную выше функцию ленивого чтения данных из файла..
    for piece in read_file_in_chunks(f):

        # Обработайте часть данных, например, запишите данные в другой файл.
        process_data(piece)