import random
import requests

print(" Hello! I'm your chatbot.")
print("Type 'bye' whenever you want to exit.")

# Fun facts the chatbot can choose from randomly
fun_facts = [
    "Octopuses have three hearts.",
    "Honey can last for thousands of years without spoiling.",
    "A group of flamingos is called a flamboyance.",
    "Bananas are berries, but strawberries are not."
]

def get_weather(city):
    api_key = "867627333ccb51be25ff7c3999adbc7b"

    url = "https://api.openweathermap.org/data/2.5/weather"

    parameters = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=parameters)

        if response.status_code == 404:
            return "I couldn't find that city."
        
        if response.status_code != 200:
            #print("Status code:", response.status_code)
            #print("Response:", response.text)
            return "Weather request failed."

        
        
        data = response.json()

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]

        return f"The weather in {city.title()} is {description}, {temperature}°C. It feels like {feels_like}°C."

    except requests.exceptions.RequestException:
        return "I couldn't connect to the weather service."
    

def calculate_math(expression):
    try:
        # Remove the word "calculate" or "math" if the user included it
        expression = expression.replace("calculate", "").replace("math", "").replace("solve", "").strip()

       
        for operator in ["+", "-", "*", "/"]:
            if operator in expression:
                parts = expression.split(operator)

                if len(parts) != 2:
                    return "Please give me a simple calculation, like 5 + 3."

                number1 = float(parts[0].strip())
                number2 = float(parts[1].strip())

                if operator == "+":
                    result = number1 + number2
                elif operator == "-":
                    result = number1 - number2
                elif operator == "*":
                    result = number1 * number2
                elif operator == "/":
                    if number2 == 0:
                        return "You can't divide by zero!"

                    result = number1 / number2

                # Display whole numbers without .0
                if result.is_integer():
                    return str(int(result))

                return str(result)

        return "I can calculate using +, -, *, and /."

    except ValueError:
        return "Please enter numbers, like: calculate 10 + 5."



while True:
    # Get input from the user and convert it to lowercase
    user_input = input("You: ").lower().strip()

    # Error handling for an empty input
    if user_input == "":
        print("Bot: Please type something so I can help you.")

    # Goodbye
    elif "bye" in user_input or "goodbye" in user_input:
        print("Bot: Goodbye! Have a great day!")
        break  

    #greetings 
    elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("Bot: Hello! How can I help you today?")


    # Name
    elif "name" in user_input or "who are you" in user_input:
        print("Bot: I'm a simple Python chatbot!")

    # Weather
    elif "weather" in user_input or "forecast" in user_input or "temperature" in user_input:
        city = input("Bot: What city? ").strip()
        print("Bot:", get_weather(city))


    # Help
    elif "help" in user_input or "support" in user_input:
        print("Bot: I can help with weather, facts, math, and more!")

    # Random fact
    elif "fact" in user_input or "facts" in user_input:
        print("Bot:", random.choice(fun_facts))

    # Another keywords
    elif "thank" in user_input:
        print("Bot: You're welcome! ")
        print("Bot: Is there anything else I can help you with?")

    elif "joke" in user_input:
        print("Bot: Why did the computer go to the doctor? Because it caught a virus!")
       
    # Math 
    elif "calculate" in user_input or "math" in user_input or "solve" in user_input:
        print("Bot:", calculate_math(user_input))

    # Unknown input error handling
    else:
        print("Bot: I'm sorry, I don't understand that.") 

