from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/webhook/', methods=['POST', 'GET'])
def webhook_whatsapp():
   
    if request.method == 'GET':
      
        if request.args.get('hub.verify_token') == 'AgroConnection':
            return request.args.get('hub.challenge')
        else:
            return 'authentication error'
      
    data = request.get_json()
    
    message = 'Telefono:'+data['entry'][0]['changes'][0]['value']['messages'][0]['from']
    message += '|Mensaje:'+data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']

    if message is not None:

        from rivescript import RiveScript

        bot = RiveScript()

        bot.load_file('welcome.rive')
        bot.sort_replies()
        
        # get the answers
        answer = bot.reply('localuser', message)
        answer = answer.replace('\\n', '\\\n')
        answer = answer.replace('\\', '')

        # save the conversation
        conversation = message + '\n' + answer + '\n\n'

        f = open('text.txt', 'w')
        f.write(conversation)
        f.close()

        return jsonify({'status': 'success'}), 200


if __name__ == "__main__":
    app.run(debug=True)

