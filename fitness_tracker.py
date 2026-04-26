import os
from datetime import datetime
user_workout = "user_workout.txt"
headers = ["date", "lift", "weight", "reps", "sets"]
exercises = ["bench press", "deadlift", "squat"]

session_count = 0
total_volume = 0
total_volume_by_lift = {}
max_by_lift = {}
dates = set()


while True:
    print("--------------------------------")
    print("CLI FITNESS TRACKER")
    print("--------------------------------\n")

    print("1. Add New Workout")
    print("2. View Previous Workouts")
    print("3. View Overall Summary")
    print("4. Reset Statistics")
    print("5. Exit Program\n")

    user_input = input("Enter Value (1-5): ")

    # ADDING A NEW WORKOUT
    if user_input.strip() == "1":
        with open(user_workout, "a") as file:
            if os.path.getsize(user_workout) == 0:
                file.write(",".join(headers) + "\n")

            while True:
                print("--------------------------------")
                print("ADDING NEW WORKOUT")
                print("--------------------------------")
                print("\nEnter new workout. Type 'done' to print summary\n")

                while True:
                    workout_date = input("Date (DD-MM-YYYY): ").strip()

                    if workout_date.lower() == "done":
                        break

                    else:
                        try:
                            datetime.strptime(workout_date, "%d-%m-%Y")
                            file.write(workout_date + ",")
                            break

                        except ValueError:
                            print("Invalid date, try again\n")

                if workout_date.lower() == "done":
                    print(f"\nCalculating summary...\n")
                    break

                while True:
                    workout_lift = str(
                        input("Lift (Bench Press, Deadlift, Squat): ")).lower().strip()

                    if workout_lift in exercises:
                        file.write(workout_lift + ",")
                        break

                    else:
                        print("Invalid option, try again\n")

                while True:
                    try:
                        workout_weight = int(input("Weight (kg): "))

                        if (workout_weight > 0) and (workout_weight <= 400):
                            file.write(str(workout_weight) + ",")
                            break

                        else:
                            print("Invalid value, try again (1-400)\n")

                    except ValueError:
                        print("Please enter a valid value\n")

                while True:
                    try:
                        workout_reps = int(input("Reps: "))

                        if (workout_reps > 0) and (workout_reps <= 100):
                            file.write(str(workout_reps) + ",")
                            break

                        else:
                            print("Invalid value, try again (1-100)\n")

                    except ValueError:
                        print("Please enter a valid value\n")

                while True:
                    try:
                        workout_sets = int(input("Sets: "))

                        if (workout_sets > 0) and (workout_sets <= 10):
                            file.write(str(workout_sets) + "\n")
                            break

                        else:
                            print("Invalid value, try again (1-10)\n")

                    except ValueError:
                        print("Please enter a valid value\n")

                print("\nWorkout saved\n")

                total_volume = total_volume + \
                    ((workout_weight * workout_reps) * workout_sets)
                total_volume_by_lift[workout_lift] = total_volume_by_lift.get(
                    workout_lift, 0) + ((workout_weight * workout_reps) * workout_sets)

                if (workout_lift not in max_by_lift) or (workout_weight > max_by_lift[workout_lift]):
                    max_by_lift[workout_lift] = workout_weight

                dates.add(workout_date)
                session_count = session_count + 1

        print("--------------------------------")
        print("WORKOUT SUMMARY")
        print("--------------------------------")

        print(f"\nSessions logged: {session_count}")
        print(f"Days trained: {len(dates)}")

        print(f"\n\nVolume per lifts:")

        for lift, volume in total_volume_by_lift.items():
            print(f"    - {lift.title()}: {volume}kg")

        print(f"\nTotal volume: {total_volume}kg")

        print(f"\n\nMax lifts:")

        for lift, max_weight in max_by_lift.items():
            print(f"    - {lift.title()}: {max_weight}kg")

        print("\n--------------------------------")
        print("Workout has been saved")
        print("--------------------------------\n")
        break

    # VIEWING PREVIOUS WORKOUTS
    elif user_input.strip() == "2":
        print("--------------------------------")
        print("PREVIOUS WORKOUTS")
        print("--------------------------------")

        if os.path.getsize(user_workout) < 2:
            print("\nNo workout recorded\n")

        else:
            with open(user_workout, 'r') as file:
                next(file)

                for line in file:
                    date, lift, weight, reps, sets = line.strip().split(",")

                    print(f"\nDate: {date}")
                    print(f"Lift: {lift.title()}")
                    print(f"Weight: {weight}kg")
                    print(f"Reps: {reps}")
                    print(f"Sets: {sets}")
                print("")

    # VIEWING SUMMARY
    elif user_input.strip() == "3":
        print("--------------------------------")
        print("WORKOUT SUMMARY")
        print("--------------------------------")

        if os.path.getsize(user_workout) < 2:
            print("\nNo workouts recorded.\n")

        else:
            total_volume = 0
            session_count = 0
            dates = set()
            total_volume_by_lift = {}
            max_by_lift = {}

            with open(user_workout, "r") as file:
                next(file)  # skip headers

                for line in file:
                    date, lift, weight, reps, sets = line.strip().split(",")

                    weight = int(weight)
                    reps = int(reps)
                    sets = int(sets)

                    volume = weight * reps * sets

                    session_count += 1
                    total_volume += volume
                    dates.add(date)

                    total_volume_by_lift[lift] = total_volume_by_lift.get(
                        lift, 0) + volume

                    if lift not in max_by_lift or weight > max_by_lift[lift]:
                        max_by_lift[lift] = weight

            print(f"\nSessions logged: {session_count}")
            print(f"Days trained: {len(dates)}")
            print(f"Total volume: {total_volume}kg")

            print("\nVolume per lift:")
            for lift, volume in total_volume_by_lift.items():
                print(f"    - {lift.title()}: {volume}kg")

            print("\nMax lifts:")
            for lift, max_weight in max_by_lift.items():
                print(f"    - {lift.title()}: {max_weight}kg")

            print("")

    # RESETTING STATISTICS
    elif user_input.strip() == "4":
        print("--------------------------------")
        print("RESETTING STATISTICS")
        print("--------------------------------")

        user_input = input("\nAre you sure (yes/no): ").lower()

        if user_input == "yes":
            open(user_workout, "w").close()
            print("\nRESET SUCCESSFUL\n")

        else:
            print("\nRESET CANCELLED\n")

    # EXITING PROGRAM
    elif user_input.strip() == "5":
        print("--------------------------------")
        print("EXITING PROGRAM")
        print("--------------------------------")

        break

    else:
        print("Invalid response, try again\n")
