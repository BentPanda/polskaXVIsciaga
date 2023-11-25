import tkinter as tk
import sqlite3

def fetch_and_display_text():
    # Połączenie z bazą danych
    conn = sqlite3.connect('bazadanych.db')
    cursor = conn.cursor()

    # Wykonanie zapytania do bazy danych
    cursor.execute("SELECT tresc FROM tekst")
    text_data = cursor.fetchall()

    # Wyświetlenie pobranych danych
    display_text = '\n'.join([row[0] for row in text_data])
    text_area.config(state=tk.NORMAL)
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, display_text)
    text_area.config(state=tk.DISABLED)

    # Zamknięcie połączenia z bazą danych
    conn.close()

def clear_text():
    # Czyszczenie obszaru tekstowego
    text_area.config(state=tk.NORMAL)
    text_area.delete('1.0', tk.END)
    text_area.config(state=tk.DISABLED)

# Utworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Wyświetlacz Tekstu")

# Utworzenie przycisku do pobierania tekstu
fetch_button = tk.Button(root, text="Pobierz tekst", command=fetch_and_display_text)
fetch_button.pack(side=tk.LEFT)

# Utworzenie przycisku do czyszczenia tekstu
clear_button = tk.Button(root, text="Cofnij tekst", command=clear_text)
clear_button.pack(side=tk.RIGHT)

# Utworzenie obszaru tekstowego do wyświetlania danych
text_area = tk.Text(root, wrap="word", state=tk.DISABLED)
text_area.pack(expand=True, fill='both')

# Uruchomienie aplikacji
root.mainloop()
