#Here you should write the messages 
from openai import OpenAI
import os


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
,  
)

def chat_with_assistant():

    conversation = [
        {"role": "system", "content": "You are a voice assistant in a car that facilitate multi-user interactions."}
    ]


    speakers = ["Speaker 1", "Speaker 2"]

    while True:

        for speaker in speakers:
            user_input = input(f"{speaker}: ")
            if user_input.lower() == "exit":
                print("Conversation ended.")
                return
            
            conversation.append({"role": "user", "content": f"{speaker}: {user_input}"})

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=conversation,
                max_tokens=100,
                temperature=0.7
            )


        assistant_reply = response.choices[0].message.content
        conversation.append({"role": "assistant", "content": assistant_reply})
        print(f"Assistant: {assistant_reply}")


chat_with_assistant()
