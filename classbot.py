import telepot

class library:
    def __init__(self, bot, chat_id, msg):
        self.bot = bot
        self.chat_id = chat_id
        self.msg = msg

    def check_command(self, msg):
        log = open('log_commands.txt', 'a')
        links = open('links.txt', 'a')
        adm_id = []

        try:
            user = '@' + self.msg['from']['username']
        except:
            user = self.msg['from']['first_name']

        if msg == '/start@lib':
            self.bot.sendMessage(self.chat_id, 'Hello sir.', reply_to_message_id=self.msg['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
            print('Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + '  __/start@lib__')
        elif msg == '/test@lib':
            self.bot.sendMessage(self.chat_id, 'Say.', reply_to_message_id=self.msg['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
            print('Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' __/test@lib__')
        elif msg == '/unpin@lib':
            self.bot.unpinChatMessage(self.chat_id)
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print('Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' __/unpin@lib__')
        elif msg == '/fix@lib':
            self.bot.pinChatMessage(self.chat_id, self.msg['reply_to_message']['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print('Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' __/fix@lib__')
        elif msg == '/ban@lib':
            try:
                usern = self.msg['reply_to_message']['from']['first_name']
            except:
                usern = self.msg['reply_to_message']['from']['first_name']
            self.bot.kickChatMember(self.chat_id, self.msg['reply_to_message']['from']['id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print('Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' __ban@lib__')
            print(str(user.encode('utf-8')) + ' has banned ' + str(usern.encode('utf-8')))
        elif msg == '/rt':
            try:
                reply_user = '@' + self.msg['reply_to_message']['from']['username']
            except:
                reply_user = self.msg['reply_to_message']['from']['first_name']
            self.bot.sendMessage(self.chat_id, user + ' concorda com ' + reply_user, reply_to_message_id=self.msg['message_id'])
        elif msg == '/help@lib':
            self.bot.sendMessage(self.chat_id, '[+]User commands[+]\n/myid@lib\n/id@lib\n/onionlink@lib\n/test@lib\n[+]Admin commands[+]\n/ban@lib\n/fix@lib\n/unpin@lib\n/addlink@lib\n/unban@lib\n/promote@lib', reply_to_message_id=self.msg['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
            print('Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' __/help@lib__')
        elif msg == '/src@lib':
            self.bot.sendMessage(self.chat_id, 'NotHere', reply_to_message_id=self.msg['message_id'])
        elif msg == '/pin@lib':
            if self.msg['from']['id'] == :
                self.bot.forwardMessage('@', self.chat_id, self.msg['reply_to_message']['message_id'])
                self.bot.sendMessage(self.chat_id, 'Ok sir.', reply_to_message_id=self.msg['message_id'])
                log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
                print('Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' __/forward@lib__')
            else:
                self.bot.sendMessage(self.chat_id, 'Fuck you bitch!', reply_to_message_id=self.msg['message_id'])
        elif msg == '/banid@lib':
            fw = self.msg.get('text').split()
            self.bot.kickChatMember(self.chat_id, fw[1])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
            print('Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' __/banid@lib__')
            print(str(user.encode('utf-8')) + ' has banned ' + str(usern.encode('utf-8')))
        elif self.msg.get('text').startswith('/addlink@lib'):
            if self.msg['from']['id'] == :
                damn = self.msg.get('text').split()
                damn2 = damn[1]
                links_reading = open('links.txt', 'r')
                links_read = links_reading.read()
                if '.onion' in str(damn2):
                    if damn2 in links_read:
                        self.bot.sendMessage(self.chat_id, 'File exists.', reply_to_message_id=self.msg['message_id'])
                    else:
                        fuck = links.write(str(damn[1] + ' '))
                        fuckk = links.write(str('  | ' + ' '.join(damn[2:]) + ' |\n'))
                        self.bot.sendMessage(self.chat_id, 'Ok sir.', reply_to_message_id=self.msg['message_id'])
                        log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
                        print('Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' __/addlink@lib__')
                else:
                    self.bot.sendMessage(self.chat_id, 'Fuck you bitch!', reply_to_message_id=self.msg['message_id'])
            else:
                self.bot.sendMessage(self.chat_id, 'Fuck you bitch!', reply_to_message_id=self.msg['message_id'])
        elif msg == '/id@lib':
            self.bot.sendMessage(self.chat_id, self.msg['reply_to_message']['from']['id'], reply_to_message_id=self.msg['message_id'])
        elif msg == '/onionlink@lib':
            opn = open('links.txt', 'r')
            opn_read = opn.read()
            self.bot.sendMessage(self.chat_id, opn_read, reply_to_message_id=self.msg['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
            print('Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' __/onionlink@lib__')
        elif msg == '/myid@lib':
            self.bot.sendMessage(self.chat_id, self.msg['from']['id'], reply_to_message_id=self.msg['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
            print('Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' __/myid@lib__')
        elif msg == '/unban@lib':
            try:
                fodeu = '@' + self.msg['reply_to_message']['from']['username']
            except:
                fodeu = self.msg['reply_to_message']['from']['first_name']
            self.bot.unbanChatMember(self.chat_id, self.msg['reply_to_message']['from']['id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print('Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' __/unban@lib__')
            print(str(user.encode('utf-8')) + ' has unbanned ' + str(fodeu.encode('utf-8')))
        elif msg == '/promote@lib':
            try:
                promoted = '@' + self.msg['reply_to_message']['from']['username']
            except:
                promoted = self.msg['reply_to_message']['from']['first_name']
            self.bot.promoteChatMember(self.chat_id, self.msg['reply_to_message']['from']['id'], can_change_info=True, can_post_messages=False, can_edit_messages=False, can_delete_messages=True, can_invite_users=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True)
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print('Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' __/promote@lib__')
            print(str(user.encode('utf-8')) + ' has promoted ' + str(promoted.encode('utf-8')))
        elif self.msg.get('text').startswith('/title@lib'):
            mensagem = self.msg.get('text').split()
            mensagem2 = mensagem[1:]
            self.bot.setChatTitle(self.chat_id, ' '.join(mensagem2).encode('utf-8'))
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print('Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' __/title@lib__')
            print(str(user.encode('utf-8')) + ' has changed the name of ' + str(self.chat_id))
