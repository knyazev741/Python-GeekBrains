name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
date = input("Введите дату рождения: ")
city = input("Введите город проживания: ")
mail = input("Введите e-mail: ")
phone = input("Введите телефон: ")

def user(name=None, surname=None, date=None, city=None, mail=None, phone=None):
    print(f"Данные о пользователе:  Имя:{name} Фамилия:{surname} Дата рождения:{date} Город проживания:{city} E-mail:{mail} Номер телефона:{phone}")

user(name=name, surname=surname, date=date, phone=phone, city=city, mail=mail)
