def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(f"Hello, my name is {name}.")
    return badges

def assign_rooms(names):
    room_assignments = []
    room = 1
    for name in names:
        room_assignments.append(f"Hello, {name}! You'll be assigned to room {room}!")
        room += 1
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    for badge in badges:
        print(badge)
    for room in room_assignments:
        print(room)

        
    
