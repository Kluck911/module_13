user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm',
    'kluck': '1812'
}

username = input('Введите логин:\n')
if username in user_database.keys():
   password = input('Введите пароль:\n')
   if password == user_database.get(username):
       print('Вы успешно вошли в систему')
   else:
       print('Отказано в доступе')
else:
   print('Такого пользователя не существует')