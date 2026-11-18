# #8-9 Messages
# text_messages = ["Message one - bla", "Message two - blabla", "Message three - b"]

# def short_text_messages(texts):
#     """Function which prints short text messages"""
#     for text in texts:
#         msg = f"{text}"
#         print(text)

# short_text_messages(text_messages)

#8-10 Sending Messages


# unsent_messages = ["Message one", "Message two", "Message three"]
# sent_messages = []

# def short_text_messages(unsent_messages, sent_messages):
#     """Function which prints short text messages"""
#     print(f"\nUnsent messages: {unsent_messages}")
#     while unsent_messages:
#         send_message = unsent_messages.pop()
#         print(f"\tSending a message {send_message}")
#         sent_messages.append(send_message) #the algoritm behind this is: 1) name of an empty list 2) the append function 
#         #3) thing I want to append

#     print(f"\nUnsent messages after sending: {unsent_messages}")
#     print(f"Sent messages: {sent_messages}")

# short_text_messages(unsent_messages, sent_messages)

#8-11 Archived messages

unsent_messages = ["Message one", "Message two", "Message three"]
sent_messages = []

def short_text_messages(unsent_messages, sent_messages):
    """Function which prints short text messages"""
    print(f"\nUnsent messages: {unsent_messages}")
    while unsent_messages:
        send_message = unsent_messages.pop()
        print(f"\tSending a message {send_message}")
        sent_messages.append(send_message) 

short_text_messages(unsent_messages[:], sent_messages)

print(f"\nUnsent copied messages after sending: {unsent_messages}")
print(f"Copied sent messages: {sent_messages}")


short_text_messages(unsent_messages, sent_messages)

print(f"\nUnsent original messages after sending: {unsent_messages}")
print(f"Original sent messages: {sent_messages}")
