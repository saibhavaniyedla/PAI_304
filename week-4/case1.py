class ProctorAssignmentCSP:
    def __init__(self, exams, proctors):
        self.exams = exams
        self.proctors = proctors
        self.assignment = {}
    # Check if two time intervals overlap
    def is_time_conflict(self, t1, t2):
        return max(t1[0], t2[0]) < min(t1[1], t2[1])
    # Check constraints
    def is_valid(self, exam, proctor):
        exam_time = self.exams[exam]["time"]
        exam_subject = self.exams[exam]["subject"]
        # Skill match
        if exam_subject not in self.proctors[proctor]["skills"]:
            return False
        # Availability check
        available = self.proctors[proctor]["availability"]
        if not (available[0] <= exam_time[0] and available[1] >= exam_time[1]):
            return False
        # Time conflict check
        for assigned_exam, assigned_proctor in self.assignment.items():
            if assigned_proctor == proctor:
                assigned_time = self.exams[assigned_exam]["time"]
                if self.is_time_conflict(exam_time, assigned_time):
                    return False
        return True
    def backtrack(self, index=0):
        if index == len(self.exams):
            return True

        exam = list(self.exams.keys())[index]

        for proctor in self.proctors:
            if self.is_valid(exam, proctor):
                self.assignment[exam] = proctor

                if self.backtrack(index + 1):
                    return True
                del self.assignment[exam]  # Backtrack
        return False
    def solve(self):
        if self.backtrack():
            return self.assignment
        return None
exams = {}
num_exams = int(input("Enter number of exams: "))

for i in range(num_exams):
    name = input(f"\nEnter name of exam {i+1}: ")
    subject = input("Enter subject: ")
    start = int(input("Enter start time (24hr format, e.g., 10): "))
    end = int(input("Enter end time (24hr format, e.g., 12): "))
    exams[name] = {"subject": subject, "time": (start, end)}

# Input Proctors
proctors = {}
num_proctors = int(input("\nEnter number of proctors: "))
for i in range(num_proctors):
    name = input(f"\nEnter name of proctor {i+1}: ")
    skills = input("Enter skills (comma separated): ").split(",")
    skills = [skill.strip() for skill in skills]
    start = int(input("Enter availability start time: "))
    end = int(input("Enter availability end time: "))
    proctors[name] = {"skills": skills, "availability": (start, end)}
csp = ProctorAssignmentCSP(exams, proctors)
solution = csp.solve()
print("\n==============================")

if solution:
    print("✅ Proctor Assignment Solution:\n")
    for exam, proctor in solution.items():
        print(f"{exam}  --->  {proctor}")
else:
    print("❌ No valid assignment found.")

print("==============================")
