import ollama

def llm(question):
    response = ollama.chat(model='gemma:2b', messages=[
    {
        'role': 'user',
        'content': question,
    },
    ])
    return response['message']['content']

def system(question):
    response = ollama.chat(model='gemma:2b', messages=[
    {
        'role': 'system',
        'content': question,
    },
    ])
    return response['message']['content']

def AI(question):
    response = ollama.chat(model='gemma:2b', messages=[
    {
        'role': 'assistant',
        'content': question,
    },
    ])
    return response['message']['content']

