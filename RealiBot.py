import EzTG


async def callback(bot, update):
    # here's your bot
    if 'message' in update:
        # messages "handler"
        message_id = update['message']['message_id']  # https://core.telegram.org/bots/api#message
        user_id = update['message']['from']['id']
        chat_id = update['message']['chat']['id']
        text = update['message']['text']

        if text == '/start':
            #menu nel messaggio
            MenuStart()

            # you can find method parameters in https://core.telegram.org/bots/api#sendmessage


        #nasconde il menu
        if text == '/tastiera':
            RimuoviMenu()
            await bot.sendMessage(chat_id=chat_id, reply_markup=keyboard)


    if 'callback_query' in update:
        # callback query "handler"
        message_id = update['callback_query']['message']['message_id']
        user_id = update['callback_query']['from']['id']
        chat_id = update['callback_query']['message']['chat']['id']
        cb_id = update['callback_query']['id']
        cb_data = update['callback_query']['data']

        if cb_data == 'callback contatti':
            MenuContatti()
              # you can find method parameters in https://core.telegram.org/bots/api#editmessagetext

        if cb_data == 'callback servizi':
            MenuServizi()


        if cb_data == 'callback indietro':
            indietro('contatti')
            await bot.editMessageText(chat_id=chat_id, message_id=message_id)


def MenuPrincipale():
    keyboard = EzTG.Keyboard('inline')
    keyboard.add('Contatti', 'callback contatti')
    keyboard.newLine()
    keyboard.add('Servizi', 'callback servizi')

def MenuSecondario():
    menu = EzTG.Keyboard('keyboard')
    menu.add('INDIETRO', 'indietro')
    menu.add('HOME', 'home')
    menu.newLine()
    menu.add('ARRESTA BOT', 'stop')

def MenuStart():
    MenuPrincipale()
    MenuSecondario()
    await bot.sendMessage(chat_id=chat_id, text=ListaComandi(), reply_markup=keyboard)

def ListaComandi():
    command="""Ciao sono RealiBot!
    Sono qui per mostrarti tutta la potenzialità di Lean Sales e perchè è la community italiana n. 1

    Comandi:
    /start
    /menu
    /tastiera
    /stop
    """
    return command

def RimuoviMenu():
    menu = EzTG.Keyboard('keyboard')

def MenuContatti():
    keyboard = EzTG.Keyboard('inline')
    keyboard.add('Simone Reali', 'callback simone')
    menu.newLine()
    keyboard.add('Commericalista', 'callback commercialista')
    menu.newLine()
    keyboard.add('Spedizionere', 'callback spedizionere')
    menu.newLine()
    keyboard.add('<- INDIETRO', 'callback indietro')
    await bot.editMessageText(chat_id=chat_id, message_id=message_id,
                        text='Ecco tutti i Contatti Lean Sales', reply_markup=keyboard)

def MenuServizi():
    keyboard = EzTG.Keyboard('inline')
    keyboard.add('controllo qualita', 'callback qualita')
    menu.newLine()
    keyboard.add('competizione potenziale', 'callback potenzialita')
    menu.newLine()
    keyboard.add('<- INDIETRO', indietro('servizi'))
    await bot.editMessageText(chat_id=chat_id, message_id=message_id,
                        text='Ecco tutti i Servizi Lean Sales', reply_markup=keyboard)

def indietro(source):
    if(source=='contatti'):
        MenuPrincipale()
    elif(source=='servizi'):
        MenuPrincipale()


bot = EzTG.EzTG(token='1494645372:AAHlmQr4hWPd3HPf-00WzzCaz5FdksfCeH4',
                callback=callback)
