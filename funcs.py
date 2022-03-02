from telegram import Chat, ChatMember
from config import SUDO_USERS 

def is_support_plus(chat: Chat, user_id: int, member: ChatMember = None) -> bool: 
  return user_id in SUDO_USERS
