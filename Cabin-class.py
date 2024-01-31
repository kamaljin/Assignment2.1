def describe_cabin_class(cabin_class):
    if cabin_class == 'LUX':
        print("Upper-deck cabin with a balcony.")
    elif cabin_class == 'A':
        print("Above the car deck, equipped with a window.")
    elif cabin_class == 'B':
        print("Windowless cabin above the car deck.")
    elif cabin_class == 'C':
        print("Windowless cabin below the car deck.")
    else:
        print("Error: Invalid cabin class.")

if __name__ == "__main__":
    cabin_class = input("Enter the cabin class of the cruise ship: ")
    describe_cabin_class(cabin_class)
