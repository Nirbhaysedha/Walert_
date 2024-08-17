from read_email import READ
from RAG import Inference
from send_emai import SEND
from llms import llm



def Pipeline(llm,USER_QUERY):
    Recieptent,Sender,date,snippet,Subject=READ()
    message=Inference(llm,USER_QUERY)
    flag=SEND(message,Recieptent,Sender,Subject)
    return flag


def main(llm):
    with open("/Users/nirbhaysedha/Desktop/walert/email_content.txt","r") as f:
        USER_QUERY=f.read()
    Pipeline(llm,USER_QUERY)

main(llm)

