import speech_recognition
import pyttsx3
import openai

class VoiceAssistant:
    def __init__(self, name="", sex="", speech_language=""):
        self.name = name
        self.sex = sex
        self.speech_language = speech_language
        self.recognition_language = ""
        self.chat_history = []  # Список для хранения истории общения

def setup_assistant_voice(assistant, tts_engine):
    voices = tts_engine.getProperty("voices")

    if assistant.speech_language == "ru":
        assistant.recognition_language = "en-US"
        voice_index = 1 if assistant.sex == "female" else 0
    else:
        assistant.recognition_language = "ru-RU"
        voice_index = 0

    tts_engine.setProperty("voice", voices[voice_index].id)

def play_voice_assistant_speech(text_to_speech, tts_engine):
    tts_engine.say(str(text_to_speech))
    tts_engine.runAndWait()

def record_and_recognize_audio(recognizer, microphone):
    with microphone:
        recognized_data = ""
        recognizer.adjust_for_ambient_noise(microphone, duration=2)
        
        try:
            print("Listening...")
            audio = recognizer.listen(microphone, timeout=3)
        except:
            print("Can you check if your microphone is on, please?")
            return None
        
        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()
        except speech_recognition.UnknownValueError:
            pass
        except speech_recognition.RequestError:
            print("Check your Internet Connection, please")

        return recognized_data

if __name__ == "__main__":
    tts_engine = pyttsx3.init()
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    assistant = VoiceAssistant(name="", sex="", speech_language="en")
    setup_assistant_voice(assistant, tts_engine)

    openai.api_key = "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"

    while True:
        voice_input = record_and_recognize_audio(recognizer, microphone)
        if voice_input is not None:
            print(voice_input)
            
            # Добавляем запрос в историю общения
            assistant.chat_history.append({"role": "user", "content": voice_input})
            
            end = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Вы - чат бот."},
                    {"role": "user", "content": voice_input}
                ] + assistant.chat_history  # Включаем историю в сообщения для модели
            )
            response = end.choices[0].message.content
            print(response)
            play_voice_assistant_speech(response, tts_engine)
