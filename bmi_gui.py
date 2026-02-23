import tkinter as tk
from tkinter import messagebox, ttk 
import sqlite3
from PIL import Image, ImageTk  

# --- Database setup ---
def init_db():
    conn = sqlite3.connect("bmi.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT)""")
    #  a new data row was added here.
    c.execute("""CREATE TABLE IF NOT EXISTS bmi_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                weight REAL,
                height REAL,
                bmi REAL,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    conn.commit()
    conn.close()

init_db()

class BMIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pro BMI Calculator v2.0")
        self.root.geometry("400x650")
        self.root.resizable(False, False)
        
        # Colors - Modern Dark Theme
        self.bg_color = "#1e272e"
        self.card_color = "#2f3542"
        self.accent_color = "#575fcf"
        self.text_color = "#ffffff"
        self.green = "#05c46b"
        self.red = "#ff3f34"
        
        self.user_id = None
        self.login_screen()

    def set_background(self, img_path):
        try:
            img = Image.open(img_path)
            img = img.resize((400, 650), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(img)
            bg_label = tk.Label(self.root, image=self.bg_photo)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            self.root.config(bg=self.bg_color)
            print(f"Image Error: {e}")

    # The y_pos is set to 0.5 (center) by default.
    def create_card(self, height=400, y_pos=0.5):
        card = tk.Frame(self.root, bg=self.card_color, padx=20, pady=20, highlightthickness=1, highlightbackground="#3d4451")
        card.place(relx=0.5, rely=y_pos, anchor="center", width=340, height=height)
        return card

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def on_entry_click(self, entry, placeholder, is_pass=False):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="white")
            if is_pass: entry.config(show="*")

    # ---------------- LOGIN SCREEN ----------------
    def login_screen(self):
        self.clear_screen()
        self.set_background("login.jpg") 
        
        tk.Label(self.root, text="Welcome to Your Health Journey!", font=("Segoe UI", 18, "bold"), 
                 bg=self.bg_color, fg=self.accent_color).pack(pady=(40, 10))
        tk.Label(self.root, text="Please login to continue", font=("Segoe UI", 10), 
                 bg=self.bg_color, fg="gray").pack()

        # since y_pos is not specified here, it is set to default(0.5).
        card = self.create_card(height=350)
        
        tk.Label(card, text="Username", bg=self.card_color, fg="gray", font=("Segoe UI", 9)).pack(anchor="w", padx=10, pady=(10,0))
        self.username_entry = tk.Entry(card, font=("Segoe UI", 12), bg="#3d4451", fg="gray", borderwidth=0, justify="center")
        self.username_entry.insert(0, "Username")
        self.username_entry.bind("<FocusIn>", lambda e: self.on_entry_click(self.username_entry, "Username"))
        self.username_entry.pack(pady=10, ipady=8, fill="x")

        tk.Label(card, text="Password", bg=self.card_color, fg="gray", font=("Segoe UI", 9)).pack(anchor="w", padx=10)
        self.password_entry = tk.Entry(card, font=("Segoe UI", 12), bg="#3d4451", fg="gray", borderwidth=0, justify="center")
        self.password_entry.insert(0, "Password")
        self.password_entry.bind("<FocusIn>", lambda e: self.on_entry_click(self.password_entry, "Password", True))
        self.password_entry.pack(pady=10, ipady=8, fill="x")

        tk.Button(card, text="LOGIN", font=("Segoe UI", 12, "bold"), bg=self.accent_color, fg="white", 
                  cursor="hand2", borderwidth=0, command=self.login).pack(pady=20, fill="x", ipady=5)
        
        tk.Button(self.root, text="Create new account", font=("Segoe UI", 10, "underline"), bg=self.bg_color, 
                  fg=self.green, borderwidth=0, cursor="hand2", command=self.register_screen).pack(side="bottom", pady=40)

    # ---------------- REGISTER SCREEN ----------------
    def register_screen(self):
        self.clear_screen()
        self.set_background("background.jpg") 

        tk.Label(self.root, text="Join Us", font=("Segoe UI", 26, "bold"), 
                 bg=self.bg_color, fg=self.green).pack(pady=(40, 10))

         # since y_pos is not specified here, it is set to default(0.5).
        card = self.create_card(height=350)

        self.reg_username = tk.Entry(card, font=("Segoe UI", 12), bg="#3d4451", fg="gray", borderwidth=0, justify="center")
        self.reg_username.insert(0, "New Username")
        self.reg_username.bind("<FocusIn>", lambda e: self.on_entry_click(self.reg_username, "New Username"))
        self.reg_username.pack(pady=15, ipady=8, fill="x")

        self.reg_password = tk.Entry(card, font=("Segoe UI", 12), bg="#3d4451", fg="gray", borderwidth=0, justify="center")
        self.reg_password.insert(0, "New Password")
        self.reg_password.bind("<FocusIn>", lambda e: self.on_entry_click(self.reg_password, "New Password", True))
        self.reg_password.pack(pady=15, ipady=8, fill="x")

        tk.Button(card, text="REGISTER", font=("Segoe UI", 12, "bold"), bg=self.green, fg="white", 
                  cursor="hand2", borderwidth=0, command=self.register).pack(pady=20, fill="x", ipady=5)
        
        tk.Button(card, text="Back to Login", font=("Segoe UI", 10), bg=self.card_color, 
                  fg="gray", borderwidth=0, command=self.login_screen).pack()

    # ---------------- DASHBOARD (CALCULATOR) ----------------
    def dashboard_screen(self):
        self.clear_screen()
        self.set_background("dashboard_bg.jpg")

        tk.Label(self.root, text="Access Your BMI Dashboard", font=("Segoe UI", 22, "bold"), 
                 bg=self.bg_color, fg=self.text_color).pack(pady=30)

        # only here, the box has been moved slightly down by changing y_pos=0.56.
        card = self.create_card(height=520, y_pos=0.56) 

        tk.Label(card, text="Weight (kg)", bg=self.card_color, fg="white").pack(pady=(10,0))
        self.weight_entry = tk.Entry(card, font=("Segoe UI", 16), bg="#3d4451", fg="white", borderwidth=0, justify="center")
        self.weight_entry.pack(pady=5, ipady=5, fill="x")

        tk.Label(card, text="Height (m)", bg=self.card_color, fg="white").pack()
        self.height_entry = tk.Entry(card, font=("Segoe UI", 16), bg="#3d4451", fg="white", borderwidth=0, justify="center")
        self.height_entry.pack(pady=5, ipady=5, fill="x")

        tk.Button(card, text="CALCULATE", font=("Segoe UI", 12, "bold"), bg=self.accent_color, fg="white", 
                  borderwidth=0, command=self.calculate_bmi).pack(pady=15, fill="x", ipady=8)

        self.result_label = tk.Label(card, text="Enter details to start", font=("Segoe UI", 13, "bold"), 
                                     bg=self.card_color, fg="gray")
        self.result_label.pack(pady=5)

        self.prog_bg = tk.Frame(card, bg="#1e272e", width=280, height=12)
        self.prog_bg.pack_propagate(False)
        self.prog_bg.pack(pady=5)
        self.progress_fill = tk.Frame(self.prog_bg, bg=self.green, width=0, height=12)
        self.progress_fill.pack(side="left")

        # ---- newly added HISTORY button ----
        tk.Button(card, text="VIEW HISTORY", font=("Segoe UI", 10, "bold"), bg="#ffa502", fg="white", 
                  borderwidth=0, cursor="hand2", command=self.access_history).pack(pady=10, fill="x", ipady=5)

        btn_frame = tk.Frame(card, bg=self.card_color)
        btn_frame.pack(side="bottom", fill="x", pady=10)
        
        tk.Button(btn_frame, text="Clear", bg=self.red, fg="white", borderwidth=0, width=10, command=self.clear_fields).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Logout", bg="#4b4b4b", fg="white", borderwidth=0, width=10, command=self.logout).pack(side="right", padx=5)

    # ---------------- NEW HISTORY WINDOW ----------------
    def access_history(self):
        history_win = tk.Toplevel(self.root)
        history_win.title("BMI History Log")
        history_win.geometry("500x400")
        history_win.config(bg=self.bg_color)

        tk.Label(history_win, text="Your History", font=("Segoe UI", 18, "bold"), bg=self.bg_color, fg=self.green).pack(pady=15)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background=self.card_color, foreground="white", fieldbackground=self.card_color, borderwidth=0)
        style.map("Treeview", background=[('selected', self.accent_color)])

        columns = ("date", "weight", "height", "bmi")
        tree = ttk.Treeview(history_win, columns=columns, show="headings")
        
        tree.heading("date", text="Date & Time")
        tree.heading("weight", text="Weight (kg)")
        tree.heading("height", text="Height (m)")
        tree.heading("bmi", text="BMI")

        conn = sqlite3.connect("bmi.db")
        data = conn.execute("SELECT date, weight, height, bmi FROM bmi_results WHERE user_id=? ORDER BY date DESC", (self.user_id,)).fetchall()
        for row in data:
            tree.insert("", tk.END, values=row)
        conn.close()

        tree.pack(fill="both", expand=True, padx=20, pady=20)

    # ---------------- LOGIC ----------------
    def register(self):
        u, p = self.reg_username.get(), self.reg_password.get()
        if u in ["", "New Username"] or p in ["", "New Password"]:
            messagebox.showwarning("Warning", "Fill all fields!")
            return
        conn = sqlite3.connect("bmi.db")
        try:
            conn.execute("INSERT INTO users (username, password) VALUES (?,?)", (u, p))
            conn.commit()
            messagebox.showinfo("Success", "Account created!")
            self.login_screen()
        except: messagebox.showerror("Error", "Username exists!")
        finally: conn.close()

    def login(self):
        u, p = self.username_entry.get(), self.password_entry.get()
        conn = sqlite3.connect("bmi.db")
        user = conn.execute("SELECT id FROM users WHERE username=? AND password=?", (u, p)).fetchone()
        conn.close()
        if user: 
            self.user_id = user[0]
            self.dashboard_screen()
        else: messagebox.showerror("Error", "Invalid login!")

    def calculate_bmi(self):
        try:
            w, h = float(self.weight_entry.get()), float(self.height_entry.get())
            if h <= 0: raise ValueError
            bmi = round(w / (h**2), 2)
            
            if bmi < 18.5: cat, col = "Underweight", "#3498db"
            elif bmi < 24.9: cat, col = "Normal", "#2ecc71"
            elif bmi < 29.9: cat, col = "Overweight", "#f39c12"
            else: cat, col = "Obese", "#e74c3c"

            self.result_label.config(text=f"BMI: {bmi}\n{cat}", fg=col)
            fill_w = min(int((bmi/50)*280), 280)
            self.progress_fill.config(width=fill_w, bg=col)

            conn = sqlite3.connect("bmi.db")
            conn.execute("INSERT INTO bmi_results (user_id, weight, height, bmi) VALUES (?,?,?,?)",
                         (self.user_id, w, h, bmi))
            conn.commit()
            conn.close()
        except: messagebox.showerror("Input Error", "Enter valid Weight (kg) & Height (m)!")

    def clear_fields(self):
        self.weight_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.result_label.config(text="Enter details", fg="gray")
        self.progress_fill.config(width=0)

    def logout(self):
        self.user_id = None
        self.login_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()