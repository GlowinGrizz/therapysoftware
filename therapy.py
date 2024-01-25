import tkinter as tk
from tkinter import ttk, scrolledtext
import pygame

class TherapistGameUI:
    def __init__(self, master):
        self.master = master
        master.title("Digital Therapist Game")

        # Initialize pygame mixer
        pygame.mixer.init()

        # Load background music
        pygame.mixer.music.load("therapymusic.mp3")  # Replace with the correct path if needed

        # Get screen width and height
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Calculate window width and height
        window_width = int(screen_width * 0.6)
        window_height = int(screen_height * 0.4)

        # Calculate window position
        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)

        # Set window size and position
        master.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12))
        self.style.configure('TLabel', font=('Arial', 12))
        self.style.configure('TEntry', font=('Arial', 12))
        self.style.configure('TText', font=('Arial', 12))

        self.developer_label = ttk.Label(master, text="Developed by lasagnapapa", style='TLabel')
        self.developer_label.pack(pady=10)

        self.start_button = ttk.Button(master, text="Start Session", command=self.show_intermediate_screen, style='TButton')
        self.start_button.pack(pady=20)

        self.quit_button = ttk.Button(master, text="Exit", command=self.exit_application, style='TButton')
        self.quit_button.pack(pady=10)

    def show_intermediate_screen(self):
        self.master.withdraw()  # Hide the main window

        intermediate_screen = tk.Toplevel(self.master)
        intermediate_screen.title("Intermediate Screen")

        # Get screen width and height
        screen_width = intermediate_screen.winfo_screenwidth()
        screen_height = intermediate_screen.winfo_screenheight()

        # Calculate window width and height
        window_width = int(screen_width * 0.6)
        window_height = int(screen_height * 0.3)

        # Calculate window position
        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)

        # Set window size and position
        intermediate_screen.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        message_label = ttk.Label(intermediate_screen, text="For Steve, nobody deserves to go through a day like that", font=("Arial", 14, "bold"))
        message_label.pack(pady=20)

        ok_button = ttk.Button(intermediate_screen, text="OK", command=lambda: self.start_session(intermediate_screen), style='TButton')
        ok_button.pack(pady=10)

    def start_session(self, intermediate_screen):
        intermediate_screen.destroy()  # Close the intermediate screen

        # Start playing background music
        pygame.mixer.music.play(-1)  # -1 means loop indefinitely

        session_window = tk.Toplevel(self.master)
        session_window.title("Therapist Session")

        # Get screen width and height
        screen_width = session_window.winfo_screenwidth()
        screen_height = session_window.winfo_screenheight()

        # Calculate window width and height
        window_width = int(screen_width * 0.6)
        window_height = int(screen_height * 0.5)

        # Calculate window position
        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)

        # Set window size and position
        session_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.session_label = ttk.Label(session_window, text="Digital Therapist: How can I help you today?", font=("Arial", 16, "bold"))
        self.session_label.pack(pady=10)

        self.user_input = ttk.Entry(session_window, width=40, font=('Arial', 12))
        self.user_input.pack(pady=5)

        self.joke_output = scrolledtext.ScrolledText(session_window, wrap=tk.WORD, width=40, height=5, state='disabled', font=('Arial', 12))
        self.joke_output.pack(pady=10)

        self.generate_button = ttk.Button(session_window, text="Tell the therapist", command=self.generate_joke, style='TButton')
        self.generate_button.pack(pady=10)

        self.exit_session_button = ttk.Button(session_window, text="Exit Session", command=lambda: self.exit_session(session_window), style='TButton')
        self.exit_session_button.pack(pady=10)

        # Stop background music when the session window is closed
        session_window.protocol("WM_DELETE_WINDOW", self.stop_music)

    def generate_joke(self):
        user_sentence = self.user_input.get()
        joke = generate_yo_mama_response(user_sentence)
        self.joke_output.configure(state='normal')
        self.joke_output.delete('1.0', tk.END)
        self.joke_output.insert(tk.END, joke)
        self.joke_output.configure(state='disabled')

    def exit_session(self, session_window):
        # Stop background music
        self.stop_music()
        # Destroy the session window
        session_window.destroy()
        # Show the main window again
        self.master.deiconify()

    def stop_music(self):
        pygame.mixer.music.stop()

    def exit_application(self):
        self.stop_music()
        self.master.destroy()

