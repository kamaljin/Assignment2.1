def main():
    # Ask for biological gender
    gender = input("Enter your biological gender (male/female): ").strip().lower()

    # Ask for hb value
    hb = float(input("Enter your hb value (g/l): "))

    # Define normal ranges based on gender
    if gender == "male":
        low_range = 134
        high_range = 167
    elif gender == "female":
        low_range = 117
        high_range = 155
    else:
        print("Invalid gender input. Please enter 'male' or 'female'.")
        return

    # Check if hb value is low, normal, or high
    if hb < low_range:
        print("Your hb level is low.")
    elif low_range <= hb <= high_range:
        print("Your hb level is normal.")
    else:
        print("Your hb level is high.")

if __name__ == "__main__":
    main()
