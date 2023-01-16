def main():
    info = take_dates()
    print(new_history(info))

def new_history(dates):
    history = f"I am Zeus, and i have he a live, the name wich we will are give is {dates[0]} \n" \
              f"and his last name will be {dates[1]}. This mortal, his must will be protect his origin city {dates[2]}\n" \
              f"and as gift for this live, he must give me one {dates[3]} or never more he will can {dates[4]}. \n" \
              f"That's how it's written and that's how it's fulfilled"

    return history

def take_dates():
    dates = []

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    city = input("Enter your city of origin: ")
    fav_food = input("Enter your favorite food: ")
    fav_task = input(("Enter your favorite task: "))

    dates.append(first_name)
    dates.append(last_name)
    dates.append(city)
    dates.append(fav_food)
    dates.append(fav_task)

    return dates

if __name__ == '__main__':
    main()
