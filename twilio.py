from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC595067541a156778084cf66e691588b2"
# Your Auth Token from twilio.com/console
auth_token  = "b3a7d86b7672ec508b11063af82f0173"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8613147032447", 
    from_="+12562989011",
    body="中文有用吗？")

print(message.sid)
