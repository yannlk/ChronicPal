from ttkthemes import ThemedTk


def root_init():
    """Initiate the Tkinter window and namely the Root Object, Returns Root"""
    root = ThemedTk(theme="equilux")  # Use a dark mode theme
    root.title('Anki Data Collection')
    root.geometry('800x800')
    return root


def clear_window(root):
    try:  # Remove Tkinter Widgets from previous iteration
        for widget in root.winfo_children():
            widget.destroy()
    except AttributeError:
        pass

