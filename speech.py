import speech_recognition as sr
import openai
openai.api_key = "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"
messages = []
def recognize_speech():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google_cloud(audio)
        return text
    except sr.RequestError as e:
        print(f"Could not process: {e}")
    except sr.UnknownValueError:
        print("Unknown value error")
    return None

def chatbot_interaction(message):
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content # type: ignore
        print(f"Bot: {reply}")
        messages.append({"role": "assistant", "content": reply})

def main():
   
    while True:
        user_input = recognize_speech()
        if user_input:
            chatbot_interaction(user_input)
        

if __name__ == "__main__":
    main()
