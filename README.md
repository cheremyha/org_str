# org_str
This is a web application repository organizational structure.

Удобнее всего будет развернуть это приложение на локалке именно в докере.
Для этого клонируем репу -> запускаем докер ( к примеру декстоп приложение ).
В Пайчармe переходим в директорию с докер файлами ( на уровне manage.py ). 
В консоли исполняем команду ( точь-в-точь как ниже с точкой и пробелом ) :

docker build --tag docker_org_str .

Затем:

docker-compose up

После этого приложение доступно по адресу http://localhost:8000/

В приложении есть авторизация и разграничение доступна. 
Часть страниц доступа только авторизованым юзерам, другая - всем. 

При открытии сайта вы увидите страницу авторизации:
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/0.png" width="800">

Если у вас еще нету логина и пароля, то пройдите регистрацию: 
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/1.png" width="800">

Пройдя авторизацию вы попадаете на главную с навигацей по страницам сайта:
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/2.png" width="800">

<p>Кнопка Выйти работает, при нажатии на нее вас разлогинет и перенаправит на стриницу </p>
<p>( == подтвержение что разлогинивание прошло успешно):</p>
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/8.png" width="800">

Дерево сотрудников могло бы выглядеть как-то так(раскрывающееся, с кнопками):
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/6.png" width="700">

Но пока выгллядит вот так, полностью статично и не производительно:( 
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/3.png" width="700">

Пагинированная страница с сотрудниками с возможностью фильтрации:  
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/7.png" width="700">

<p>Админка с деревом и меню:<p>
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/5.png" width="700">
