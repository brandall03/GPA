import os
os.environ['TK_SILENCE_DEPRECATION'] = "1"
import tkinter as tk
from tkinter import messagebox

class GPACalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("GPA Calculator")
        self.root.geometry("600x700")
        self.root.configure(bg='#2E2E2E')

        # Grade conversion dictionary
        self.grade_to_points = {
            'A+': 4.0, 'A': 4.0, 'A-': 3.7,
            'B+': 3.3, 'B': 3.0, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7,
            'D+': 1.3, 'D': 1.0, 'D-': 0.7,
            'F': 0.0
        }

        # Percentage to letter grade conversion
        self.percentage_to_letter = {
            (93, 100): 'A',
            (90, 92.99): 'A-',
            (87, 89.99): 'B+',
            (83, 86.99): 'B',
            (80, 82.99): 'B-',
            (77, 79.99): 'C+',
            (73, 76.99): 'C',
            (70, 72.99): 'C-',
            (67, 69.99): 'D+',
            (63, 66.99): 'D',
            (60, 62.99): 'D-',
            (0, 59.99): 'F'
        }

        # Title
        title = tk.Label(root, 
                        text="GPA Calculator", 
                        font=('Helvetica', 24), 
                        fg='white',
                        bg='#2E2E2E')
        title.pack(pady=20)

        # Total GPA Points Input
        gpa_label = tk.Label(root, 
                            text="Total GPA Points:", 
                            font=('Helvetica', 14), 
                            fg='white',
                            bg='#2E2E2E')
        gpa_label.pack()
        
        self.total_points_entry = tk.Entry(root, 
                                        font=('Helvetica', 14),
                                        bg='white',
                                        fg='black')
        self.total_points_entry.pack(pady=5)

        # Units Taken Input
        credits_label = tk.Label(root, 
                               text="Units Taken Toward GPA:", 
                               font=('Helvetica', 14), 
                               fg='white',
                               bg='#2E2E2E')
        credits_label.pack()
        
        self.completed_credits_entry = tk.Entry(root, 
                                              font=('Helvetica', 14),
                                              bg='white',
                                              fg='black')
        self.completed_credits_entry.pack(pady=5)

        # Current GPA Display
        self.current_gpa_label = tk.Label(root,
                                        text="Current GPA: N/A",
                                        font=('Helvetica', 14),
                                        fg='white',
                                        bg='#2E2E2E')
        self.current_gpa_label.pack(pady=10)

        # Courses Frame
        self.courses_frame = tk.Frame(root, bg='#2E2E2E')
        self.courses_frame.pack(pady=20)
        
        courses_label = tk.Label(self.courses_frame, 
                               text="Upcoming Courses", 
                               font=('Helvetica', 16), 
                               fg='white',
                               bg='#2E2E2E')
        courses_label.pack()

        self.courses = []
        self.add_course()

        # Add Course Button
        add_button = tk.Button(root, 
                             text="Add Another Course", 
                             command=self.add_course,
                             font=('Helvetica', 12),
                             bg='white',
                             fg='black')
        add_button.pack(pady=10)

        # Calculate Button
        calc_button = tk.Button(root, 
                              text="Calculate New GPA", 
                              command=self.calculate_gpa,
                              font=('Helvetica', 14),
                              bg='white',
                              fg='black')
        calc_button.pack(pady=20)

        # Result Label
        self.result_label = tk.Label(root, 
                                   text="Projected GPA: ", 
                                   font=('Helvetica', 16),
                                   fg='white',
                                   bg='#2E2E2E')
        self.result_label.pack(pady=20)

    def add_course(self):
        course_frame = tk.Frame(self.courses_frame, bg='#2E2E2E')
        course_frame.pack(pady=10)

        # Credits Entry
        tk.Label(course_frame, 
                text="Credits:", 
                fg='white',
                bg='#2E2E2E',
                font=('Helvetica', 12)).pack(side=tk.LEFT, padx=5)
        
        credits_entry = tk.Entry(course_frame, 
                               width=5,
                               bg='white',
                               fg='black')
        credits_entry.pack(side=tk.LEFT, padx=5)

        # Grade Entry
        tk.Label(course_frame, 
                text="Expected Grade:", 
                fg='white',
                bg='#2E2E2E',
                font=('Helvetica', 12)).pack(side=tk.LEFT, padx=5)
        
        grade_entry = tk.Entry(course_frame, 
                             width=5,
                             bg='white',
                             fg='black')
        grade_entry.pack(side=tk.LEFT, padx=5)

        # Remove Button
        remove_btn = tk.Button(course_frame, 
                             text="Remove", 
                             command=lambda: self.remove_course(course_frame),
                             bg='white',
                             fg='black')
        remove_btn.pack(side=tk.LEFT, padx=5)

        self.courses.append((credits_entry, grade_entry, course_frame))

    def remove_course(self, course_frame):
        self.courses = [(c, g, f) for c, g, f in self.courses if f != course_frame]
        course_frame.destroy()

    def convert_grade_to_points(self, grade_str):
        # Remove any whitespace and convert to uppercase
        grade_str = grade_str.strip().upper()
        
        try:
            # Try to convert to float first (for numerical inputs)
            grade_float = float(grade_str)
            
            # Check if it's a percentage (0-100)
            if 0 <= grade_float <= 100:
                # Convert percentage to letter grade
                for (min_grade, max_grade), letter in self.percentage_to_letter.items():
                    if min_grade <= grade_float <= max_grade:
                        return self.grade_to_points[letter]
            # Check if it's a 4.0 scale grade
            elif 0 <= grade_float <= 4:
                return grade_float
            else:
                raise ValueError("Grade must be between 0-100 or 0-4")
        except ValueError:
            # If not a number, try to convert letter grade
            if grade_str in self.grade_to_points:
                return self.grade_to_points[grade_str]
            else:
                raise ValueError(f"Invalid grade: {grade_str}")

    def calculate_gpa(self):
        try:
            total_points = float(self.total_points_entry.get())
            completed_credits = float(self.completed_credits_entry.get())
            
            # Calculate current GPA
            current_gpa = total_points / completed_credits
            self.current_gpa_label.config(text=f"Current GPA: {current_gpa:.4f}")
            
            expected_points_sum = 0
            total_new_credits = 0
            
            for credits_entry, grade_entry, _ in self.courses:
                try:
                    credits = float(credits_entry.get())
                    grade_points = self.convert_grade_to_points(grade_entry.get())
                    # Calculate points for this class (credits × grade points)
                    class_points = credits * grade_points
                    expected_points_sum += class_points
                    total_new_credits += credits
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
                    return

            # Calculate new GPA using total points
            new_total_points = total_points + expected_points_sum
            new_total_credits = completed_credits + total_new_credits
            new_gpa = new_total_points / new_total_credits
            
            self.result_label.config(text=f"Projected GPA: {new_gpa:.4f}")
            
        except ValueError:
            self.result_label.config(text="Please enter valid numbers in all fields")
            self.current_gpa_label.config(text="Current GPA: N/A")

def main():
    root = tk.Tk()
    app = GPACalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()