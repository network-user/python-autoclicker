import time

from pynput.mouse import Button, Controller
import threading
import keyboard

clicking = False
mouse = Controller()

def auto_clicker():
    global clicking
    try:
        while clicking:
            mouse.click(Button.left)
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass

def toggle_clicker():
    global clicking
    clicking = not clicking
    if clicking:
        print("Автокликер запущен. Нажмите F10 для остановки.")
        auto_clicker_thread = threading.Thread(target=auto_clicker)
        auto_clicker_thread.start()
    else:
        print("Автокликер остановлен.")

def main():
    keyboard.add_hotkey('f9', lambda: toggle_clicker())  # Биндим F9 на запуск/остановку автокликера
    keyboard.add_hotkey('f10', lambda: toggle_clicker())  # Биндим F10 на остановку автокликера
    print("Нажмите F9 для запуска автокликера.")

    try:
        keyboard.wait('esc')  # Ждем нажатия Esc для выхода
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
