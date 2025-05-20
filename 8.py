import openai

def generate_response(user_input):
    try:
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "system", "content": "Assume the role of a marketing assistant, and think step by step. Your name is MarkBot."},
                        {"role": "user", "content":user_input}]

        )

        response_text = completion['choices'][0]['message']['content']
        return response_text
    except Exception as e:
        print("Error generating response:", e)
        return "I'm sorry, I couldn't generate a response."

def main():
    openai.api_key = " - " #put api key
    print("\n welcome to MarkBot – Your Marketing Assistant! Type 'quit' to exit.\n")

    while True:
        user_input = input("Ask a marketing question: ")

        if user_input.lower() == "quit":
            print("Exiting MarkBot.")
            break

        response = generate_response(user_input)

        print("MarkBot:", response)

if __name__ == "__main__":
    main()