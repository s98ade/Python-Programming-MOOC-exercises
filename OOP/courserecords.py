class Course:
    def __init__(self, name, grade, credits):
        self.name = name
        self.grade = grade
        self.credits = credits


    def update_grade(self, new_grade):
        if new_grade > self.grade:
            self.grade = new_grade


class Data:
    def __init__(self):
        self.courses = {}


    def add_course(self, name, grade, credits):
        if name in self.courses:
            course = self.courses[name]
            if grade > course.grade:
                course.update_grade(grade)
        else:
            self.courses[name] = Course(name, grade, credits)


    def get_course(self, name):
        if name in self.courses:
            course = self.courses[name]
            return f"{course.name} ({course.credits} cr) grade {course.grade}"
        else:
            return "no entry for this course"


    def calculate_statistics(self):
        if not self.courses:
            return "No courses completed."

        total_courses = len(self.courses)
        total_credits = sum(course.credits for course in self.courses.values())
        weighted_grades = sum(course.grade * course.credits for course in self.courses.values())
        mean_grade = weighted_grades / total_credits if total_credits > 0 else 0

        grade_dist = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
        for course in self.courses.values():
            grade_dist[course.grade] += 1

        stats_output = f"{total_courses} completed courses, a total of {total_credits} credits\n"
        stats_output += f"mean {mean_grade:.1f}\n"
        stats_output += "grade distribution\n"
        for grade, count in sorted(grade_dist.items(), reverse=True):
            stats_output += f"{grade}: {'x' * count}\n"

        return stats_output.strip()


class Application:
    def __init__(self):
        self.data = Data()


    def run(self):
        self.display_menu()
        while True:
            command = input("command: ")
            if command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.show_statistics()
            elif command == "0":
                break
            else:
                print("Unknown command. Please try again.")


    def display_menu(self):
        print("\n1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")


    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.data.add_course(name, grade, credits)


    def get_course_data(self):
        name = input("course: ")
        print(self.data.get_course(name))


    def show_statistics(self):
        print(self.data.calculate_statistics())


app = Application()
app.run()