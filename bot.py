from pyrogram import Client, Filters, Emoji, MessageHandler, InputPhoneContact
from func_lists import *

app = Client("shanelka")

MENTION = "[{}](tg://user?id={})"
msg_count_dict = {}
end_chat_msg_count_dict = {}

with app:
    app.send_message("me", "BOT RESTARTED...!")
    contacts = app.get_contacts()
    contact_list = []
    for count in range(len(contacts)):
        contact_list.append(contacts[count]["id"])

# create contact id txt file as "contact_list.txt"
with open("contact_list.txt", "w") as f:
    for con in contact_list:
        f.write(str(con)+"\n")

# adding contact id list to "allow_list.txt"
with open("allow_list.txt", "w") as f:
    for con in contact_list:
        f.write(str(con)+"\n")

contact_list.clear()

with app:
    me = app.get_me()
    my_id = (me.id)
    # Me adding to my contact and allow lists
    add_allow_list((str(my_id)))
    add_contacts_list((str(my_id)))

#------------------------------------------------------------------------------------------------------------------#


#@app.on_message(Filters.text & Filters.incoming & Filters.private & Filters.regex("Hi"))
#def hello(client, message):
#    app.send_chat_action(message.chat.id, "typing")
#    message.reply_text("`Hello,` {} {}".format(MENTION.format(message.chat.first_name, message.chat.id), Emoji.SMILING_FACE))

#@app.on_message(Filters.text & Filters.private & Filters.incoming & (Filters.regex("Good Morning") | Filters.regex("good morning") | Filters.regex("Good morning")), group=1)
#ef GM(client, message):
#    app.send_chat_action(message.chat.id, "typing")
#    message.reply_text("`Good morning...!` {}  {}".format(Emoji.RED_HEART, MENTION.format(message.chat.first_name, message.chat.id)))

@app.on_message(Filters.incoming & Filters.private & ~Filters.service & ~Filters.bot)
def new_message(client, message):
    

    if not (search_contacts(str(message.from_user.id))) and not (search_allow_list(str(message.from_user.id))):
        msg_count_dict.setdefault(message.chat.id, [0])
        msg_count_dict[message.chat.id].append(0)
        #print(msg_count_dict)

        if len(msg_count_dict[message.chat.id]) != 11:
            app.delete_messages(message.chat.id, (message.message_id - 1))
            app.send_chat_action(message.chat.id, "typing")
            message.reply_text("""
            `You are not in my contacts.
Please wait until I respond `{}`.
Don't spam my PM`
`If you send me` **[** {} **]** `more messages you will automatically be Blocked` {}""".format(MENTION.format(message.chat.first_name, message.chat.id), 11 - (len(msg_count_dict[message.chat.id])), Emoji.WARNING))
        
        elif len(msg_count_dict[message.chat.id]) == 11:
            app.send_chat_action(message.chat.id, "typing")
            message.reply_text("`You are Blocked due SPAM` {}".format(Emoji.SMIRKING_FACE))
            app.block_user(message.chat.id)
            add_block_list(str(message.from_user.id))
            msg_count_dict.update({message.chat.id : [0]})
    else:
        pass

@app.on_message(Filters.incoming & Filters.private & ~Filters.bot, group=1)
def after_end_chat(client, message):
    if (search_end_chat_list(str(message.from_user.id))):
        end_chat_msg_count_dict.setdefault(message.chat.id, [0])
        end_chat_msg_count_dict[message.chat.id].append(0)
        #print(end_chat_msg_count_dict)

        if len(end_chat_msg_count_dict[message.chat.id]) == 3 :
            app.send_chat_action(message.chat.id, "typing")
            message.reply_text("`Hi, `{}` I will get back to you soon!`".format(MENTION.format(message.chat.first_name, message.chat.id)))

        elif len(end_chat_msg_count_dict[message.chat.id]) == 6:
            app.send_chat_action(message.chat.id, "typing")
            message.reply_text("{} `Please don't spam my PM`".format(Emoji.WARNING))

        elif len(end_chat_msg_count_dict[message.chat.id]) == 11:
            app.send_chat_action(message.chat.id, "typing")
            message.reply_text("{} `SPAM Warning` {}".format(Emoji.STOP_SIGN, Emoji.STOP_SIGN))
        
        elif len(end_chat_msg_count_dict[message.chat.id]) == 16:
            app.send_chat_action(message.chat.id, "typing")
            message.reply_text("{} `SPAM Warning` {}".format(Emoji.STOP_SIGN, Emoji.STOP_SIGN))
        
        elif len(end_chat_msg_count_dict[message.chat.id]) == 21:
            app.send_chat_action(message.chat.id, "typing")
            message.reply_text("`You are Blocked due SPAM` {}".format(Emoji.SMIRKING_FACE))
            app.block_user(message.chat.id)
            add_block_list(str(message.from_user.id))
            remove_end_chat_list((str(message.chat.id)))
            remove_allow_list((str(message.chat.id)))
            remove_contacts_list((str(message.chat.id)))
            end_chat_msg_count_dict.update({message.chat.id : [0]})
        else:
            pass

