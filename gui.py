import tkinter as tk
import pickle
import numpy as np

model = pickle.load(open("mobile_model.pkl", "rb"))

def predict():
    try:
        screen = float(e1.get())
        apps = float(e2.get())
        social = float(e3.get())
        sleep = float(e4.get())

        data = np.array([[screen, apps, social, sleep]])
        result = model.predict(data)

        if result[0] == 1:
            label_result.config(text="⚠ Addicted to Mobile", fg="red")
        else:
            label_result.config(text="✅ Not Addicted", fg="green")

    except:
        label_result.config(text="Enter valid values")

root = tk.Tk()
root.title("Mobile Addiction Predictor")
root.geometry("400x400")

tk.Label(root, text="Screen Time (hrs)").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="App Usage (no. of apps)").pack()
e2 = tk.Entry(root)
e2.pack()

tk.Label(root, text="Social Media Time (hrs)").pack()
e3 = tk.Entry(root)
e3.pack()

tk.Label(root, text="Sleep Hours").pack()
e4 = tk.Entry(root)
e4.pack()

tk.Button(root, text="Predict", command=predict).pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()