from services.nvidia import llm

def get_response(msg):
    response = llm.invoke(msg.message)
    return response.content