@app.on_message(Filters.outgoing & Filters.private, group=2)
def if_i_reply_to_end_chat(client, message):
    if (search_end_chat_list(str(message.chat.id))):
        remove_end_chat_list((str(message.chat.id)))
        end_chat_msg_count_dict.update({message.chat.id : [0]})
        #print(end_chat_msg_count_dict)
    else:
        pass

@app.on_message(Filters.outgoing & Filters.private & ~Filters.contact & ~Filters.bot, group=3)
def if_i_reply(client, message):
    if not(search_contacts(str(message.chat.id))) and not(search_allow_list(str(message.chat.id))):
        #app.edit_message_text(message.chat.id, (message.message_id - 1), "{}` approved to PM!`".format(MENTION.format(message.chat.first_name, message.chat.id))) 
        app.delete_messages(message.chat.id, message.message_id)
        app.send_chat_action(message.chat.id, "typing")
        message.reply_text("{}` approved to PM!`".format(MENTION.format(message.chat.first_name, message.chat.id)))
        add_allow_list((str(message.chat.id)))
        remove_block_list((str(message.chat.id)))
        add_contacts_list((str(message.chat.id)))
        msg_count_dict.update({message.chat.id : [0]})
        end_chat_msg_count_dict.update({message.chat.id : [0]})
    else:
        pass

#---------------------------------------------- OUT COMMANDS ------------------------------------------------------#

# Chat end with bye message
@app.on_message(Filters.text & Filters.outgoing & Filters.private & Filters.command(["bye"]), group=4)
def end_chat_bye(client, message):
    app.edit_message_text(message.chat.id, (message.message_id),"{}` has closed the chat bye `{} {}".format(MENTION.format(message.from_user.first_name, message.from_user.id), MENTION.format(message.chat.first_name, message.chat.id), Emoji.HUGGING_FACE))
    add_end_chat_list((str(message.chat.id)))
    end_chat_msg_count_dict.update({message.chat.id : [0]})

# Chat end without message
@app.on_message(Filters.text & Filters.outgoing & Filters.private & Filters.command(["end"]), group=5)
def end_chat(client, message):
    app.delete_messages(message.chat.id, message.message_id)
    #app.edit_message_text(message.chat.id, (message.message_id),"{}` has closed the chat bye `{}".format(MENTION.format(message.from_user.first_name, message.from_user.id), MENTION.format(message.chat.first_name, message.chat.id)))
    add_end_chat_list((str(message.chat.id)))
    end_chat_msg_count_dict.update({message.chat.id : [0]})

# Block user
@app.on_message(Filters.text & Filters.outgoing & Filters.private & Filters.command(["block"]), group=6)
def block(client, message):
    app.edit_message_text(message.chat.id, (message.message_id),"`Sorry, `{}` I'm blocking you `{}".format(MENTION.format(message.chat.first_name, message.chat.id), Emoji.SAD_BUT_RELIEVED_FACE))
    app.block_user(message.chat.id)
    add_block_list(str(message.chat.id))
    remove_allow_list((str(message.chat.id)))
    remove_contacts_list((str(message.chat.id)))
    end_chat_msg_count_dict.update({message.chat.id : [0]})
    msg_count_dict.update({message.chat.id : [0]})

# Delete contact
@app.on_message(Filters.text & Filters.outgoing & Filters.private & Filters.command(["delete"]), group=7)
def delete_contact(client, message):
    app.delete_messages(message.chat.id, message.message_id)
    app.delete_contacts([message.chat.id])
    remove_allow_list((str(message.chat.id)))
    remove_contacts_list((str(message.chat.id)))

# Bot Update
@app.on_message(Filters.me & Filters.text & Filters.incoming & Filters.command(["update"]), group=8)
def bot_update(client, message):
    app.send_message("me", "BOT Updating...!")
    clear_contacts_list()
    clear_allow_list()

    #with app:
    me = app.get_me()
    my_id = (me.id)

    contacts = app.get_contacts()
    update_contact_list = []
    for count in range(len(contacts)):
        update_contact_list.append(contacts[count]["id"])
    
    # create contact id txt file as "contact_list.txt"
    with open("contact_list.txt", "w") as f:
        for con in update_contact_list:
            f.write(str(con)+"\n")

    # adding contact id list to "allow_list.txt"
    with open("allow_list.txt", "w") as f:
        for con in update_contact_list:
            f.write(str(con)+"\n")
    
    update_contact_list.clear()

    # Me adding to my contact and allow lists
    add_allow_list((str(my_id)))
    add_contacts_list((str(my_id)))
    app.send_message("me", "Done..!")

