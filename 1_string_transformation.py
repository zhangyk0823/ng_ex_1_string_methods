booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

p = booking.strip().split(" | ")
event_code, username, room, time, email, vip = p[0], p[1], p[2], p[3], p[4], p[5]

domain = email[email.find("@") + 1:].lower()

print(f"Event code: {event_code}")
print(f"Name: {username.title()}")
print(f"Room: {room.upper()}")
print(f"Time: {time}")
print(f"Email domain: {domain}")
print(f"VIP tag count: {vip.count('VIP')}")
print(f"Valid event code: {event_code.startswith('EVT-')}")
print(f"Valid username: {username.replace('_', '').isalpha()}")
print(f"Valid room: {room.startswith('Room-')}")
print(f"Valid time: {':' in time}")
print(f"Valid email: {'@' in email}")
