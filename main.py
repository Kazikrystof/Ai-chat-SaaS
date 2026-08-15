import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

print("Ahoj s čím ti mohu pomoci?")

with open("test_produkt.json", "r", encoding="utf-8") as file:
    products = json.load(file)


chat_history_client = []  
chat_history_ai = []  


while True:
    user_message = input("Ty: ")
    print("")

    if user_message.lower().strip() == "exit":
        break

    response = client.responses.create(
        model="gpt-5.6-luna",
        instructions="""
        Jsi AI asistent.
        Odpovídej vždy česky, přátelsky ale profesionálně vykej mi.
        Buď stručný.
        Pokud něco nevíš, řekni, že to nevíš.
        Nikdy si nevymýšlej fakta.
        Používej emoji, nepouživej tučný text.
            """,
        input = F"""produkty v na skladu: {products}
            Dotaz zákazníka: {user_message}
            Historie chatu od uživatele: {chat_history_client}
            Historie chatu od tebe: {chat_history_ai}""")
    
    chat_history_client.append(user_message)
    chat_history_ai.append(response.output_text)    
   
    print("AI:", response.output_text)
    print("")
