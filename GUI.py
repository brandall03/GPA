import os
os.environ['TK_SILENCE_DEPRECATION'] = "1"
import tkinter as tk

class GPACalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("GPA Calculator")
        self.root.geometry("600x700")
        self.root.configure(bg='#2E2E2E')

        # Title
        title = tk.Label(root, 
                        text="GPA Calculator", 
                        font=('Helvetica', 24), 
                        fg='white',
                        bg='#2E2E2E')
        title.pack(pady=20)

        # Current GPA Input
        gpa_label = tk.Label(root, 
                            text="Current GPA:", 
                            font=('Helvetica', 14), 
                            fg='white',
                            bg='#2E2E2E')
        gpa_label.pack()
        
        self.current_gpa_entry = tk.Entry(root, 
                                        font=('Helvetica', 14),
                                        bg='white',
                                        fg='black')
        self.current_gpa_entry.pack(pady=5)

        # Credit Hours Input
        credits_label = tk.Label(root, 
                               text="Completed Credit Hours:", 
                               font=('Helvetica', 14), 
                               fg='white',
                               bg='#2E2E2E')
        credits_label.pack()
        
        self.completed_credits_entry = tk.Entry(root, 
                                              font=('Helvetica', 14),
                                              bg='white',
                                              fg='black')
        self.completed_credits_entry.pack(pady=5)

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

    def calculate_gpa(self):
        try:
            current_gpa = float(self.current_gpa_entry.get())
            completed_credits = float(self.completed_credits_entry.get())
            
            expected_points_sum = 0
            total_new_credits = 0
            
            for credits_entry, grade_entry, _ in self.courses:
                credits = float(credits_entry.get())
                grade_points = float(grade_entry.get())
                expected_points_sum += credits * grade_points
                total_new_credits += credits

            numerator = (current_gpa * completed_credits) + expected_points_sum
            denominator = completed_credits + total_new_credits
            new_gpa = numerator / denominator
            
            self.result_label.config(text=f"Projected GPA: {new_gpa:.2f}")
            
        except ValueError:
            self.result_label.config(text="Please enter valid numbers in all fields")

def main():
    root = tk.Tk()
    app = GPACalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()