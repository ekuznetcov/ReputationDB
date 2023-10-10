## Порядок работы с репозиторием  

#### Требования  
На машине, где будет располагаться скрипт:
- Docker  
- python > 3.9  
- машина должна иметь выход в Интернет  

#### Порядок работы
0. Склонировать git репозиторий  
```bash
git clone https://github.com/egor57k/ReputationDB  
```
1. Запустить mongo db в Docker-контейнере с помощью команды  
```bash
docker run -d -p hostport:27017 -v /path/to/local/data/folder/:/data mongo  
```
2. Создать виртуальное окружение python и установить зависимости  
```bash  
cd ReputationDB  
python3 -m venv .venv  
source ./.venv/bin/activate  
pip install -r requirements.txt  
```
3. Добавить main.py в crontab на ежедневное выполнение
```bash
crontab -e
```
В редакторе добавть запись:  
`0 0 * * * /path/to/ReputationDB/.venv/bin/python /path/to/ReputationDB/main.py`

Теперь скрипт будет выполняться каждый день в 00:00

#### Дополнительно 
Скрипт создаст:
- базу данных: repdb
- и в ней коллекцию replist

Структура документа:  
  {  
    _id: ObjectId("652483a0e499afb1fe2e07ec"),  
    created_date: '2023-10-09T22:33:14',  
    data: '93. 83. 35. 2',  
    data_type: 'ip',  
    derived: '8447',  
    derived_type: 'asn_num',  
    source: 'threatfox',  
    source_url: 'https://threatfox.abuse.ch'  
  }

Результат работы скрипта - csv файл reputation-YYYY-MM-DD.csv  
Строка файла имеет структуру:  
data, source_url created_date