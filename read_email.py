from simplegmail import Gmail
from simplegmail.query import construct_query


def READ():
    gmail = Gmail()


    query_params = {
        "newer_than": (1, "day")  
    }

    messages = gmail.get_messages(query=construct_query(query_params))


    if messages:
        latest_message = max(messages, key=lambda m: m.date)  # Get the latest email by date
        Recieptent=latest_message.recipient
        Sender=latest_message.sender
        Subject=latest_message.subject
        date=latest_message.date
        snippet=latest_message.snippet
        content_to_write = f"""
        # Email content from {latest_message.date}
        email_content = '''{latest_message.plain}'''
        """
        with open("email_content.txt", "w") as f:
            f.write(content_to_write)
            print("Email content written to email_content.py.")
            return Recieptent,Sender,date,snippet,Subject
    else:
        print("No messages found.")


Recieptent,Sender,date,snippet,Subject=READ()

