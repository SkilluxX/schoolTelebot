
class Course:
    def __init__(self, name: str, price: int, length: int) -> None:
        self.name = name
        self.price = price
        self.length = length

    def display(self):
        return f"Курс {self.name}\tЦена: {self.price}р\tПродолжительность: {self.length} занятий"