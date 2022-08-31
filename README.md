# org_str
This is a web application repository organizational structure.

Удобнее всего будет развернуть это приложение на локалке именно в докере.
Для этого клонируем репу -> запускаем докер ( к примеру десктоп приложение ).
В Пайчармe переходим в директорию с докер файлами ( на уровне manage.py ). 
В консоли исполняем команду ( точь-в-точь как ниже с точкой и пробелом ) :

docker build --tag docker_org_str .

Затем:

docker-compose up

После этого приложение доступно по адресу http://localhost:8000/

В приложении есть авторизация и разграничение доступа. 
Часть страниц доступна только авторизованым юзерам, другая - всем. 

При открытии сайта вы увидите страницу авторизации:
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/0.png" width="800">

Если у вас еще нету логина и пароля, то пройдите регистрацию: 
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/1.png" width="800">

Пройдя авторизацию вы попадаете на главную с навигацей по страницам сайта:
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/14.png" width="800">

<p>Кнопка Выйти работает, при нажатии на нее вас разлогинет и перенаправит на стриницу </p>
<p>( == подтвержение что разлогинивание прошло успешно):</p>
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/8.png" width="800">

Страница со статичным деревом сотрудников ( чтобы было видно прогресс ) 
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/3.png" width="700">

<p>Страница со динамичным деревом сотрудников<p>
( раскрывающееся меню, при нажатии на сотрудника выпадают его подчиненные, но только следующего уровня! )
<p>При нажатии на Генерального директора выпадают только его дирекора, и так для каждого. <p>
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/23.png" width="700">

<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/19.png" width="700">

Пагинированная страница с сотрудниками с возможностью фильтрации и ссылкой для редактирования этого сотрудника:  
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/20.png" width="700">
 
При нажатии на сслыку редактировать заргужаеться форма для редактирования сотрудника. 
<p>C пока не очень аккуратой версткой и не адапитированными полями<p>   
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/24.png" width="700">

 Страница с помощью которой можно добавлять новых сотрудников через сайт, а не админку:  
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/18.png" width="800">
 
 Назначемая должность и руководитель выбираеться из выпадающего списка ( в соотвествии с админкой )  
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/16.png" width="700">

<p>При успешном создании юзера перенапрявляет на страницу подтвержения того, что новый сотрудник добавлен<p>
 С возможностью юзеру быстро перейти к созданию следущего сотрудника ( гипессылка )
   
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/17.png" width="700">
 
<p>Админка с деревом и меню:<p>
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/5.png" width="700">

 <p>Админка и сайт по возможности русифицированы ( адаптировано под русскоязычного юзера ) :<p>
<img src="https://github.com/cheremyha/pictures_for_read_me/blob/main/22.png" width="700">
