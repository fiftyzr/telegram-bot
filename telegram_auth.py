from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

api_id = '22011892'
api_hash = '1d2c54a27a6590697dd0668c8e4e6bcd'
phone_number = '+79507892322'  # Ваш номер телефона
password = '785629'  # Ваш пароль

# Создание клиента с уникальной сессией
client = TelegramClient('my_session', api_id, api_hash)

async def main():
    try:
        # Запуск клиента и ожидание ввода номера телефона при первом запуске
        await client.start(phone_number)  # Номер телефона не передаем через параметр
        print("Авторизация прошла успешно.")
    except SessionPasswordNeededError:
        # Если включена двухфакторная аутентификация, ввод пароля
        await client.start(password=password)
        print("Авторизация прошла успешно.")

    # Ждем завершения работы клиента
    await client.run_until_disconnected()
