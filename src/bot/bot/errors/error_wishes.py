class ErrorWishes(Exception):
    def __str__(self) -> str:
        return 'Попробуйте ввести ваши пожелания еще раз, сообщение не должно превышать 300 символов'
