import logging#Если в коде мы допустим ошибку, мы об этом не узнаем, так как авторы библиотеки для устойчивости бота "перехватывают" исключения, которые встречаются в нашем коде.
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)#Теперь, настроим логирование. Будем записывать все сообщения уровня INFO и выше в файл bot.log

# настройки Прокси
PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}

def main():
     # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher#В функции main() мы будем использовать диспетчер mybot.dispatcher для того, чтобы при наступлении события вызывалась наша функция:
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))#При использовании MessageHandler укажем, что мы хотим реагировать только на текстовые сообщения - Filters.text
    # Командуем боту начать ходить в Telegram за сообщениями
    logging.info("Бот стартовал") #Залогируем в файл информацию о старте бота
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

def talk_to_me(update, context):#Напишем функцию talk_to_me, которая будет "отвечать" пользователю
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def greet_user(update, context):#Бот вызовет функцию greet_user, когда пользователь напишет команду /start или нажмет кнопку Start при первом подключении к боту.
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')#Сейчас, когда пользователь пишет /start, наш бот сообщает об этом в консоль, но ничего не пишет пользователю. Ответим пользователю на его сообщение при помощи update.message.reply_text():

if __name__ == "__main__":
    main()