from datetime import datetime


def sample_response(input):
    user_message = str(input).lower()

    if user_message in ("hello", "hi"):
        return "Hey there! How's it going?"

    elif user_message in ("who are you", "who are you?", "what is your name","what is your name?"):
        return "Hey, I'm SajiBot!! I'm your virtual friend created by Mr.Sreejith R! to have some fun conversatiions.." 
    
    elif user_message in ("time","time?","what is the time?","what is the time now?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)
    
    elif user_message in ("what do you like to eat","what do you like to eat?"):
        return "I don't like eating anything because I'm a bot obviously!!"
    
    elif user_message in ("how are you", "how are you?", "how are you doing", "how are you doing?"):
        return "I'm doing great, thanks for asking! Just here, chilling and ready to chat with you."
    
    else:
        return "I don't understand you!! Sorry!!"