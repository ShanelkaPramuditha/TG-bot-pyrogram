def search_contacts(user_id):
    with open("contact_list.txt", "r") as f:
        content = f.read()
        if user_id in content:
            return True
        else:
            return False

def add_contacts_list(user_id):                     # temp solution
    with open("contact_list.txt", "a") as f:
        f.write(user_id+"\n")

def remove_contacts_list(user_id):                     # temp solution
    with open("contact_list.txt", "r") as f:
        lines = f.readlines()
    with open("contact_list.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != user_id:
                f.write(line)

def clear_contacts_list():
    with open("contact_list.txt", "w") as f:
        f.close()




def add_allow_list(user_id):
    with open("allow_list.txt", "a") as f:
        f.write(user_id+"\n")

def search_allow_list(user_id):
    with open("allow_list.txt", "r") as f:
        content = f.read()
        if user_id in content:
            return True
        else:
            return False

def remove_allow_list(user_id):
    with open("allow_list.txt", "r") as f:
        lines = f.readlines()
    with open("allow_list.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != user_id:
                f.write(line)

def clear_allow_list():
    with open("allow_list.txt", "w") as f:
        f.close()



def add_block_list(user_id):
    with open("block_list.txt", "a") as f:
        f.write(user_id+"\n")

def search_block_list(user_id):
    with open("block_list.txt", "r") as f:
        content = f.read()
        if user_id in content:
            return True
        else:
            return False

def remove_block_list(user_id):
    with open("block_list.txt", "r") as f:
        lines = f.readlines()
    with open("block_list.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != user_id:
                f.write(line)

def clear_block_list():
    with open("block_list.txt", "w") as f:
        f.close()




def add_end_chat_list(user_id):
    with open("end_chat.txt", "a") as f:
        f.write(user_id+"\n")

def search_end_chat_list(user_id):
    with open("end_chat.txt", "r") as f:
        content = f.read()
        if user_id in content:
            return True
        else:
            return False

def remove_end_chat_list(user_id):
    with open("end_chat.txt", "r") as f:
        lines = f.readlines()
    with open("end_chat.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != user_id:
                f.write(line)

def clear_end_chat_list():
    with open("end_chat.txt", "w") as f:
        f.close()