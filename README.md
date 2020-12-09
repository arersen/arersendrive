# arersendrive
Загрузчик данных на сервер arersengit.7m.pl/files, c FTP инструментами и прочее

## Установка
#### apt install python
#### python3 -m pip install requests
#### python main.py

## Команды:
<li><b>add</b> - Добавить файл на сервер</li>
<li><b>get</b> - Получить файл с сервера</li>
<li><b>mkdir</b> - Создать директорию на сервере</li>
<li><b>ls</b> либо <b>list</b> либо <b>dir</b> - Показать содержимое директории</li>
<li><b>put</b> - загрузить файл на сервер. (а для того чтоб его загрузить вы должны иметь переконвертирован ваш файл в BASE64 String</li>
<li><b>del</b> - удаляет файл с сервера</li>

## functions.py
Модуль с http запросами создан мной для модификации своей консоли. Лучше используйте main.py, там уже все настроено.</br>Подробнее про http-запросы по этой ссылке: https://github.com/kotleni/kotleni.github.io/blob/master/projects/php/files_man/server/
