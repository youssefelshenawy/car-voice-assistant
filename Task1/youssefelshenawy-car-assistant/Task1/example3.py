#Here you should use the mic to enter the messages 
import speech_recognition as sr
from openai import OpenAI
import pyttsx3
import os


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
,  
)


def speak_text(text):
    
    engine = pyttsx3.init()

    engine.setProperty('rate', 150)  
    engine.setProperty('volume', 1.0)  
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    
    engine.say(text)

    engine.runAndWait()





def listen_and_convert_to_text(speaker):
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()

    # Set the microphone as the source of the audio
    with sr.Microphone() as source:
        print(f"{speaker}, please speak now...")
        speak_text(f"{speaker},please speak now")

        # Adjust for ambient noise and listen for audio input
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Use Google Web Speech API to recognize speech
            text = recognizer.recognize_google(audio)
            print(f"{speaker} said: {text}")
            speak_text(f"{speaker} said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            speak_text("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Sorry, there was an error with the API request.")
            speak_text("Sorry, there was an error with the API request.")
            return None





def chat_with_assistant():

    conversation = [
        {"role": "system", "content": "You are a voice assistant in a car that facilitate multi-user interactions."}
    ]


    speakers = ["Speaker 1", "Speaker 2"]

    inputs = [None, None]

    while True:
        for i, speaker in enumerate(speakers):
            while inputs[i] is None:  # Keep prompting the same speaker until valid input
                inputs[i] = listen_and_convert_to_text(speaker)
                if inputs[i] and inputs[i].lower() == "exit":
                    print("Conversation ended.")
                    speak_text("Conversation ended.")
                    return

            conversation.append({"role": "user", "content": f"{speaker}: {inputs[i]}"})
       

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            max_tokens=100,
            temperature=0.7
            )


        assistant_reply = response.choices[0].message.content
        conversation.append({"role": "assistant", "content": assistant_reply})
        print(f"Assistant: {assistant_reply}")
        speak_text(f"Assistant: {assistant_reply}")
        inputs = [None, None]
        


chat_with_assistant()
