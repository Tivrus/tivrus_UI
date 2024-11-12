import re
import requests
import json




def get_figma_file_from_url(figma_url, api_token):
    # Извлекаем file ID из ссылки с помощью регулярного выражения для разных случаев
    match = re.search(r'https://www.figma.com/(file|design)/([0-9A-Za-z]+)', figma_url)
    if match:
        figma_url = match.group(0)
    elif not match:
        print("Не удалось найти file ID в ссылке.")
        return None
    
    file_id = match.group(2)  # Извлекаем file ID из второго совпадения
    print(f"Найденный file ID: {file_id}")
    
    # Выполняем запрос к Figma API
    response = requests.get(
                f"https://api.figma.com/v1/files/{file_id}",
                headers={"X-FIGMA-TOKEN": api_token})
    return response.json()

def save_to_json(data, filename="figma_file_data.json"):
    # Сохраняем данные JSON в файл
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Данные сохранены в {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")







# Пример использования
figma_url = input("Введите ссылку:\n ")
api_token = "figd_Dv7w381lon2V1Msc3POEkP5uUodOKsKlAlk3-NBA"

# Получаем данные
file_data = get_figma_file_from_url(figma_url, api_token)

# Проверяем результат и сохраняем
if file_data:
    print("Данные JSON получены.")
    save_to_json(file_data)  # Сохраняем JSON данные в файл
else:
    print("Ошибка при получении данных.")

