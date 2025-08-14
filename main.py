from abc import ABC, abstractmethod

class Habit(ABC):
    @abstractmethod
    def track(self):
        pass

class PersonalHabit(Habit):
    def __init__(self, name):
        self.__name = name  # Encapsulated attribute
        self.__progress = 0

    def get_name(self):
        return self.__name

    def get_progress(self):
        return self.__progress

    def update_progress(self, value):
        self.__progress += value

    def track(self):
        print(f"Tracking habit: {self.__name}")

class HealthHabit(PersonalHabit):
    def __init__(self, name, duration):
        super().__init__(name)
        self.duration = duration

    def track(self):
        print(f"Health Habit: {self.get_name()}, Duration: {self.duration} mins, Progress: {self.get_progress()}%")

class LearningHabit(PersonalHabit):
    def __init__(self, name, topic):
        super().__init__(name)
        self.topic = topic

    def track(self):
        print(f"Learning Habit: {self.get_name()}, Topic: {self.topic}, Progress: {self.get_progress()}%")

def menu():
    habits = []
    while True:
        print("\n--- Habit Tracker Menu ---")
        print("1. Add Health Habit")
        print("2. Add Learning Habit")
        print("3. Update Progress")
        print("4. View All Habits")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter health habit name: ")
            duration = int(input("Enter duration in minutes: "))
            habits.append(HealthHabit(name, duration))
            print("Health habit added!")

        elif choice == '2':
            name = input("Enter learning habit name: ")
            topic = input("Enter topic: ")
            habits.append(LearningHabit(name, topic))
            print("Learning habit added!")

        elif choice == '3':
            if not habits:
                print("No habits found!")
            else:
                for i, habit in enumerate(habits):
                    print(f"{i+1}. {habit.get_name()}")
                index = int(input("Select habit number: ")) - 1
                value = int(input("Enter progress to add (%): "))
                habits[index].update_progress(value)
                print("Progress updated!")

        elif choice == '4':
            if not habits:
                print("No habits found!")
            else:
                for habit in habits:
                    habit.track()

        elif choice == '5':
            print("Exiting Habit Tracker...")
            break
        else:
            print("Invalid choice, please try again.")
menu()
