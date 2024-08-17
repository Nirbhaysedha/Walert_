from simplegmail import Gmail
from read_email import Recieptent,Sender,Subject,date
from RAG import message

def SEND(message,Recieptent,Sender,Subject):
    gmail = Gmail()
    message = message.replace("\n", "<br>")
    params = {
            "to": Recieptent,
            "sender": Sender,
            "subject": f"REPLY TO :{Subject}",
            "msg_html": message
        }


    try:
        gmail.send_message(**params) 
        return True
    except Exception as e:
        print(f"Not able to send the email{e}")



