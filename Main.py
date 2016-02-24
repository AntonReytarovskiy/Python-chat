from Message import Message

name = raw_input('Enter name: ')
while True:
    command = raw_input('Enter command: ')
    if command == 'chat':
        for msg in Message.select():
            print msg

    elif command == 'message' or command == 'msg':
        Message.create(name=name,
                       text_message=raw_input('Enter message: '))

    elif command == 'rename':
        name = raw_input('Enter name: ')

    elif command == 'help':
        print 'Commands: "chat" - View chat!  ' \
              '"msg or message" - Send message!  ' \
              '"rename" - change name  ' \
              '"Exit or exit" - exit application'

    elif command == 'Exit' or command == 'exit':
        print 'goodbye'
        break

    else:
        print 'command not found!'