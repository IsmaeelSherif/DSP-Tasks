import tkinter as tk
from models.wave import Wave


def newWaveDialog(root) -> Wave:
    newWave = None
    dialog = tk.Toplevel(root)

    # Create a label for the type field
    type_label = tk.Label(dialog, text="Type:")
    type_label.grid(row=0, column=0, columnspan=2, pady=5)

    # Create a StringVar to store the selected type
    selected_type = tk.StringVar(value="sin")

    # Create a frame for radio buttons
    type_frame = tk.Frame(dialog)
    type_frame.grid(row=1, column=0, columnspan=2)

    # Create radio buttons for "sine" and "cosine" and arrange them horizontally
    sine_radio = tk.Radiobutton(type_frame, text="Sine", variable=selected_type, value="sin")
    cosine_radio = tk.Radiobutton(type_frame, text="Cosine", variable=selected_type, value="cos")

    sine_radio.grid(row=0, column=0, padx=5)
    cosine_radio.grid(row=0, column=1, padx=5)

    # Create entry widgets for the other input fields
    amplitude_label = tk.Label(dialog, text="Amplitude")
    amplitude_entry = tk.Entry(dialog)

    analog_freq_label = tk.Label(dialog, text="Analog Frequency")
    analog_freq_entry = tk.Entry(dialog)

    sampling_freq_label = tk.Label(dialog, text="Sampling Frequency")
    sampling_freq_entry = tk.Entry(dialog)

    phase_shift_label = tk.Label(dialog, text="Phase Shift")
    phase_shift_entry = tk.Entry(dialog)

    amplitude_label.grid(row=2, column=0, pady=5, padx=5)
    amplitude_entry.grid(row=2, column=1, pady=5, padx=5)
    analog_freq_label.grid(row=3, column=0, pady=5, padx=5)
    analog_freq_entry.grid(row=3, column=1, pady=5, padx=5)
    sampling_freq_label.grid(row=4, column=0, pady=5, padx=5)
    sampling_freq_entry.grid(row=4, column=1, pady=5, padx=5)
    phase_shift_label.grid(row=5, column=0, pady=5, padx=5)
    phase_shift_entry.grid(row=5, column=1, pady=5, padx=5)

    # Function to save the input data to the dictionary
    def save_input():
        try:
            type = selected_type.get()
            amplitude = int(amplitude_entry.get())
            analogFreq = int(analog_freq_entry.get())
            fs = int(sampling_freq_entry.get())
            phase = float(phase_shift_entry.get())

            nonlocal newWave
            newWave = Wave(
                isSine=type == 'sin',
                amplitude=amplitude,
                analogF=analogFreq,
                fs=fs,
                phaseShift=phase
            )
            dialog.destroy()
        except:
            print('please fill fields correctly')

    save_button = tk.Button(dialog, width=15, height=3, text="Save", command=save_input)
    save_button.grid(row=6, column=0, columnspan=2, pady=10)

    # Block execution until the dialog is closed
    dialog.wait_window()

    return newWave