from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import os

class ShowAttendance:
    def run(self):
        self.root = Tk()
        self.root.geometry("800x500")
        self.root.title("Attendance Data Viewer")
        self.root.resizable(True, True)
        self.createUI()
        self.root.mainloop()

    def createUI(self):
        # Frame for table
        table_frame = Frame(self.root)
        table_frame.pack(pady=20, fill=BOTH, expand=True)

        # Create Treeview (table)
        self.table = ttk.Treeview(table_frame, columns=(), show="headings")
        self.table.pack(fill=BOTH, expand=True)

        # Add vertical and horizontal scrollbars
        scrollbar_y = ttk.Scrollbar(table_frame, orient=VERTICAL, command=self.table.yview)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL, command=self.table.xview)
        scrollbar_x.pack(side=BOTTOM, fill=X)

        self.table.configure(yscroll=scrollbar_y.set, xscroll=scrollbar_x.set)

        # Load and display the CSV data automatically
        self.loadCsvFile()

    def loadCsvFile(self):
        """Load data from the CSV file (atten.csv) and display it in the table."""
        file_path = os.path.join(os.getcwd(), "attend.csv")  # File path in the same directory
        # print(file_path)
        if os.path.exists(file_path):
            self.displayCsvData(file_path)
        else:
            messagebox.showerror("Error", f"File 'atten.csv' not found in the current directory.")

    def displayCsvData(self, file_path):
        """Read CSV file and populate the table."""
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                data = list(reader)
                print(data)

                if len(data) == 0:
                    messagebox.showerror("Error", "The CSV file is empty.")
                    return

                # Clear existing data
                self.table.delete(*self.table.get_children())

                # Define table columns manually
                columns = ["Name", "Roll No", "Department", "Date", "Time"]  # Custom column titles
                self.table["columns"] = columns
                self.table["show"] = "headings"

                for col in columns:
                    self.table.heading(col, text=col)
                    self.table.column(col, width=150, anchor="center")

                # # Add data rows
                # for row in data:
                #     # Ensure each row is correctly parsed
                #     row = self.format_row(row)
                #     self.table.insert("", "end", values=row)

                # Add data rows
                for row in data[1:]:
                    self.table.insert("", "end", values=row)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV file: {e}")

    def format_row(self, row):
        """Format each row to ensure it matches the expected structure."""
        # Example: ('Computer Application',) needs to be converted to a string
        formatted_row = []
        for item in row:
            if isinstance(item, tuple):
                item = ", ".join(item)  # Convert tuple to a comma-separated string
            formatted_row.append(item)
        return formatted_row


# Run the application
# app = ShowAttendance()
# app.run()
