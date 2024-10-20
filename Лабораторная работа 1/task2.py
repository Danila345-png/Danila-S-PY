# TODO Найдите количество книг, которое можно разместить на дискете
weight_per_symbol = 4
symbols_in_line = 25
lines_in_page = 50
pages_in_book = 100
symbols_in_page = symbols_in_line * lines_in_page
symbols_in_book = symbols_in_page * pages_in_book
weight_per_book = symbols_in_book * 4 # 4 - количество байт
bytes_in_floppy = 1509949.44
books_in_floppy = bytes_in_floppy // weight_per_book
print("Количество книг, помещающихся на дискету:", int(books_in_floppy))
