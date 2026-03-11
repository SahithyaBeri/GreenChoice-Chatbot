from chatbot.rag_chatbot import generate_response
from automation.relay_webhook import send_to_relay

def chatbot():

    print("Sustainable Shopping Assistant")
    print("Type 'exit' to stop")

    while True:

        query = input("You: ")

        if query == "exit":
            break

        response = generate_response(query)

        print(response)

        try:
            status = send_to_relay(query, response)
            print("Relay status:", status)
        except:
            print("Relay not connected")

chatbot()