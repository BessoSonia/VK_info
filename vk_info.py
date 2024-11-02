import requests
import json
import os


token = os.getenv("VK_ACCESS_TOKEN")
version = 5.131


def get_user_data(user_id):
    params = {
        'access_token': token,
        'v': version,
        'user_id': user_id,
        'fields': 'followers_count'
    }
    response = requests.get(f"https://api.vk.com/method/users.get", params=params)
    return response.json()

def get_followers(user_id):
    params = {
        'access_token': token,
        'v': version,
        'user_id': user_id
    }
    response = requests.get(f"https://api.vk.com/method/users.getFollowers", params=params)
    return response.json()

def get_subscriptions(user_id):
    params = {
        'access_token': token,
        'v': version,
        'user_id': user_id
    }
    response = requests.get(f"https://api.vk.com/method/users.getSubscriptions", params=params)
    return response.json()

def save_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    if token:
        user_id = input("Введите ID пользователя: ")
        if not user_id:
            user_id = 172531131
        file_path = input("Введите путь для сохранения файла: ")
        if not file_path:
            file_path = "output.json"
        else:
            file_path = file_path + '\output.json'
        user_data = get_user_data(user_id)
        followers = get_followers(user_id)
        subscriptions = get_subscriptions(user_id)
        result = {
            'user_data': user_data,
            'followers': followers,
            'subscriptions': subscriptions
        }
        save_data(file_path, result)
        print(f"Данные сохранены в {file_path}")
    else:
        print("Ошибка: токен доступа не найден. Установите переменную окружения VK_ACCESS_TOKEN.")