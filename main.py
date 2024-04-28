from tkinter import *
from tkinter import ttk
from marker import WaterMarker


# destroy unneeded widgets
def clear_window():
    for widget in window.grid_slaves()[:-8]:
        widget.destroy()


def img_mode():
    clear_window()

    # Watermark select label
    mark_select_label = Label(text="Select watermark", width=16, font=("Helvetica", 10, "bold"))
    mark_select_label.grid(column=0, row=6)

    # Watermark select button, update watermark label with chosen filename
    mark_select_button = Button(text="Browse", width=12,
                                command=lambda:
                                [marker.open_mark_dialog(),
                                 mark_select_label.config(
                                     text=marker.mark_select_label, font=("Helvetica", 10, "normal"))])
    mark_select_button.grid(column=1, row=6)

    # Separator line
    line3 = ttk.Separator(window, orient="horizontal")
    line3.grid(column=0, row=7, columnspan=2, sticky="ew")

    # Watermark opacity label
    mark_opacity_label = Label(text="Watermark opacity %", width=16, pady=3, font=("Helvetica", 10, "bold"))
    mark_opacity_label.grid(column=0, row=8)

    # Watermark opacity setter
    mark_opacity_setter = Spinbox(from_=0, to=100, width=13)
    mark_opacity_setter.grid(column=1, row=8)

    # Separator line
    line4 = ttk.Separator(window, orient="horizontal")
    line4.grid(column=0, row=9, columnspan=2, sticky="ew")

    # Watermark position label
    mark_position_label = Label(text="Watermark position", width=16, font=("Helvetica", 10, "bold"))
    mark_position_label.grid(column=0, row=10)

    # Watermark position setter
    mark_position_setter = Listbox(width=15, height=4)
    mark_position_list = ["top left", "top right", "bottom left", "bottom right"]
    for pos in mark_position_list:
        mark_position_setter.insert(mark_position_list.index(pos), pos)
    mark_position_setter.grid(column=1, row=10)

    # Separator line
    line5 = ttk.Separator(window, orient="horizontal")
    line5.grid(column=0, row=11, columnspan=2, sticky="ew")

    # Add watermark button
    add_mark_button = Button(text="ADD WATERMARK", font=("Helvetica", 12, "bold"),
                             command=lambda: marker.add_img_watermark(
                                 mark_opacity_setter.get(),
                                 mark_position_setter.get(mark_position_setter.curselection())))
    add_mark_button.grid(column=0, row=12, columnspan=2)

    window.update()


def text_mode():
    clear_window()

    # Text entry label
    text_entry_label = Label(text="Watermark text", font=("Helvetica", 10, "bold"), pady=3)
    text_entry_label.grid(column=0, row=6)

    # Text entry field
    text_entry = Entry(width=17)
    text_entry.grid(column=1, row=6)

    # Separator line
    line6 = ttk.Separator(window, orient="horizontal")
    line6.grid(column=0, row=7, columnspan=2, sticky="ew")

    # Text color example label
    text_color_label = Label(text="Watermark color", font=("Helvetica", 10, "bold"))
    text_color_label.grid(column=0, row=8)

    # Text color picker button
    text_color_button = Button(text="Change color",
                               command=lambda: [marker.open_color_dialog(),
                                                text_color_label.config(fg=marker.text_select_color[1])])

    text_color_button.grid(column=1, row=8)

    # Separator line
    line7 = ttk.Separator(window, orient="horizontal")
    line7.grid(column=0, row=9, columnspan=2, sticky="ew")

    # Text font size label
    text_font_size_label = Label(text="Font Size", width=16, pady=3, font=("Helvetica", 10, "bold"))
    text_font_size_label.grid(column=0, row=10)

    # Text font size setter
    text_font_size_setter = Spinbox(from_=1, to=200, width=13)
    text_font_size_setter.grid(column=1, row=10)

    # Separator line
    line8 = ttk.Separator(window, orient="horizontal")
    line8.grid(column=0, row=11, columnspan=2, sticky="ew")

    # Text opacity label
    text_opacity_label = Label(text="Watermark opacity %", width=16, pady=3, font=("Helvetica", 10, "bold"))
    text_opacity_label.grid(column=0, row=12)

    # Text opacity setter
    text_opacity_setter = Spinbox(from_=0, to=100, width=13)
    text_opacity_setter.grid(column=1, row=12)

    # Separator line
    line9 = ttk.Separator(window, orient="horizontal")
    line9.grid(column=0, row=13, columnspan=2, sticky="ew")

    # Text position label
    text_position_label = Label(text="Watermark position", width=16, font=("Helvetica", 10, "bold"))
    text_position_label.grid(column=0, row=14)

    # Text position setter
    text_position_setter = Listbox(width=15, height=4)
    text_position_list = ["top left", "top right", "bottom left", "bottom right"]
    for pos in text_position_list:
        text_position_setter.insert(text_position_list.index(pos), pos)
    text_position_setter.grid(column=1, row=14)

    # Separator line
    line10 = ttk.Separator(window, orient="horizontal")
    line10.grid(column=0, row=15, columnspan=2, sticky="ew")

    # Add watermark button
    add_text_button = Button(text="ADD WATERMARK", font=("Helvetica", 12, "bold"),
                             command=lambda: marker.add_text_watermark(
                                 text_font_size_setter.get(),
                                 text_opacity_setter.get(),
                                 text_position_setter.get(text_position_setter.curselection()),
                                 text_entry.get()))

    add_text_button.grid(column=0, row=16, columnspan=2)

    window.update()


# Create instance of WaterMarker object
marker = WaterMarker()

# Base Window
window = Tk()
window.title("Image Watermarker")
window.minsize(width=270, height=150)
window.config(padx=10, pady=10)

# Title Label
title_label = Label(text="Image Watermarker \nby Gáspár Németh", font=("Helvetica", 12, "bold"))
title_label.grid(column=0, row=0, columnspan=2)

# Separator line
line0 = ttk.Separator(window, orient="horizontal")
line0.grid(column=0, row=1, columnspan=2, sticky="ew")

# Image select label
img_select_label = Label(text="Select image", width=16, font=("Helvetica", 10, "bold"))
img_select_label.grid(column=0, row=2)

# Image select button, update image label with chosen filename
img_select_button = Button(text="Browse", width=12,
                           command=lambda:
                           [marker.open_img_dialog(), img_select_label.config(text=marker.img_select_label,
                                                                              font=("Helvetica", 10, "normal"))])
img_select_button.grid(column=1, row=2)

# Separator line
line1 = ttk.Separator(window, orient="horizontal")
line1.grid(column=0, row=3, columnspan=2, sticky="ew")

# Mode switch
radio_state = IntVar()
switch_img_mode = Radiobutton(text="Image Watermark", value=1, variable=radio_state, command=img_mode)
switch_text_mode = Radiobutton(text="Text Watermark", value=2, variable=radio_state, command=text_mode)
switch_img_mode.grid(column=0, row=4)
switch_text_mode.grid(column=1, row=4)

# Separator line
line2 = ttk.Separator(window, orient="horizontal")
line2.grid(column=0, row=5, columnspan=2, sticky="ew")

window.mainloop()
