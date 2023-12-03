class PaginationHelper:
    def __init__(self, array: list, amount_item: int):
        self.array = array
        self.amount_item = amount_item
        if len(array) % amount_item == 0:
            self.amount_pages = int(len(array) / amount_item)
        else:
            self.amount_pages = len(array) // amount_item + 1



    def amount_items(self):
        return f'Количество элементов массива: {len(self.array)}'

    def amount_available_pages(self):
        return f'Количество доступных страниц: {self.amount_pages}'

    def amount_items_on_page(self, number_page: int):
        if number_page + 1 < 0 or number_page + 1 > self.amount_pages:
            raise ValueError(f"Страницы с таким номером не существует, вам доступны значения от 0 до {self.amount_pages - 1}")
        elif len(self.array) % self.amount_item == 0:
            return (f'Количество элементов на странице "{number_page}" равно {self.amount_item}')
        else:
            if number_page + 1 == self.amount_pages:
                elem = int(len(self.array) - (self.amount_pages - 1) * self.amount_item)
                return f'Количество элементов на странице "{number_page}" равно {elem}'
            else:
                return f'Количество элементов на странице "{number_page}" равно {self.amount_item}'

    def index(self, index_item: int):
        if index_item < 0 or index_item > len(self.array) - 1:
            raise ValueError(f'Вы можете ввести только индексы от 0 до {len(self.array) - 1}')
        index_item += 1
        if index_item % self.amount_item == 0:
            return f"Элемент с индексом {index_item - 1} находится на странице {index_item // self.amount_item - 1}"
        else:
            return f"Элемент с индексом {index_item - 1} находится на странице {round(index_item // self.amount_item)}"






