import tkinter as tk

PINK = "#F92061"
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}
window = tk.Tk()
# Code to add widgets will go here...
# frame a is the images with the glu
frame_a = tk.Frame(master=window, height=100, bg=PINK)
# frame a is the images with the glu
frame_b = tk.Frame(master=window, height=100, bg=PINK)

#greeting = tk.Label(text="Hello, Tkinter")
#greeting.pack()
label = tk.Label(master=frame_a, text="Cell type:", bg=PINK)
label.pack()
entry = tk.Entry(master=frame_a, fg="black", bg="white", width=10)
entry.pack()
image_name = entry.get()
label = tk.Label(
    master=frame_a,
    text="Enter the images with glucose",
    foreground="white",  # Set the text color to white
    background=PINK,  # Set the background color to black
    relief="raised"
    #width=25,
    #height=10
)
label.pack()
button = tk.Button(master=frame_a, text="Click me!", bg=PINK, fg="yellow")
button.pack()

frame_a.pack(fill=tk.X)
frame_b.pack(fill=tk.X)
window.mainloop()

#just a check