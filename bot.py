from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print('Microfone...')
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio, language='pt_BR')
        print('Humano: ' + frase)
    except sr.UnknownValueError:
        print('Bot: Isso não funcionou')
    return frase

def cria_audio(audio):
    tts = gTTS(audio, lang='pt-BR')
    tts.save('bot.mp3')
    playsound('bot.mp3')

bot = ChatBot('ChatBot')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Eu estou bem e você?', 'Eu estou bem', 'Que bom', 'Qual sua série favorita', 'Modern Family']

trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
    #quest = input('Humano: ')
    quest = ouvir_microfone()
    resposta = bot.get_response(quest)
    cria_audio(str(resposta))
    print('Bot: ', resposta)

