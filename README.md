# simbirSoftTestProj
Предварительно необходимо иметь/завести почтовый ящик в google (или
yandex, если будут проблемы с автоматизацией). Отправить на этот ящик
несколько писем с темой «Simbirsoft Тестовое задание» с любым содержимым
(можно отправить с этого же ящика самому себе).
В задании необходимо:
1) Использовать Python/Java, подключить библиотеку Selenium Webdriver;
2) С помощью Selenium открыть браузер, открыть страницу выше указанной
почты(google.com/yandex.ru) и авторизоваться;
3) С помощью Selenium определить сколько во входящих нашлось писем с
темой «Simbirsoft Тестовое задание»;
4) С помощью Selenium и интерфейса почты написать/отправить письмо на
этот же почтовый ящик, в тексте которого указать найденное в шаге 3
количество писем. Указать тему письма «Simbirsoft Тестовое задание.
<Фамилия>», где <Фамилия> - это Ваша фамилия;
5) Оформить эти действия в виде теста.
При выполнении работы необходимо использовать следующие
технологии:
1) Selenium GRID (тесты запускать через GRID обязательно)
2) Использовать паттерн проектирования автотестов Page Object
3) Реализовать формирование отчетов о пройденных тестах через Allure

From test requirements was done:
1. Gmail auth via selenuim
2. Counting emails with required subject
3. Sending email with number of counted emails
4. Using pytest
5. Generating allure reports

Not done run tests via Selenium Grid ( never was in touch with selenium and testing before )

16 hours  on reading documentation and watching videos with examples and about 8 hours on writing and testing code.
