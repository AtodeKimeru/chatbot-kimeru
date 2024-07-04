from rivescript import RiveScript

bot = RiveScript()
bot.load_file("welcome1.rive")
bot.sort_replies()

while True:
    message = input("You: ")
    if message == "quit":
        break

    reply = bot.reply("localuser", message)
    print("Bot: " + reply)