Тестовое задание одного из работодателей. 
Frontend не обязателен
Авторизацию делать не надо

Система предназначена для рекрутов, желающих пройти обучение.
Система содержит следующие модели:
Рекрут (Имя, Планета на которой живет, Возраст, Почта);
Преподаватель (Имя, Планета на которой преподает);
Планета (Наименования);
Тестовые вопросы (уникальный код преподавателя, список вопросов);
Такие модели как Преподаватель, Планета, Тестовые вопросы заводятся через панель администратора.


На главной странице системы нужно отобразить выбор формы:

«Для Преподавателей» и «Для Рекрутов»

Если пользователь выбрал «Для Рекрутов»: 
- Необходимо отобразить ему форму, в которой о укажет данные (Имя, Планета, Возраст, Почта) и нажмет кнопку «Далее». Данные сохраняются в базу студентов. 
- Затем ему отображаются тестовые вопросы, на которые он даст ответы (для простоты ответы могут быть True/False).

Если пользователь выбрал «Для Преподавателей»:
- Выбирает себя из списка преподавателей. Далее ему отображается список рекрутов, ответивших на вопросы, но не зачисленных к преподавателю.
- Преподаватель может посмотреть список ответов каждого студента.
- Если ответы устраивают преподавателя, но зачисляет студента к себе.
- Если рекрут зачислен, ему направляется уведомление.  

Дополнительно (не обязательно к реализации):
- Установить ограничение на кол-во рекрутов у одного преподавателя (не более 3-х).
- Вывести полный список преподавателей в котором для каждого преподавателя будет указано кол-во студентов.
- Вывести всех преподавателей, у которых более 1 студента. 

TODO List
1.	Добавить Дополнительные требования; 
2.	Frontend;
3.	Доработать форму ответов на вопросы;
4.	Доработать форму зачисления рекрутов к преподавателю.
