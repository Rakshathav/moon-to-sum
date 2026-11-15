import tkinter as tk
root =tk.Tk()
root.title("moon to sum")
c =tk.Canvas(root, width=300,height=300, bg="#0b1026",highlightthickness=0)
c.pack()
is_moon =True
def draw():
    c.delete("all")
    bg="#0b1026" if is_moon else "#87ceeb"
    c.config(bg=bg)
    if is_moon:
        c.create_oval(90, 90, 210, 210, fill="#f5f3ce", outline="")
        c.create_oval(120, 80, 240, 200, fill=bg, outline="")  # crescent cut
    else:
        c.create_oval(90,90,210,210, fill ="#ffcc00",outline="")
    btn.config(text="Switch to Sun ☀️" if is_moon else "Switch to Moon 🌙")

def toggle():
    global is_moon
    is_moon = not is_moon
    draw()
btn =tk.Button(root, command=toggle, font=("Arial",14))
btn.pack(pady=10)
draw()
root.mainloop()