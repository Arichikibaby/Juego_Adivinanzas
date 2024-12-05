import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina el Número")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Variables del juego
        self.random_number = 0
        self.attempts_left = 10

        # Widgets principales
        self.title_label = tk.Label(root, text="¡Adivina el Número!", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.instructions_label = tk.Label(root, text="Ingresa un número entre 1 y 100:", font=("Arial", 12))
        self.instructions_label.pack(pady=5)

        self.input_field = tk.Entry(root, font=("Arial", 12))
        self.input_field.pack(pady=5)

        self.guess_button = tk.Button(root, text="Adivinar", font=("Arial", 12), bg="lightblue", command=self.make_guess)
        self.guess_button.pack(pady=5)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.feedback_label.pack(pady=5)

        self.attempts_label = tk.Label(root, text=f"Intentos restantes: {self.attempts_left}", font=("Arial", 12))
        self.attempts_label.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reiniciar", font=("Arial", 12), bg="lightgreen", command=self.reset_game)
        self.reset_button.pack(pady=10)

        # Iniciar juego
        self.reset_game()

    def reset_game(self):
        """Reinicia el juego generando un nuevo número y reiniciando los intentos."""
        self.random_number = random.randint(1, 100)
        self.attempts_left = 10
        self.feedback_label.config(text="")
        self.attempts_label.config(text=f"Intentos restantes: {self.attempts_left}")
        self.input_field.delete(0, tk.END)
        self.guess_button.config(state=tk.NORMAL)
        print(f"(Debug) Número generado: {self.random_number}")  # Debug: Ver el número generado

    def make_guess(self):
        """Valida la entrada del usuario y proporciona retroalimentación."""
        user_input = self.input_field.get()

        # Validar que la entrada sea un número entre 1 y 100
        if not user_input.isdigit():
            self.feedback_label.config(text="Por favor, ingresa un número válido.")
            return

        user_guess = int(user_input)
        if user_guess < 1 or user_guess > 100:
            self.feedback_label.config(text="Número fuera de rango. Ingresa entre 1 y 100.")
            return

        # Reducir intentos
        self.attempts_left -= 1
        self.attempts_label.config(text=f"Intentos restantes: {self.attempts_left}")

        # Comparar el número ingresado con el número generado
        if user_guess == self.random_number:
            self.feedback_label.config(text="¡Correcto! Has adivinado el número.", fg="green")
            self.guess_button.config(state=tk.DISABLED)
        elif user_guess > self.random_number:
            self.feedback_label.config(text="Demasiado alto. Intenta con un número más bajo.", fg="red")
        else:
            self.feedback_label.config(text="Demasiado bajo. Intenta con un número más alto.", fg="red")

        # Verificar si se quedaron sin intentos
        if self.attempts_left == 0 and user_guess != self.random_number:
            self.feedback_label.config(text=f"Has perdido. El número era {self.random_number}.", fg="red")
            self.guess_button.config(state=tk.DISABLED)

        # Limpiar el campo de entrada
        self.input_field.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()
