import random
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from datetime import datetime

token_file = open("token.txt")
token = token_file.readline().strip()
group_id = token_file.readline().strip()

vk_session = vk_api.VkApi(token=token)

def send_user(id: int, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})

def send_chat(id: int, text):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})

def send_group(id: int, text):
    vk_session.method('messages.send', {'group_id': id, 'message': text, 'random_id': 0})

def is_command(text: str) -> bool:
    if (text[0] == '/'):
        return True
    return False

def generate_cock_size() -> int:
    return random.randint(0, 22)

def main():
    while True:
        try:
            longpoll = VkBotLongPoll(vk_session, int(group_id))
            for event in longpoll.listen():
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        now = datetime.now()
                        current_time = now.strftime("%d %b %H:%M:%S")
                        print(current_time)
                        msg = event.object.message['text'].lower()
                        print('Текст:', msg)
                        if not is_command(msg):
                            continue
                        if msg[1:] == "cock":
                            size = generate_cock_size()
                            text = "Your cock size is " + str(size) + "cm!\n"
                            if size >= 0:
                                text += "c" + "=" * size + "3"
                            print("Cock command found!")
                            if event.from_user:
                                send_user(int(event.object.message['from_id']), text)
                            if event.from_chat:
                                send_chat(int(event.chat_id), text)
                        print()
        except Exception:
            print("Caught an exception")

if __name__ == '__main__':
    main()