Задание: 
----
* Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
* Django Модель `Item` с полями `(name, description, price) `
* API с двумя методами:
    * GET `/buy/{id}`, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос` stripe.checkout.Session.create(...)` и полученный session.id выдаваться в результате запроса
    *  GET `/item/{id}`, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном `Item` и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на `/buy/{id}`, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму `stripe.redirectToCheckout(sessionId=session_id)`
Пример реализации можно посмотреть в пунктах 1-3 тут

* Залить решение на Github, описать запуск в Readme.md

* Запуск используя `Docker`

* Использование `environment variables`

* Просмотр Django Моделей в Django Admin панели - __доступно по адресу `sw.neafiol.site:8000/admin` user: `admin`, pass: `admin`__

* Запуск приложения на удаленном сервере, доступном для тестирования - __запущенно на `sw.neafiol.site:8000`__

*  Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items - __сделана реализация методов в API__


Запуск
----
```
apt-get install python3-venv git

git clone https://github.com/tturdumamatovv/stripe
python3 -m venv ./venv
pip3 install -r requirements.txt
python3 manage.py runserver 0.0.0.0:8000
```

Сервис
----------------------------
* `/` - index
* `admin/` - Админка admin.site.urls
* `buy/<item_id>` - купить товар
* `item/<item_id>` - страница товара
* `order/buy/<order_id>` - купить заказ
* `order/put/<order_id>` - добавить товар в заказ
* `order/new/` - создать заказ
