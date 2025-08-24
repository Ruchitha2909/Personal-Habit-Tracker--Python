🎯 Python Habit Tracker

A command-line application built with Python to create, manage, and track personal habits. This project demonstrates core Object-Oriented Programming (OOP) principles including Inheritance, Encapsulation, and Abstraction.

📖 Overview

This Habit Tracker allows users to define different types of habits, update their progress, and view a summary. It's designed to be a simple yet powerful demonstration of software design patterns in a practical application.

✨ Features

-   **Habit Categorization:** Create two specific types of habits: `HealthHabit` and `LearningHabit`.
-   **Progress Tracking:** Update and monitor the progress percentage for each habit.
-   **Polymorphic Display:** Each habit type displays its information in a unique way using method overriding.
-   **Interactive CLI Menu:** Easy-to-use text-based menu system for navigation.
-   **Data Encapsulation:** Habit names and progress are protected as private attributes, accessed via getter methods.

🧩 Object-Oriented Design

The project architecture is built on solid OOP principles:

-   **Abstraction:** The abstract base class `Habit` defines the required structure (`track` method) for all habits.
-   **Inheritance:** `PersonalHabit` inherits from `Habit`, and `HealthHabit`/`LearningHabit` inherit from `PersonalHabit`, creating a clear hierarchy.
-   **Encapsulation:** The `__name` and `__progress` attributes are private and can only be modified through public methods like `update_progress()`.
-   **Polymorphism:** The `track()` method is overridden in each subclass to display habit-specific details (e.g., duration for health habits, topic for learning habits).

🛠️ Technologies Used

-   **Python 3**
-   **OOP Concepts:**
    -   Abstract Base Classes (`abc` module)
    -   Inheritance
    -   Encapsulation (Private attributes with getters)
    -   Polymorphism (Method overriding)

