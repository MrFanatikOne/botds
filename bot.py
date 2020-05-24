import DB
import discord
import random
#токен аунтификации бота в дс
TOKEN = ''

client = discord.Client()
#DB.create_table()

@client.event
async def on_message(message):
    #заглушка от обработки лишних сообщений
    if message.author == client.user or not (message.content.startswith('!')):
        return
    msg = ''


#Список всех команд
    if message.content.startswith('!Help'):
        msg = 'Привет, я бот, мои команды \n!Число - произвольное число\n!Ответь, - бот произвольно отвечает на твой вопрос\n!Кто - выбирает кого то с сервера'
        await message.channel.send(msg)


#Рандомное число до 100000
    if message.content.startswith('!Число'):
        await message.channel.send(random.randint(0, 1000000))


#Рандомный ответ на вопрос
    if message.content.startswith('!Ответь,'):
        random_choice = random.random() * 5
        msg = 'Error'
        if int(random_choice) == 1:
                msg='Да'

        if int(random_choice) == 2:
                msg='Нет'

        if int(random_choice) == 3:
                msg='Без понятия'

        if int(random_choice) == 4:
                msg='38'

        if int(random_choice) == 5:
                msg='А гугл тебе зачем?'

        if int(random_choice) == 0:
                msg='Спроси у Мурада'

        await message.channel.send(msg,tts=False)

    #Команда Кто
    if message.content.startswith('!Кто'):
        data = DB.read_db()
        msg = 'Я думаю это ' + random.choice(data)[2]
        await message.channel.send(msg, tts=False)




@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
