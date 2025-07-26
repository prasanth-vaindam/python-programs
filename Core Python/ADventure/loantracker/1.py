import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class LoanPayoffTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Loan Payoff Motivator")
        self.root.geometry("900x700")

        # Initial loan data for BOI
        self.initial_loan_amount = 1934397.00
        self.current_balance = self.initial_loan_amount
        self.emi_amount = 23955.00
        self.start_date = datetime.now()

        # Payment history
        self.payment_history = []

        # Create GUI elements
        self.create_widgets()
        self.update_display()

    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header with motivational title
        header = ttk.Label(main_frame, text="🚀 Loan Payoff Journey",
                           font=("Helvetica", 16, "bold"))
        header.pack(pady=10)

        # Current balance display
        balance_frame = ttk.LabelFrame(main_frame, text="Current Status", padding=10)
        balance_frame.pack(fill=tk.X, pady=10)

        self.balance_label = ttk.Label(balance_frame,
                                       text=f"Initial Loan: ₹{self.initial_loan_amount:,.2f}",
                                       font=("Helvetica", 12))
        self.balance_label.pack(anchor=tk.W)

        self.remaining_label = ttk.Label(balance_frame,
                                         font=("Helvetica", 14, "bold"),
                                         foreground="red")
        self.remaining_label.pack(anchor=tk.W, pady=5)

        self.percentage_label = ttk.Label(balance_frame,
                                          font=("Helvetica", 12))
        self.percentage_label.pack(anchor=tk.W)

        # Payment section
        payment_frame = ttk.LabelFrame(main_frame, text="Make Payment", padding=10)
        payment_frame.pack(fill=tk.X, pady=10)

        ttk.Label(payment_frame, text="Payment Amount:").pack(anchor=tk.W)
        self.payment_entry = ttk.Entry(payment_frame)
        self.payment_entry.pack(fill=tk.X, pady=5)

        ttk.Label(payment_frame, text="Payment Type:").pack(anchor=tk.W)
        self.payment_type = tk.StringVar(value="EMI")
        ttk.Radiobutton(payment_frame, text="Regular EMI", variable=self.payment_type,
                        value="EMI").pack(anchor=tk.W)
        ttk.Radiobutton(payment_frame, text="Part Payment", variable=self.payment_type,
                        value="Part").pack(anchor=tk.W)

        pay_button = ttk.Button(payment_frame, text="Record Payment",
                                command=self.record_payment)
        pay_button.pack(pady=10)

        # Progress visualization
        viz_frame = ttk.LabelFrame(main_frame, text="Progress Visualization", padding=10)
        viz_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.figure = plt.Figure(figsize=(8, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=viz_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Motivational messages
        self.motivation_label = ttk.Label(main_frame,
                                          text="",
                                          font=("Helvetica", 10, "italic"),
                                          wraplength=800)
        self.motivation_label.pack(pady=10)

        # Payment history
        history_frame = ttk.LabelFrame(main_frame, text="Payment History", padding=10)
        history_frame.pack(fill=tk.BOTH, pady=10)

        columns = ("Date", "Amount", "Type", "Balance")
        self.history_tree = ttk.Treeview(history_frame, columns=columns, show="headings")
        for col in columns:
            self.history_tree.heading(col, text=col)
            self.history_tree.column(col, width=100, anchor=tk.CENTER)
        self.history_tree.pack(fill=tk.BOTH, expand=True)

    def update_display(self):
        # Update balance display
        self.remaining_label.config(text=f"Remaining Balance: ₹{self.current_balance:,.2f}")

        # Calculate percentage paid
        percent_paid = ((self.initial_loan_amount - self.current_balance) /
                        self.initial_loan_amount * 100)
        self.percentage_label.config(
            text=f"Progress: {percent_paid:.1f}% paid ({self.initial_loan_amount - self.current_balance:,.2f} of {self.initial_loan_amount:,.2f})"
        )

        # Update chart
        self.update_chart()

        # Update motivation message
        self.update_motivation(percent_paid)

        # Update payment history
        self.update_history()

    def update_chart(self):
        self.ax.clear()

        # Data for chart
        labels = ['Paid', 'Remaining']
        sizes = [self.initial_loan_amount - self.current_balance, self.current_balance]
        colors = ['#4CAF50', '#F44336']

        # Create pie chart
        self.ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                    startangle=90, wedgeprops=dict(width=0.4))
        self.ax.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle
        self.ax.set_title('Loan Payoff Progress')

        self.canvas.draw()

    def update_motivation(self, percent_paid):
        if percent_paid < 10:
            msg = "Every big journey begins with a single step! You've started your debt-free journey."
        elif percent_paid < 30:
            msg = "Keep going! Consistency is key. Each payment brings you closer to financial freedom."
        elif percent_paid < 50:
            msg = "You're making great progress! The halfway point is within reach."
        elif percent_paid < 70:
            msg = "More than halfway there! Your future self will thank you for this discipline."
        elif percent_paid < 90:
            msg = "You're in the home stretch! The finish line is getting closer every day."
        else:
            msg = "Almost there! You're demonstrating incredible financial discipline. The end is in sight!"

        self.motivation_label.config(text=msg)

    def update_history(self):
        # Clear existing entries
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)

        # Add all payments to history
        for payment in self.payment_history:
            self.history_tree.insert("", tk.END, values=payment)

    def record_payment(self):
        try:
            amount = float(self.payment_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Payment amount must be positive")
                return

            if amount > self.current_balance:
                messagebox.showwarning("Warning", "Payment exceeds remaining balance")
                return

            payment_type = self.payment_type.get()

            # Update balance
            self.current_balance -= amount
            if self.current_balance < 0.01:  # Handle floating point precision
                self.current_balance = 0.00

            # Record payment
            payment_date = datetime.now().strftime("%Y-%m-%d %H:%M")
            self.payment_history.append(
                (payment_date, f"₹{amount:,.2f}", payment_type, f"₹{self.current_balance:,.2f}")
            )

            # Update display
            self.update_display()
            self.payment_entry.delete(0, tk.END)

            # Show success message
            messagebox.showinfo("Success", f"Payment of ₹{amount:,.2f} recorded successfully!")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid payment amount")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoanPayoffTracker(root)
    root.mainloop()