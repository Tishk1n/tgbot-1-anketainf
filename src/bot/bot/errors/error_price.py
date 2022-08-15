class ErrorPrice(Exception):
    def __str__(self):
        return 'Цена должна быть целым числом!'
