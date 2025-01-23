import os 
from openai import OpenAI

client = OpenAI()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")


def search_word_information():
    prompt = """
You are a helpful assistant facilitating a conversation between two users who have different dining preferences.
- Speaker 1 wants burgers near Sendlinger Tor.
- Speaker 2 wants something healthy instead.
Your goal is to suggest a nearby restaurant that satisfies both preferences. Be specific and provide a name or type of restaurant.

Speaker 1: Hey car, I want to get some burgers close to Sendlinger Tor.
Speaker 2: No no! I had burgers yesterday. Let’s get something more healthy instead.
Assistant:"""


    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    

    generated_text = response.choices[0].text
    print(generated_text)

search_word_information()