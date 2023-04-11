from aiogram.types import Message

# Класс-фильтр, который проверяет пользователь админ или нет
class IsAdmin:
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids
    def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids