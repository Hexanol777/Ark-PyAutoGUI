import pyautogui
import time
import random
import customtkinter
import threading

customtkinter.set_appearance_mode("system")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Application(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Get Amiya'd")
        self.iconbitmap('Images/Amiya.ico') #hehe
        self.geometry('300x250')
        self.attributes('-alpha', 0.7) # set the transparency level to 70%
        self.geometry("+0+0")  # move the window to the top left corner
        self.create_widgets()

    def create_widgets(self):
        self.progress_log = customtkinter.CTkTextbox(self)
        self.progress_log.pack(side="top", fill="both", expand=True)
        self.progress_log.configure(state=customtkinter.DISABLED)

        self.start_button = customtkinter.CTkButton(self, text='Start',
                                                    text_color='white',
                                                    border_color='white',
                                                    width=5, command=self.start_script)
        self.start_button.pack(side="right", padx=50, pady=10, fill=customtkinter.BOTH, expand=True)

        self.stop_button = customtkinter.CTkButton(self, text='Stop',
                                                   text_color='white',
                                                   border_color='white',
                                                   hover_color='red',
                                                   width=5, command=self.stop_script)
        self.stop_button.pack(side="left", padx=50, pady=10, fill=customtkinter.BOTH, expand=True)

    def start_script(self):
        pyautogui.PAUSE = 1.5
        center = pyautogui.size()
        pyautogui.moveTo(center[0] / 2, center[1] / 2, duration=0)
        time.sleep(1)
        self.counter = 1

        def randomizer():
            return random.choice(range(-40, 40)), random.choice(range(-40, 40))

        def main():
            x_off, y_off = randomizer()

            while True:
                start_POS = pyautogui.locateOnScreen(r"Images/startBTN.png", confidence=0.85)
                start_btn = pyautogui.center(start_POS)
                pyautogui.click(x=start_btn[0] + x_off, y=start_btn[1] + y_off, clicks=1, button='left')

                while pyautogui.locateOnScreen(r"Images/MissionStartBTN.png", confidence=0.85) is None:
                    time.sleep(0.5)
                mission_start_POS = pyautogui.locateOnScreen(r"Images/MissionStartBTN.png", confidence=0.85)
                mission_start_btn = pyautogui.center(mission_start_POS)
                pyautogui.click(x=mission_start_btn[0] + x_off, y=mission_start_btn[1] + y_off, clicks=1, button='left')

                self.progress_log.configure(state=customtkinter.NORMAL)
                self.progress_log.delete('1.0', customtkinter.END)
                self.progress_log.insert(customtkinter.END, 'Entering The Stage...')
                self.progress_log.configure(state=customtkinter.DISABLED)

                while pyautogui.locateOnScreen(r"Images/Trust.png", confidence=0.85) is None:
                    time.sleep(5)
                trust = pyautogui.locateOnScreen(r"Images/Trust.png", confidence=0.85)
                trust_btn = pyautogui.center(trust)
                time.sleep(1)
                pyautogui.click(x=trust_btn[0] + x_off, y=trust_btn[1] + y_off, clicks=1, button='left')

                self.progress_log.configure(state=customtkinter.NORMAL)
                self.progress_log.delete('1.0', customtkinter.END)
                self.progress_log.insert(customtkinter.END, f'run no.{self.counter} complete.\ncontinuing the process.')
                self.progress_log.configure(state=customtkinter.DISABLED)

                self.counter += 1

                if pyautogui.locateOnScreen(r"Images/SanityRefill.png", confidence=0.85) is not None:
                    self.progress_log.configure(state=customtkinter.NORMAL)
                    self.progress_log.insert(customtkinter.END,
                                             "Not enough sanity to repeat the stage, closing the program.")
                    self.progress_log.configure(state=customtkinter.DISABLED)

                    self.stop_script()

                else:
                    time.sleep(10)

        # Create a new thread and start running the `main` function
        threading.Thread(target=main, daemon=True).start()

    def stop_script(self):
        self.destroy()

app = Application()
app.mainloop()