# Bot reset
@app.on_message(Filters.me & Filters.text & Filters.incoming & Filters.command(["reset"]), group=9)
def bot_reset(client, message):
    app.send_message("me", "BOT Reseting...!")
    clear_contacts_list()
    clear_block_list()
    clear_allow_list()
    clear_end_chat_list()

    #with app:
    me = app.get_me()
    my_id = (me.id)

    contacts = app.get_contacts()
    new_contact_list = []
    for count in range(len(contacts)):
        new_contact_list.append(contacts[count]["id"])
    
    # create contact id txt file as "contact_list.txt"
    with open("contact_list.txt", "w") as f:
        for con in new_contact_list:
            f.write(str(con)+"\n")

    # adding contact id list to "allow_list.txt"
    with open("allow_list.txt", "w") as f:
        for con in new_contact_list:
            f.write(str(con)+"\n")
    
    msg_count_dict.clear()
    end_chat_msg_count_dict.clear()
    contact_list.clear()
    new_contact_list.clear()

    # Me adding to my contact and allow lists
    add_allow_list((str(my_id)))
    add_contacts_list((str(my_id)))
    app.send_message("me", "Done..!")

#----------------------------------------------------------------------------------------------------------------------
# HI
@app.on_message(Filters.text & Filters.outgoing & Filters.private & Filters.command(["hi"]), group=10)
def hi_private(client, message):
    app.delete_messages(message.chat.id, message.message_id)
    app.send_chat_action(message.chat.id, "typing")
    message.reply_text("`Hello,` {} {}".format(MENTION.format(message.chat.first_name, message.chat.id), Emoji.SMILING_FACE_WITH_HALO ))

@app.on_message(Filters.text & Filters.outgoing & Filters.group & Filters.command(["hi"]), group=11)
def hi_group(client, message):
    app.delete_messages(message.chat.id, message.message_id)
    app.send_chat_action(message.chat.id, "typing")
    message.reply_text("`Hello,` Everyone {}".format(Emoji.SMILING_FACE_WITH_HALO ))

# GM
@app.on_message(Filters.text & Filters.outgoing & Filters.private & Filters.command(["gm"]), group=12)
def gm_private(client, message):
    app.delete_messages(message.chat.id, message.message_id)
    app.send_chat_action(message.chat.id, "typing")
    message.reply_text("`Good morning...!` {}{} {}".format(Emoji.SMILING_FACE_WITH_SUNGLASSES, Emoji.RED_HEART, MENTION.format(message.chat.first_name, message.chat.id)))

@app.on_message(Filters.text & Filters.outgoing & Filters.group & Filters.command(["gm"]), group=13)
def gm_group(client, message):
    app.delete_messages(message.chat.id, message.message_id)
    app.send_chat_action(message.chat.id, "typing")
    message.reply_text("`Good morning...!` {}{} Everyone".format(Emoji.SMILING_FACE_WITH_SUNGLASSES, Emoji.RED_HEART))

# GN
@app.on_message(Filters.text & Filters.outgoing & Filters.private & Filters.command(["gn"]), group=14)
def gn_private(client, message):
    app.delete_messages(message.chat.id, message.message_id)
    app.send_chat_action(message.chat.id, "typing")
    message.reply_text("`Good night...!` {}{} {}".format(Emoji.SLEEPING_FACE, Emoji.RED_HEART, MENTION.format(message.chat.first_name, message.chat.id)))

@app.on_message(Filters.text & Filters.outgoing & Filters.group & Filters.command(["gn"]), group=15)
def gn_group(client, message):
    app.delete_messages(message.chat.id, message.message_id)
    app.send_chat_action(message.chat.id, "typing")
    message.reply_text("`Good night...!` {}{} Everyone".format(Emoji.SLEEPING_FACE, Emoji.RED_HEART))

# SORRY
@app.on_message(Filters.text & Filters.outgoing & Filters.private & Filters.command(["sorry"]), group=16)
def sorry_private(client, message):
    app.delete_messages(message.chat.id, message.message_id)
    app.send_chat_action(message.chat.id, "typing")
    message.reply_text("`Sorry for the delayed response` {}".format(Emoji.NEUTRAL_FACE))

@app.on_message(Filters.text & Filters.outgoing & Filters.group & Filters.command(["sorry"]), group=17)
def sorry_group(client, message):
    app.delete_messages(message.chat.id, message.message_id)
    app.send_chat_action(message.chat.id, "typing")
    message.reply_text("`Sorry for the delayed response` {}".format(Emoji.NEUTRAL_FACE))

app.run()