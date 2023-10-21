import tkinter as tk


def showArithOpsDialog(root):

    # Create the dialog
    dialog = tk.Toplevel(root)
    dialog.grab_set()
    dialog.title("Arithmetic Operations")

    dialog.geometry("360x380")
    
    def addition_click():
        from dialogs.ArithDialogs.addition import openAddDialog
        openAddDialog(dialog)

    def subtraction_click():
        from dialogs.ArithDialogs.subtraction import openSubDialog
        openSubDialog(dialog)

    def multiplication_click():
        from dialogs.ArithDialogs.mutliplication import openMultiplyDialog
        openMultiplyDialog(dialog)

    def squaring_click():
        from dialogs.ArithDialogs.squaring import openSquaringDialog
        openSquaringDialog(dialog)

    def shifting_click():
        from dialogs.ArithDialogs.shifting import openShiftDialog
        openShiftDialog(dialog)

    def normalization_click():
        from dialogs.ArithDialogs.normalization import openNormalizeDialog
        openNormalizeDialog(dialog)

    def accumulation_click():
        from dialogs.ArithDialogs.accum import openAccumDialog
        openAccumDialog(dialog)

    # Create and configure a frame with padding
    frame = tk.Frame(dialog, padx=20, pady=10)
    frame.pack()

    # Create and place the buttons vertically with fixed width
    button_width = 20

    addition_button = tk.Button(frame, text="Addition", command=addition_click, width=button_width)
    subtraction_button = tk.Button(frame, text="Subtraction", command=subtraction_click, width=button_width)
    multiplication_button = tk.Button(frame, text="Multiplication", command=multiplication_click, width=button_width)
    squaring_button = tk.Button(frame, text="Squaring", command=squaring_click, width=button_width)
    shifting_button = tk.Button(frame, text="Shifting", command=shifting_click, width=button_width)
    normalization_button = tk.Button(frame, text="Normalization", command=normalization_click, width=button_width)
    accumulation_button = tk.Button(frame, text="Accumulation", command=accumulation_click, width=button_width)

    # Add vertical space between buttons
    vertical_space = 10
    addition_button.pack(pady=(0, vertical_space))
    subtraction_button.pack(pady=vertical_space)
    multiplication_button.pack(pady=vertical_space)
    squaring_button.pack(pady=vertical_space)
    shifting_button.pack(pady=vertical_space)
    normalization_button.pack(pady=vertical_space)
    accumulation_button.pack(pady=(vertical_space, 0))

    dialog.wait_window()
