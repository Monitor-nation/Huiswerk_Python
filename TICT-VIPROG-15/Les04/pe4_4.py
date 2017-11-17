#Nieuw en oud ww mogen niet gelijk zijn en nieuw ww minimaal 6 karakters
def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6:
        return True
    return False
print(new_password('hhh', 'hhh'))