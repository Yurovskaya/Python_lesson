 # создайте списко с серией коротких сообщений. Передайте списко функции show_message()
 # которая выводит текст каждого сообщения в списке

# def show_message(message_list):
#     for message in message_list:
#         print(message)
#
# message_list = ['Прогноз погоды на сегодня', 'Штормовое предупреждение', 'Ожидается порывистый ветер', 'Местами дождь']
# show_message(message_list)


# Напишите функцию send_message() которая выводит каждое сообщение и перемещает его в новый список
#  с именем sent_massage. После вызова функции выведете обы списка и убедитесь в том, что перемещение произошло успешно

def show_message(message_list):
    while message_list:
        new_message_list = message_list.pop()
        sent_messages.append(new_message_list)
        print(f"Printing message: {new_message_list}")
        print(f"{sent_messages}")


message_list = ['Прогноз погоды на сегодня', 'Штормовое предупреждение', 'Ожидается порывистый ветер', 'Местами дождь']
sent_messages = []
show_message(message_list[:])




