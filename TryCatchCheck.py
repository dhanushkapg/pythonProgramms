def checkUserName(userName,lent):
    assert type(userName)==str, "user Name must be a String"
    if lent<=2:
        raise ValueError("minimum length should be 5 ")
    if len(userName)<lent:
        return False
    else:
        return True