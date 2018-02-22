def run():
    guests = ['dima', 'sergey', 'valik', 'zhenya', 'vitalya', 'valera', 'nastya', 'olya']
    for guest in guests:
        print("Dear " + guest.title() + "! I invite you to my birthday!")
    guests.reverse()
    qt_guests = len(guests)
    while qt_guests > 2:
        popped_guest = guests.pop()
        print("Sorry, dear " + popped_guest.title() + ", but i have not opportunity "
                                                      "to invite you on my birthday.")
        qt_guests -= 1
    for guest in guests:
        print("Dear " + guest.title() + "! My invitation is still valid! Waiting for you!")


if __name__ == "__main__":
    run()