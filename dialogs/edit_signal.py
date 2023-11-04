

import tkinter as tk
from tkinter import scrolledtext

def openEditDialog(root, amplitudes, phases):

    new_amps = None
    new_phases = None

    def cancel():
        dialog.destroy()

    def save():

        nonlocal new_amps
        nonlocal new_phases
        new_amps = []
        new_phases = []

        content = listbox.get("1.0", "end-1c")  # Get all lines of text
        lines = content.split('\n')  # Split the text into lines

        for line in lines:
            parts = line.split()
            
            if len(parts) > 0:
                xAsString = parts[0].replace('f', '')
                yAsString = parts[1].replace('f', '')

                amp = float(xAsString)
                phas = float(yAsString)

                new_amps.append(amp)
                new_phases.append(phas)
        dialog.destroy()


    dialog = tk.Toplevel(root)
    dialog.grab_set()
    dialog.title("Edit Signal")
    dialog.geometry("360x380")


    # Create a scrolled text widget for the list view
    listbox_frame = tk.Frame(dialog)
    listbox_frame.pack()

    listbox = scrolledtext.ScrolledText(listbox_frame, width=40, height=10, wrap=tk.WORD)
    listbox.grid(row=0, column=0, padx=10, pady=5)


    button_frame2 = tk.Frame(dialog, padx=10, pady=10)
    button_frame2.pack()

    save_button = tk.Button(button_frame2, text="Save", command=save)
    save_button.grid(row=0, column=0, padx=5)

    cancel_button = tk.Button(button_frame2, text="Cancel", command=cancel)
    cancel_button.grid(row=0, column=1, padx=5)


    for i in range(len(amplitudes)):
        listbox.insert(tk.END, str(amplitudes[i]) + ' ' + str(phases[i]) + '\n')

    dialog.wait_window()


    return new_amps, new_phases



