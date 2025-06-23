![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)


##  Автотест проверки автоматической установки под платформу Windows с использованием Python. 


Убедитесь, что у вас установлен Python. Клонируйте репозиторий
```bash
git clone git@github.com:Evgeniya-Shokolova/testing_application.git
```
Перейти в папку с проектом
```bash
cd testing_application
```
Создать виртуальное окружение:
   Команда для Windows: -
```bash
python -m venv venv
```
Команда для Linux и macOS: - 
```bash
python3 -m venv venv
```
Активировать виртуальное окружение:
   Команда для Windows: -
```bash
source venv/Scripts/activate
```
Для Linux и macOS: -
```bash
source venv/bin/activate
```
Установить необходимые библиотеки:
```bash
pip install requests
```
```bash
pip install html-testRunner
```
Обновить пакетный менеджер:
   Для Windows: -
```bash
python -m pip install --upgrade pip
```
Для Linux и macOS: -
```bash
python3 -m pip install --upgrade pip
```


### Запуск скрипта:
```bash  
pytest --html=report.html
```

### Отчет о тестировании

Чтобы открыть файл `report.html` в браузере, выполните следующие шаги:
1. Через проводник:
   - Дважды щелкните по файлу левой кнопкой мыши. Обычно по умолчанию он откроется в вашем браузере.

2. Через браузер:
   - Перетащите файл `report.html` из проводника в окно браузера.

