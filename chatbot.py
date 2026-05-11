# Elementary Customer Support Chatbot

print("===================================")
print(" Welcome to Online Shopping Bot ")
print(" Type 'exit' to end chat ")
print("===================================")

while True:

    user = input("\nYou: ").lower()

    # Exit condition
    if user == "exit":
        print("Bot: Thank you for visiting our store!")
        break

    # Greetings
    elif "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you today?")

    # Order status
    elif "order" in user:
        print("Bot: Please enter your order ID on our website to track your order.")

    # Delivery information
    elif "delivery" in user or "shipping" in user:
        print("Bot: Delivery usually takes 3-5 business days.")

    # Payment methods
    elif "payment" in user:
        print("Bot: We accept Credit Card, Debit Card, UPI, and Net Banking.")

    # Return policy
    elif "return" in user:
        print("Bot: Products can be returned within 7 days of delivery.")

    # Product availability
    elif "available" in user or "stock" in user:
        print("Bot: Please check product availability on the product page.")

    # Default response
    else:
        print("Bot: Sorry, I didn't understand your query.")