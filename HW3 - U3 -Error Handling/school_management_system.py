# ==========================================
# School Management System
# ==========================================

def main():
    # INPUT
    students = []
    
    print("=== SCHOOL MANAGEMENT SYSTEM ===")
    
    while True:
        print("\nSelect Mode:")
        print("1. Add Student")
        print("2. View Students")
        print("3. Calculate Averages")
        print("4. Exit")
        
        # INPUT
        mode = input("Enter mode (1-4): ")
        
        # PROCESS
        if mode == '1':
            # INPUT
            name = input("Enter student name: ")
            grade = float(input("Enter student grade: "))
            
            # PROCESS
            student_data = {"name": name, "grade": grade}
            students.append(student_data)
            
            # OUTPUT
            print(f"--> Student '{name}' added successfully!")
            
        elif mode == '2':
            # OUTPUT
            print("\n--- Student List ---")
            if not students:
                print("No students registered yet.")
            else:
                for idx, student in enumerate(students, start=1):
                    print(f"{idx}. {student['name']} - Grade: {student['grade']}")
                    
        elif mode == '3':
            # PROCESS
            if not students:
                # OUTPUT
                print("No data available to calculate average.")
            else:
                total_sum = sum(student['grade'] for student in students)
                average = total_sum / len(students)
                
                # OUTPUT
                print(f"--> Overall Average Grade: {average:.2f}")
                
        elif mode == '4':
            # OUTPUT
            print("Exiting system. Goodbye!")
            break
        else:
            # OUTPUT
            print("Invalid mode selected. Please try again.")

if __name__ == "__main__":
    main()
