
def searchPartner(sid, rooms):
    for room in rooms:
        if sid in room:
            return room, True
    return None, False