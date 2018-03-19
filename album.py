def run():
    # Theme with function

    def make_album(singer_name, album_name, track_number=''):
        """This function will make the dictionary with your album"""

        # Album dictionary, empty in default
        album = {}

        # You can enter quantity of tracks in album if you want
        if track_number:
            album['track number'] = track_number

        # Here you enter singer name
        album['singer name'] = singer_name

        # Here you enter album name
        album['album name'] = album_name

        # The dictionary with entering data returns
        return album

    users_dict = {}
    while True:

        user_name = input("Please, enter your name: ")
        user_album = make_album(input("Enter singer or group name: "),
                                input("Enter album name: "),
                                input("If you want, enter track numbers"
                                      "\nIf not, just press 'Enter': "))
        users_dict[user_name] = user_album
        message = input("Print 'q' if you don't want to continue: ")
        # Exit from cycle
        if message == 'q':
            break
    print(users_dict)


if __name__ == "__main__":
    run()

