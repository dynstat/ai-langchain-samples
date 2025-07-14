import webview
from chat_ai import getairesponse

class Api:
    def __init__(self):
        self.history = []

    def send_message(self, message):
        response = getairesponse(message)
        if not response:
            response = {"response": "No response from AI", "status": 1}
        self.history.append({"user": message, "bot": response['response']})
        return response['response']

api = Api()

if __name__ == '__main__':
    webview.create_window('ChatGPT GUI', 'index.html', js_api=api, width=500, height=700)
    webview.start()