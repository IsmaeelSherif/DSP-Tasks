import tkinter as tk
from tkinter import scrolledtext
from utils import wave_drawer
from utils.example_reader import readInputFromFile
from utils import arithmetic_ops
from testwave.comparesignals import compareSignalToFile

def openAddDialog(root):

    augmentedWaves = []

    def open_file_picker():
        inputWave, displayName = readInputFromFile()
        if inputWave:
            nonlocal augmentedWaves
            if len(augmentedWaves) > 0:
                listbox.insert(tk.END, "\n" + displayName)
            else:
                listbox.insert(tk.END, displayName)
            
            augmentedWaves = arithmetic_ops.addWave(inputWave, augmentedWaves)
            print('add result', augmentedWaves)
            

    def clear_all():
        listbox.delete(1.0, tk.END)
        nonlocal augmentedWaves
        augmentedWaves = []

    def show():
        wave_drawer.draw(augmentedWaves)

    def compare():
        compareSignalToFile(augmentedWaves)

    dialog = tk.Toplevel(root)
    dialog.grab_set()
    dialog.title("Signal Addition")
    dialog.geometry("360x380")

    # Create a frame for the buttons
    button_frame = tk.Frame(dialog, padx=10, pady=10)
    button_frame.pack()

    # Open File Picker Button
    open_file_button = tk.Button(button_frame, text="Add Input", command=open_file_picker)
    open_file_button.grid(row=0, column=0, padx=5)

    # Clear All Button
    clear_all_button = tk.Button(button_frame, text="Clear All", command=clear_all)
    clear_all_button.grid(row=0, column=1, padx=5)

    # Create a scrolled text widget for the list view
    listbox_frame = tk.Frame(dialog)
    listbox_frame.pack()

    listbox = scrolledtext.ScrolledText(listbox_frame, width=40, height=10, wrap=tk.WORD)
    listbox.grid(row=0, column=0, padx=10, pady=5)

    button_frame2 = tk.Frame(dialog, padx=10, pady=10)
    button_frame2.pack()

    show_button = tk.Button(button_frame2, text="Show", command=show)
    show_button.grid(row=0, column=0, padx=5)

    compare_button = tk.Button(button_frame2, text="Compare", command=compare)
    compare_button.grid(row=0, column=1, padx=5)

    dialog.wait_window()