import requests, pytest

#
# Глобальные переменные модуля
#

ya_token = 'AQAAAAAAEXASAADLW3F-yNzR-0K8tmaC2kHRffE'
ya_url = 'https://cloud-api.yandex.net/v1/'
disk_url = 'disk'
folder_url = 'disk/resources'

#
# Классы и процедуры модуля
#

# функция получения списка папок на yandex.disk
def ya_folders_list(token: str) -> list:
    url = ya_url + disk_url
    headers = {'Accept': 'application/json', 'Authorization' : f'OAuth {token}'}
    response = requests.get(url, headers=headers)
    if response.ok and response.status_code == 200:
        folders = response.json()['system_folders'].keys()
    else:
        folders = {}
        
    return folders
# end ya_folder_list()

# функция тестирования сервиса yandex.disk (получение списка папок)
def test_ya_folder_list():
    # в случае успешного выполнения запроса список с папками не должен быть пустой
    assert len(ya_folders_list(ya_token)) > 0
# end test_ya_folder_list()

#
# Основная программа модуля
#

if __name__ == '__main__':
    pytest.main()
