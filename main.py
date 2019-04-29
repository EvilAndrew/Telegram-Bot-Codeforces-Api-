import telebot
import requests
import time

from telebot.types import Message

from user import UserInfo
from contest import ContestInfo
from common import CommonInfo


# Initialization of objects of classes from user.py
user_info = UserInfo()


# from common.py
common_info = CommonInfo()


# from contest.py
contest_info = ContestInfo()


# Initialization of the bot by its secret token
bot = telebot.TeleBot('818264169:AAEfiWcmpeHnXoNkFBFkZ-IYAUsjSxJzLzw')


url = "http://codeforces.com/api/"

# A telegram-bot cannot start any conversation
# That was done by telegram's developers in order to prevent spam from bots
# That's why we need to start a conversation from /start, then the bot starts working

@bot.message_handler(commands=['start'])
def start_conversation(message: Message):
    answer = ''

    answer += "/find_user \tif you want to know information about the user\n\n"
    answer += "/find_contest \tif you want to know id of the contest by its title\n\n"
    
    answer += "/rating_of \tif you want to know current rating of the user\n\n"
    answer += "/max_rating_of \tif you want to know maximum rating of the user\n\n"
    
    answer += "/max_rank_of \tif you want to know maximum rank of the user\n\n"
    answer += "/place_in_contest \tif you want to know exact place of the user in the contest\n\n"

    answer += "/is_solved \tif you want to know whether some user solved exact problem (type problem handle)\n\n"
    answer += "/how_many_friends \tif you want to know exact number of people whose friend the user is\n\n"
    
    answer += "/color_of \tif you want to know what color has the user right now\n\n"
    answer += "/colour_of \tif you want to know what colour has the user right now\n\n"
    
    answer += "/color_of_number \tif you want to know what color does the number mean\n\n"
    answer += "/colour_of_number \tif you want to know what colour does the number mean\n\n"
    
    answer += "/number_of_problems \tif you want to know how many problems are there in total\n\n"
    answer += "/problems_with_tag \tif you want to know how many problems are there in total with the tag\n\n"
    
    answer += "/current_rank_of \tif you want to know current rank of the user\n\n"
    answer += "/rank_of \tif you want to know current rank of the user\n\n"

    answer += "/number_of_problems_with_tag \tif you want to know how many problems are there in total with the tag\n\n"
    answer += "/contest_link \tif you want to know link to the contest by its title\n\n"

    answer += "/profile_link \tif you want to know link to the profile by its handle\n\n"
    answer += "/problem_link \tif you want to know link to the problem by its title\n\n"

    answer += "If there is no such command, or handle, or title of contest, you will get -1 as answer, or message meaning error\n\n"

    bot.reply_to(message, answer)


# If you need to get a link to profile of some user

@bot.message_handler(commands=['profile_link'])
def link_by_handle(message: Message):
    a = ' '.join(message.text.split()[1:]).rstrip(' ').rstrip('\n')
    answer = user_info.link_to_user(a)
    bot.reply_to(message, str(answer))


# If you need to get a link to problem by its title

@bot.message_handler(commands=['problem_link'])
def link_to_problem(message: Message):
    a = ' '.join(message.text.split()[1:]).rstrip(' ').rstrip('\n')
    answer = common_info.link_to_problem(a)
    bot.reply_to(message, str(answer))

# The same, but with contest

@bot.message_handler(commands=['contest_link'])
def link_to_contest(message: Message):
    a = ' '.join(message.text.split()[1:]).rstrip(' ').rstrip('\n')
    answer = contest_info.link_to_contest(a)
    bot.reply_to(message, str(answer))


# Replying with user's current rating and his/her avatar

@bot.message_handler(commands=['find_user'])
def find_user(message: Message):
    a = ' '.join(message.text.split()[1:]).rstrip(' ').rstrip('\n')
    answer = user_info.find_handle(a)
    
    if answer[0] == -1:
        bot.reply_to(message, str(answer[0]))
        return
    
    bot.reply_to(message, str(answer[0]) + '\n' + str(answer[1]).lstrip("//"))


# Replying with contest's id

