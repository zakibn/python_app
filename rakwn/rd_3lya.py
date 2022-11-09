# 9anat  راكوان للبرمجة - CodeRK
# عنوان الفيديو
# لغة بايثون تطبيقات الذكاء الاصطناعي برمجة نظام ذكي شبيه بنظام شركة مارسيدس يستمع اليك ويتكلم معك

#from logging.config import listen
import pyttsx3
import speech_recognition as sr
import webbrowser
import time

# التهيئة
wel = pyttsx3.init()
# اجلب خاصية الاستماع الى الاصوات
voices = wel.getProperty('voices')
# التحكم في معدل الكلام
print(voices)
wel.setProperty(voices, voices[0].id)


def Speak(audio):
    # تكلم
    wel.say(audio)
    # تكلم و توقف
    wel.runAndWait()


def TakeCommands():
    command = sr.Recognizer()
    # افتح المايك لاتكلم عليه
    with sr.Microphon() as mic:
        print('say commands sir....')
        command.phrase_threshold = 1
        # استمع
        audio = command.listen(mic)
        try:
            print('Recording...')
            #    تعرف على اللغة باستخدام ريكوقنايز قوقل التي تعمل بالانترنت
            query = command.recognize_google(audio, language='en')
            print(f'you said : {query} ')
        except Exception as Error:
            return None
        return query.lower()


Speak('hello sir  Rakwan, say your commands please')
# ابقى استنى الصوت هذا معنى وايل مدام
while True:
    query = TakeCommands()
    if 'hello' in query:
        Speak('hello sir rakwan')
    if 'How are you' in query:
        Speak('am fine sir , and you')
    if 'open google' in query:
        Speak('ok sir')
        # انتظر 3 ثواني
        time.sleep(3)
        # افتح قوقل
        webbrowser.open_new_tab('https://www.google.com')

        """ https://stackoverflow.com/questions/28004954/python-speech-recognition-module-object-has-no-attribute-microphone/33032574#33032574 """
