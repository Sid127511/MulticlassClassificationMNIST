import tkinter as tk

root = tk.Tk()
root.title("Codespaces GUI App")
root.geometry("400x200")

label = tk.Label(root, text="Hello from Desktop Lite!", font=("Arial", 16))
label.pack(pady=40)

btn = tk.Button(root, text="Close App", command=root.quit)
btn.pack()

root.mainloop()