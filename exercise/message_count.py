message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
print(message,type(message))
msg_dict=dict()
for msg in message:
    msg_dict[msg] = message.count(msg)

print(msg_dict)
