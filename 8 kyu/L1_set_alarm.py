def set_alarm(employed, vacation):
    if employed == True:
        if vacation == False:
            return True
        else:
            return False
    else:
        return False