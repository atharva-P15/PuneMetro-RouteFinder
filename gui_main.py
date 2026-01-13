import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from metro_data import metro_graph
from algorithms import dijkstra

class MetroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pune Metro Route Finder")
        self.root.state('zoomed')  
        self.root.configure(bg="purple")  

       
        self.main_frame = tk.Frame(root, padx=20, pady=20, bg="purple")
        self.main_frame.pack(fill='both', expand=True)

  
        self.logo_frame = tk.Frame(self.main_frame, bg="purple")
        self.logo_frame.pack(pady=(10, 30))

        try:
            logo_img = Image.open("logo.jpg")  
            logo_img = logo_img.resize((150, 150))  
            self.logo_photo = ImageTk.PhotoImage(logo_img)
            tk.Label(self.logo_frame, image=self.logo_photo, bg="purple").pack()
        except Exception:
            tk.Label(self.logo_frame, text="Logo Image Here", font=("Arial", 14), bg="purple", fg="white").pack()


  
        self.input_frame = tk.Frame(self.main_frame, bg="purple")
        self.input_frame.pack(pady=10)

 
        tk.Label(self.input_frame, text="Select Source Station:", font=("Arial", 12), bg="purple", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.source_var = tk.StringVar()
        self.source_menu = ttk.Combobox(self.input_frame, textvariable=self.source_var, values=list(metro_graph.keys()), state="readonly", width=30)
        self.source_menu.grid(row=0, column=1, padx=10, pady=10)

   
        tk.Label(self.input_frame, text="Select Destination Station:", font=("Arial", 12), bg="purple", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.dest_var = tk.StringVar()
        self.dest_menu = ttk.Combobox(self.input_frame, textvariable=self.dest_var, values=list(metro_graph.keys()), state="readonly", width=30)
        self.dest_menu.grid(row=1, column=1, padx=10, pady=10)

   
        tk.Button(self.input_frame, text="Find Route", command=self.find_route, font=("Arial", 11), width=20, bg="white", fg="purple").grid(row=2, column=0, columnspan=2, pady=15)


        self.result_text = tk.Text(self.main_frame, height=10, width=80, font=("Courier New", 11), bg="white", fg="black")
        self.result_text.pack(pady=20)

    def find_route(self):
        source = self.source_var.get()
        dest = self.dest_var.get()

        if not source or not dest:
            messagebox.showwarning("Input Error", "Please select both stations.")
            return

        if source == dest:
            messagebox.showinfo("Same Station", "Source and destination are the same.")
            return

        path, total_time = dijkstra(metro_graph, source, dest)

        if path:
            result = f"Route from {source} to {dest}:\n"
            result += " -> ".join(path)
            result += f"\n\nTotal stations: {len(path)}"
            result += f"\nEstimated travel time: {total_time} minutes"
        else:
            result = "No route found."

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)


if __name__ == "__main__":
    root = tk.Tk()
    app = MetroApp(root)
    root.mainloop()
