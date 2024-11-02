import requests
import json
import os


# token = 'vk1.a.N5Y7h00bQ48qMnKnrBahW_lCiVvyEDhEpoLq9Sar8NZrb1xNBKYw249DDyxT80Nf6XR5KqSGSus3-HS2gmCwzg_86tQ3qeXo0iEOgwnGPemy9jmLueK9u5-mJ_urAacaTaA-tfwg2BJQorIg6oTxlLEjjh9KUJlQMCoaiO__1NTb534wgGmM2kNWkIIaXF1L'
token = os.getenv("VK_ACCESS_TOKEN")
version = 5.131
user_id = 172531131


def get_user_data():
    params = {
        'access_token': token,
        'v': version,
        'user_id': user_id,
        'fields': 'followers_count'
    }
    response = requests.get(f"https://api.vk.com/method/users.get", params=params)
    return response.json()

def get_followers():
    params = {
        'access_token': token,
        'v': version,
        'user_id': user_id
    }
    response = requests.get(f"https://api.vk.com/method/users.getFollowers", params=params)
    return response.json()

def get_subscriptions():
    params = {
        'access_token': token,
        'v': version,
        'user_id': user_id
    }
    response = requests.get(f"https://api.vk.com/method/users.getSubscriptions", params=params)
    return response.json()

def save_data(data):
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    if token:
        file_path = input("Введите путь для сохранения файла: ")
        if not file_path:
            # file_path = "..\output.json"
            script_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(script_dir, "output.json")
        user_data = get_user_data()
        followers = get_followers()
        subscriptions = get_subscriptions()
        result = {
            'user_data': user_data,
            'followers': followers,
            'subscriptions': subscriptions
        }
        save_data(result)
        print("Данные сохранены в output.json")
    else:
        print("Ошибка: токен доступа не найден. Установите переменную окружения VK_ACCESS_TOKEN.")