@bot.message_handler(commands=['find_contest'])
def find_contest(message: Message):
    a = ' '.join(message.text.split()[1:]).rstrip(' ').rstrip('\n')
    answer = contest_info.find_contest(a)
    bot.reply_to(message, answer)


# Replying with user's current rating

@bot.message_handler(commands=['rating_of'])
def get_rating(message: Message):
    a = ' '.join(message.text.split()[1:]).rstrip(' ').rstrip('\n')
    answer = user_info.find_handle(a)
    bot.reply_to(message, str(answer[0]))


# Replying with user's maximum rating

@bot.message_handler(commands=['max_rating_of'])
def get_max_rate(message: Message):
    a = ' '.join(message.text.split()[1:]).rstrip(' ').rstrip('\n')
    answer = user_info.max_rating_of_user(a)
    bot.reply_to(message, str(answer))


# Replying with user's maximum rank

@bot.message_handler(commands=['max_rank_of'])
def get_max_rank(message: Message):
    a = ' '.join(message.text.split()[1:]).rstrip(' ').rstrip('\n')
    answer = user_info.max_rank_of_user(a)
    bot.reply_to(message, str(answer))


# Replying with user's current rank

@bot.message_handler(commands=['rank_of', 'current_rank_of'])
def get_rank(message: Message):
    a = ' '.join(message.text.split()[1:]).rstrip(' ').rstrip('\n')
    answer = user_info.get_rank(a)
    bot.reply_to(message, str(answer))


# Replying with user's place in the contest (ranking)

@bot.message_handler(commands=['place_in_contest'])
def get_place_in_contests(message: Message):
    contest = ' '.join(message.text.split()[1:-1]).rstrip(' ').rstrip('\n')
    handle = message.text.split()[-1].rstrip(' ').rstrip('\n')
    answer = user_info.place_in_contest(contest, handle)
    bot.reply_to(message, str(answer))


# Replying 'solved' if the user has solved the problem, otherwise - 'not solved'

@bot.message_handler(commands=['is_solved'])
def get_solved(message: Message):
    problem = ' '.join(message.text.split()[1:-1]).rstrip(' ').rstrip('\n')
    handle = message.text.split()[-1].rstrip(' ').rstrip('\n')
    answer = user_info.is_solved(handle, problem)
    bot.reply_to(message, str(answer))


# Replying with the user's number of friends

@bot.message_handler(commands=['how_many_friends'])
def how_many_friends(message: Message):
    a = ' '.join(message.text.split()[1:]).rstrip(' ').rstrip('\n')
    answer = user_info.how_many_friend(a)
    bot.reply_to(message, str(answer))


# Replying with the user's current rating and color

@bot.message_handler(commands=['color_of', 'colour_of'])
def get_color_of(message: Message):
    a = ' '.join(message.text.split()[1:]).rstrip(' ').rstrip('\n')
    answer = user_info.what_color_is_user(a)
    bot.reply_to(message, str(answer))


# Replying with the number's color

@bot.message_handler(commands=['color_of_number', 'colour_of_number'])
def get_color_of_number(message: Message):
    a = ' '.join(message.text.split()[1:]).rstrip(' ').rstrip('\n')
    answer = common_info.what_color_is_number(a)
    bot.reply_to(message, str(answer))


# Replying with the count of problems totally

@bot.message_handler(commands=['number_of_problems'])
def problems_at_all(message: Message):
    answer = common_info.how_many_problems_at_all()
    bot.reply_to(message, str(answer))


# Replying with the number of problems with the tag

@bot.message_handler(commands=['problems_with_tag', 'number_of_problems_with_tag'])
def problems_at_all(message: Message):
    a = ' '.join(message.text.split()[1:]).rstrip(' ').rstrip('\n')
    answer = common_info.how_many_problems_at_all(a)
    bot.reply_to(message, str(answer))


# If no one of commands is appropriate, then there is no such command

@bot.message_handler(func=lambda message: True)
def is_it_error(message: Message):
    bot.reply_to(message, "There is no such command")


if __name__ == '__main__':
    while True:
        try:
            bot.polling()
        except:
            time.sleep(1)