def generate_yo_mama_response(input_text):
    replacements = {
        'I had a really bad day today': 'Yo mama had a really bad day today',
        'I love chocolate': 'Yo mama loves chocolate too',
        'I don\'t know what to do': 'Yo mama always knows what to do',
        'I feel so tired': 'Yo mama is never tired',
        'I can\'t sleep': 'Yo mama never has trouble sleeping',
        'I got a promotion at work': 'Yo mama is proud of your achievements',
        'I lost my keys': 'Yo mama never loses anything',
        'I can\'t find my phone': 'Yo mama always knows where your phone is',
        'I miss my friends': 'Yo mama misses her friends too',
        'I want to travel': 'Yo mama loves to travel',
        'I hate Mondays': 'Yo mama doesn\'t mind Mondays',
        'I need a break': 'Yo mama is always ready for a break',
        'I have a headache': 'Yo mama never gets headaches',
        'I can\'t focus': 'Yo mama always stays focused',
        'I feel so lazy': 'Yo mama is never lazy',
        'I don\'t understand': 'Yo mama understands everything',
        'I wish I could fly': 'Yo mama can fly in her dreams',
        'I need a hug': 'Yo mama gives the best hugs',
        'I want to be successful': 'Yo mama believes in your success',
        'I feel lonely': 'Yo mama is always there for you',
        'I want to be happy': 'Yo mama wants you to be happy',
        'I\'m stressed out': 'Yo mama stays stress-free',
        'I broke my phone': 'Yo mama\'s phone is unbreakable',
        'I need advice': 'Yo mama gives the best advice',
        'I have a secret': 'Yo mama can keep a secret',
        'I feel lost': 'Yo mama always knows the way',
        'I\'m going on a diet': 'Yo mama supports your healthy choices',
        'I have a big project': 'Yo mama is great at managing projects',
        'I can\'t find my glasses': 'Yo mama never loses sight of things',
        'I want to learn a new language': 'Yo mama speaks all languages',
        'I\'m feeling adventurous': 'Yo mama is up for any adventure',
        'I\'m feeling determined': 'Yo mama never gives up',
        'I got a new pet': 'Yo mama loves animals',
        'I\'m going to the gym': 'Yo mama is always fit',
        'I don\'t have time': 'Yo mama can manage her time well',
        'I\'m learning to cook': 'Yo mama is a master chef',
        'I\'m feeling creative': 'Yo mama is the queen of creativity',
        'I\'m feeling lucky': 'Yo mama brings good luck',
        'I want to make a difference': 'Yo mama believes in making a difference',
        'I\'m feeling inspired': 'Yo mama is a constant source of inspiration',
        'I\'m feeling generous': 'Yo mama is always generous',
        'I\'m feeling nostalgic': 'Yo mama has timeless memories',
        'I\'m feeling curious': 'Yo mama has all the answers',
        'I\'m feeling grateful': 'Yo mama is grateful for you',
        'I\'m feeling optimistic': 'Yo mama sees the bright side',
        'I\'m feeling peaceful': 'Yo mama brings peace to your life',
        'I\'m feeling empowered': 'Yo mama empowers those around her',
        'I\'m feeling confident': 'Yo mama believes in your potential',
        'I need motivation': 'Yo mama is your biggest motivator',
        'I want to be a better person': 'Yo mama believes in your goodness',
        'I had a great workout': 'Yo mama is your fitness inspiration',
        'I want to be more organized': 'Yo mama is the queen of organization',
        'I need motivation': 'Yo mama is your biggest motivator',
        'I want to be a better person': 'Yo mama believes in your goodness',
        'I had a great workout': 'Yo mama is your fitness inspiration',
        'I need motivation': 'Yo mama is your biggest motivator',
        'I want to be a better person': 'Yo mama believes in your goodness',
        'I had a great workout': 'Yo mama is your fitness inspiration',
        'I want to be more organized': 'Yo mama is the queen of organization',
        'I feel so clumsy': 'Yo mama is always graceful',
        'I cant find my wallet': 'Yo mama always knows where your wallet is',
        'Im feeling ambitious': 'Yo mama is the epitome of ambition',
        'I need a vacation': 'Yo mama is your dream vacation planner',
        'Im feeling overwhelmed': 'Yo mama handles everything with ease',
        'Im feeling proud': 'Yo mama is proud of your achievements',
        'Im feeling curious': 'Yo mama knows all the answers',
        'Im feeling adventurous': 'Yo mama loves adventure',
        'I want to make new friends': 'Yo mama is the friendliest person',
        'Im feeling creative': 'Yo mama is a creative genius',
        'I feel so small': 'Yo mama is larger than life',
        'I want to learn a musical instrument': 'Yo mama is a musical prodigy',
        'I need a coffee': 'Yo mama brews the best coffee',
        'Im feeling patriotic': 'Yo mama loves her country',
        'I want to adopt a pet': 'Yo mama has a soft spot for animals',
        'Im feeling generous': 'Yo mama is always generous',
        'I want to learn a new skill': 'Yo mama is a skilled teacher',
        'Im feeling blessed': 'Yo mama feels blessed to have you',
        'I want to learn to dance': 'Yo mama has the best dance moves',
        'Im feeling independent': 'Yo mama values independence',
        'I want to quit my job': 'Yo mama supports your decisions',
        'Im feeling lucky': 'Yo mama brings good luck',
        'I want to start a business': 'Yo mama is a business mogul',
        'Im feeling mischievous': 'Yo mama knows how to have fun',
        'I want to write a book': 'Yo mama is a literary genius',
        'Im feeling nostalgic': 'Yo mama has timeless memories',
        'I want to be more patient': 'Yo mama is the epitome of patience',
        'Im feeling rebellious': 'Yo mama knows when to break the rules',
        'I want to learn photography': 'Yo mama captures every moment',
        'Im feeling philosophical': 'Yo mama has profound wisdom',
        'I want to learn to paint': 'Yo mama is a master artist',
        'Im feeling spontaneous': 'Yo mama loves spontaneous adventures',
        'I want to be more positive': 'Yo mama radiates positivity',
        'Im feeling sleepy': 'Yo mama never gets tired',
        'I want to learn to code': 'Yo mama is a coding expert',
        'Im feeling overwhelmed': 'Yo mama handles everything with ease',
        'I want to be more social': 'Yo mama is the life of the party',
        'Im feeling rebellious': 'Yo mama knows when to break the rules',
        'I want to learn to meditate': 'Yo mama is a meditation guru',
        'Im feeling philosophical': 'Yo mama has profound wisdom',
        'I want to learn to cook': 'Yo mama is a master chef',
        'Im feeling inspired': 'Yo mama is an endless source of inspiration',
        'I want to learn to garden': 'Yo mama has a green thumb',
        'Im feeling nostalgic': 'Yo mama has timeless memories',
        'I want to learn a new language': 'Yo mama speaks all languages',
        'Im feeling adventurous': 'Yo mama is up for any adventure',
        'I want to be more confident': 'Yo mama believes in your confidence',
        'Im feeling lucky': 'Yo mama brings good luck',
        'I want to start a YouTube channel': 'Yo mama is a YouTube sensation',
        'Im feeling mischievous': 'Yo mama knows how to have fun',
        'I want to learn to play chess': 'Yo mama is a chess grandmaster',
        'Im feeling rebellious': 'Yo mama knows when to break the rules',
        'I want to learn to play the guitar': 'Yo mama shreds on the guitar',
        'Im feeling philosophical': 'Yo mama has profound wisdom',
        'I want to learn to dance': 'Yo mama has the best dance moves',
        'Im feeling sleepy': 'Yo mama never gets tired',
        'I want to learn to draw': 'Yo mama is an artistic prodigy',
        'Im feeling overwhelmed': 'Yo mama handles everything with ease',
        'I want to be more social': 'Yo mama is the life of the party',
        'Im feeling rebellious': 'Yo mama knows when to break the rules',
        'I want to learn to meditate': 'Yo mama is a meditation guru',
        'Im feeling philosophical': 'Yo mama has profound wisdom',
        'I want to learn to cook': 'Yo mama is a master chef',
        'Im feeling inspired': 'Yo mama is an endless source of inspiration',
        'I want to learn to garden': 'Yo mama has a green thumb',
        'Im feeling nostalgic': 'Yo mama has timeless memories',
        'I want to learn a new language': 'Yo mama speaks all languages',
        'Im feeling adventurous': 'Yo mama is up for any adventure',
        'I want to be more confident': 'Yo mama believes in your confidence',
        'Im feeling lucky': 'Yo mama brings good luck',
        'I want to start a YouTube channel': 'Yo mama is a YouTube sensation',
        'Im feeling mischievous': 'Yo mama knows how to have fun',
        'I want to learn to play chess': 'Yo mama is a chess grandmaster',
        'Im feeling rebellious': 'Yo mama knows when to break the rules',
        'I want to learn to play the guitar': 'Yo mama shreds on the guitar',
        'Im feeling philosophical': 'Yo mama has profound wisdom',
        'I want to learn to dance': 'Yo mama has the best dance moves',
        'Im feeling sleepy': 'Yo mama never gets tired',
        'I want to learn to draw': 'Yo mama is an artistic prodigy',
        'Im feeling overwhelmed': 'Yo mama handles everything with ease',
        'I want to be more social': 'Yo mama is the life of the party',
        'Im feeling rebellious': 'Yo mama knows when to break the rules',
        'I want to learn to meditate': 'Yo mama is a meditation guru',
        'Im feeling philosophical': 'Yo mama has profound wisdom',
        'I want to learn to cook': 'Yo mama is a master chef',
        'Im feeling inspired': 'Yo mama is an endless source of inspiration',
        'I want to learn to garden': 'Yo mama has a green thumb',
        'Im feeling nostalgic': 'Yo mama has timeless memories',
        'I want to learn a new language': 'Yo mama speaks all languages',
        'Im feeling adventurous': 'Yo mama is up for any adventure',
        'I want to be more confident': 'Yo mama believes in your confidence',
        'Im feeling lucky': 'Yo mama brings good luck',
        'I want to start a YouTube channel': 'Yo mama is a YouTube sensation',
        'Im feeling mischievous': 'Yo mama knows how to have fun',
        'I want to learn to play chess': 'Yo mama is a chess grandmaster',
        'Im feeling rebellious': 'Yo mama knows when to break the rules',
        'I want to learn to play the guitar': 'Yo mama shreds on the guitar',
        'Im feeling philosophical': 'Yo mama has profound wisdom',
        'I want to learn to dance': 'Yo mama has the best dance moves',
        'I feel suicidal': 'Yo mama aint raise no bitch',
        'I feel so clumsy': 'Yo mama is always graceful'
	'Im feeling sexy': 'Yo mama fine as fuck so maybe you are too'
	'I hate my life': 'Yo mama give you a L Spawn point too?'

    }

    for word, replacement in replacements.items():
        input_text = input_text.replace(word, replacement)

    return f"{input_text}? Yo mama!"

if __name__ == "__main__":
    root = tk.Tk()
    app = TherapistGameUI(root)
    root.mainloop()
