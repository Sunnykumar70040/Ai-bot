import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai

# Replace this with your actual API key
API_KEY = 'AIzaSyDD0Vs36-8aeafO0tr2nGx9yO6iu6l74-4'

# Configure Gemini AI
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Prompt context
BASE_PROMPT = (
    "You are an AI Debt Management Coach. Your job is to help users understand, plan, "
    "and optimize debt repayment strategies. Be friendly, educational, and interactive. "
    "Ask them questions to understand their financial status (income, expenses, debt types, etc.), "
    "and then offer a suitable repayment strategy like avalanche, snowball, or custom plan."
)

class DebtCoachApp:
    def _init_(self, root):
        self.root = root
        self.root.title("AI Debt Management Coach")
        self.root.configure(bg="#f0f4f7")

        # Header Label
        self.header = tk.Label(root, text="💬 AI Debt Management Coach", font=("Helvetica", 20, "bold"), bg="#f0f4f7", fg="#2c3e50")
        self.header.pack(pady=(10, 0))

        # Chat Display
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=25, font=("Segoe UI", 11), bg="#ffffff", fg="#000000", bd=2, relief=tk.RIDGE)
        self.chat_display.pack(padx=20, pady=10)
        self.chat_display.config(state='disabled')

        # Input Frame
        input_frame = tk.Frame(root, bg="#f0f4f7")
        input_frame.pack(pady=5)

        self.entry = tk.Entry(input_frame, font=("Segoe UI", 12), width=55, bd=2, relief=tk.GROOVE)
        self.entry.grid(row=0, column=0, padx=10, pady=10)

        self.send_button = tk.Button(input_frame, text="Send", font=("Segoe UI", 12, "bold"), bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white", command=self.send_message)
        self.send_button.grid(row=0, column=1, padx=5)

        # Initialize conversation
        self.convo = model.start_chat(history=[{"role": "user", "parts": [BASE_PROMPT]}])
        self.show_message("AI Coach", "Hello! I'm your AI Debt Coach. Let's build your debt repayment plan together.\nPlease tell me a bit about your debt situation!")

    def show_message(self, sender, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

    def send_message(self):
        user_input = self.entry.get().strip()
        if not user_input:
            return

        self.show_message("You", user_input)
        self.entry.delete(0, tk.END)

        response = self.convo.send_message(user_input)
        self.show_message("AI Coach", response.text)

if _name_ == "_main_":
    root = tk.Tk()
    app = DebtCoachApp(root)
    root.mainloop()