import speech_recognition as sr

def listen_and_convert_to_text():
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()

    # Set the microphone as the source of the audio
    with sr.Microphone() as source:
        print("Please speak now...")

        # Adjust for ambient noise and listen for audio input
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Use Google Web Speech API to recognize speech
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Sorry, there was an error with the API request.")
            return None


def write_to_file(text):
    with open("conversation.txt", "a") as file:
        file.write(text + "\n")

# Continuously listen and convert speech to text
while True:
    recognized_text = listen_and_convert_to_text()
    
    if recognized_text:  # If text is recognized
        write_to_file(recognized_text)  # Store the recognized text in the file
        
        # Check if the user said "exit"
        if "exit" in recognized_text.lower():
            print("Exiting the program.")
            break  # Exit the loop if "exit" is detected