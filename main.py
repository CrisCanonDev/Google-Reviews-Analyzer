def mainMenu():
    ans = True
    while ans:
        print("MENU SELECTION")
        print("[1] ENTER A PLACE NAME TO CHECK FOR REVIEWS.")
        print("[0] EXIT")

        ans = input("What would you like to do? ")
        if ans == "1":
            print("option 1")
            place_name = input("ENTER A PLACE NAME:  ")
            # place_name = "McDonald's Bugibba Square San Pawl il-Baħar"
            from googleAPI import googleAPIConn
            googleAPIConn(place_name)
            ans = False
            mainMenu()
        elif ans == "0":
            quit()
        elif ans != "":
            print("\n Not Valid Choice Try again")


if __name__ == "__main__":
    mainMenu()
