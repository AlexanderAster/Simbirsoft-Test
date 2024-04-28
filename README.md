# Simbirsoft-Test
Отборочное тестовое задание Simbirsoft. Настоящий проект содержит Selenium/Pytest тесты на языке Python,выполняющие действия и проверки на основе этапов,описанных в документе тестового задания.
1. Объект тестирования - веб-ресурс [https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login]
2. Фреймворк тестирования - Pytest на базе библиотеки веб-тестирования Selenium WebDriver (драйвер Firefox geckodriver V 0.34.0-win64)
3. Интерпретатор - VS code.
4. Условия: Selenium GRID - не выполнено (в коде можно найти образцы настройки GRID. Сумел поднять hub/node,однако = error 500 Failed to create a session); PageObject - реализован частично; Allure - выполнено.
5. Папка elements содержит файл locators.py с локаторами. Тесты обращаются к ним по импорту
6. Папка pages содержит файл base_page.py с классами страниц. Тесты обращаются к ним по импорту
7. Папка tests содержит файл xyz_test.py с тестами. Все тесты собраны в одном файле и исполняются всем набором по порядку. (Из-за немногочисленности проверок,плотной зависимости этапов друг от друга и ограниченной функциональности сервиса,разделять тесты по нескольким файлам посчитал нецелесообразным)
8. В набор внедрена библиотека и метки Allure report. Файл с результатами должен быть создан автоматически в результате успешного запуска.
9. Файл transactions.csv содержит строки собранных с сервиса данных о транзакциях и,по совместительству,является объектом загрузки новых данных  в результате успешного запуска (2 старые + 2 новые)
10. test_transactions функция считается нестабильной в силу уязвимости сервиса к высокой нагрузке.
11. Среднее время прогона в режиме ui отображения : 20 сек.
12. Запуск : python -m pytest tests\xyz_test.py --alluredir allure-results (драйвер есть в переменной среды) / python -m pytest --driver Firefox --driver-path C:{path}\geckodriver.exe tests\xyz_test.py --alluredir allure-results / allure serve - посмотреть отчёт.
