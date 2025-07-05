import tkinter as tk
from tkinter import messagebox
import joblib
import pickle
import numpy as np

model = joblib.load('rf_model.pkl')
vectorizer = joblib.load('feature_extraction.pkl')

def predict_mail():
    user_input = entry.get("1.0", tk.END).strip()
    
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter a message to check.")
        return

    input_features = vectorizer.transform([user_input])
    prediction = model.predict(input_features)


    if prediction[0] == 1:
        result_label.config(text="Prediction: Ham Mail ✅", fg="green")
    else:
        result_label.config(text="Prediction: Spam Mail ❌", fg="red")

window = tk.Tk()
window.title("Spam Mail Detector")
window.geometry("400x300")
window.resizable(False, False)


heading = tk.Label(window, text="Spam Mail Detector", font=("Arial", 18, "bold"))
heading.pack(pady=10)


entry = tk.Text(window, height=5, width=40, font=("Arial", 12))
entry.pack(pady=10)


predict_btn = tk.Button(window, text="Predict", command=predict_mail, font=("Arial", 12), bg="blue", fg="white")
predict_btn.pack(pady=10)


result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

window.mainloop()
