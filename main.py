import telebot
from telebot import types

uMap = {
    'poly':'СПБПУ Им. Петра Великого',
    'leti':'СПБГЭТУ ЛЭТИ'
}

suMap = {
    'poly':'https://www.spbstu.ru/',
    'leti': 'https://etu.ru/'

}

fbMap= {
    'poly':'https://tabiturient.ru/vuzu/spbstu/',
    'leti':'https://tabiturient.ru/vuzu/eltech/'
}

bacMap = {
    'leti':'https://etu.ru/ru/abiturientam/napravleniya-podgotovki/bakalavriat/',
    'poly':'https://www.spbstu.ru/abit/bachelor/to-choose-the-direction-of-training/bachelor-s-degree-programs/'
}

salesMap = {
    'leti':'https://etu.ru/ru/abiturientam/priyom-na-1-y-kurs/platnoe-obuchenie',
    'poly':'https://www.spbstu.ru/abit/bachelor/apply/stoimost-obucheniya/'

}

scoreMap = {
    'leti':'https://etu.ru/ru/abiturientam/priyom-na-1-y-kurs/prohodnye-bally',
    'poly':'https://www.spbstu.ru/abit/bachelor/entrance-test/average-passing-scores-of-previous-years/'
}
def main():
    bot = telebot.TeleBot("5118412505:AAGTE45Ruor59GvA7qq1UXzUehr21DQWhSE")

    @bot.message_handler(commands=["start"])
    def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton(uMap.get('poly'))
        item2 = types.KeyboardButton(uMap.get('leti'))
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Выбери университет', reply_markup=markup)

    @bot.message_handler(content_types=["text"])
    def handle_text(msg):
        if msg.text.strip()==uMap.get('poly'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('сайт')
            item2 = types.KeyboardButton('отзывы')
            markup.add(item1)
            markup.add(item2)
            bot.send_message(msg.chat.id, 'что тебя интересует?', reply_markup=markup)
            bot.register_next_step_handler(msg, question_poly)
        elif msg.text.strip()==uMap.get('leti'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('сайт')
            item2 = types.KeyboardButton('отзывы')
            markup.add(item1)
            markup.add(item2)
            bot.send_message(msg.chat.id, 'что тебя интересует?', reply_markup=markup)
            bot.register_next_step_handler(msg, question_leti)




    def question_leti(msg):
        if msg.text.strip()=='отзывы':
            bot.send_message(msg.chat.id, '[Держи]('+fbMap.get('leti')+')', parse_mode='MarkdownV2')

        elif msg.text.strip()=='сайт':
            bot.send_message(msg.chat.id, '[Лови]('+suMap.get('leti')+')', parse_mode='MarkdownV2')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bacItem = types.KeyboardButton('Направления бакалавриата')
            scoreItem = types.KeyboardButton('Проходные баллы')
            salesItem = types.KeyboardButton('Стоимость обучения')
            markup.add(bacItem)
            markup.add(scoreItem)
            markup.add(salesItem)
            bot.send_message(msg.chat.id, 'Нужно что-то конкретное?', reply_markup=markup)
            bot.register_next_step_handler(msg, lSite_question)

    def lSite_question(msg):
        if msg.text.strip()=='Направления бакалавриата':
            bot.send_message(msg.chat.id, '[Держи]('+bacMap.get('leti')+')', parse_mode='MarkdownV2')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            answerBack = types.KeyboardButton('В начало')
            answerNo = types.KeyboardButton('Нет, спасибо!')
            markup.add(answerBack)
            markup.add(answerNo)
            bot.send_message(msg.chat.id, 'Что-то ещё?', reply_markup=markup)
            bot.register_next_step_handler(msg, exit)
        elif msg.text.strip()=='Проходные баллы':
            bot.send_message(msg.chat.id, '[Держи]('+scoreMap.get('leti')+')', parse_mode='MarkdownV2')
        elif msg.text.strip()=='Стоимость обучения':
            bot.send_message(msg.chat.id, '[Держи]('+salesMap.get('leti')+')', parse_mode='MarkdownV2')

    def question_poly(msg):
        if msg.text.strip()=='отзывы':
            bot.send_message(msg.chat.id, '[Держи]('+fbMap.get('poly')+')', parse_mode='MarkdownV2')

        elif msg.text.strip()=='сайт':
            bot.send_message(msg.chat.id, '[Лови]('+suMap.get('poly')+')', parse_mode='MarkdownV2')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bacItem = types.KeyboardButton('Направления бакалавриата')
            scoreItem = types.KeyboardButton('Проходные баллы')
            salesItem = types.KeyboardButton('Стоимость обучения')
            markup.add(bacItem)
            markup.add(scoreItem)
            markup.add(salesItem)
            bot.send_message(msg.chat.id, 'Нужно что-то конкретное?', reply_markup=markup)
            bot.register_next_step_handler(msg, pSite_question)


    def pSite_question(msg):
        if msg.text.strip()=='Направления бакалавриата':
            bot.send_message(msg.chat.id, '[Держи]('+bacMap.get('poly')+')', parse_mode='MarkdownV2')
        elif msg.text.strip()=='Проходные баллы':
            bot.send_message(msg.chat.id, '[Держи]('+scoreMap.get('poly')+')', parse_mode='MarkdownV2')
        elif msg.text.strip()=='Стоимость обучения':
            bot.send_message(msg.chat.id, '[Держи]('+salesMap.get('poly')+')', parse_mode='MarkdownV2')


    def exit(msg):
        if msg.text.strip()=='Нет, спасибо!':
            bot.send_message(msg.chat.id, 'Хорошо, увидимся!')
            start()
        elif msg.text.strip()=='В начало':
            msg = "start"
            bot.register_next_step_handler(msg, start)


    bot.polling(none_stop=True, interval=0)
if __name__=='__main__':
    main()