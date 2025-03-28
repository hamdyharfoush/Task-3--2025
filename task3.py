#Hamdy_harfoush
#Section:3

import networkx as nx
from collections import defaultdict

def create_conflict_graph(conflicts):
    G = nx.Graph()
    for sub_id, conflict_sub_id, num_of_intersection in conflicts:
        G.add_edge(sub_id, conflict_sub_id, weight=num_of_intersection)
    return G

def sort_courses_by_level(courses, pattern):
    level_order = {"First": 0, "Third": 1, "Second": 2} if pattern == 1 else {"Third": 0, "First": 1, "Second": 2}
    return sorted(courses, key=lambda x: level_order[x[1]])

def schedule_exams(conflicts, courses, pattern):
    G = create_conflict_graph(conflicts)
    sorted_courses = sort_courses_by_level(courses, pattern)
    schedule = defaultdict(list)
    
    used_days = {}
    
    for course, level in sorted_courses:
        assigned = False
        for day in schedule:
            if all(neighbor not in schedule[day] for neighbor in G.neighbors(course)):
                schedule[day].append(course)
                assigned = True
                break
        if not assigned:
            schedule[len(schedule) + 1].append(course)
    
    return schedule


conflicts = [("C1", "C2", 3), ("C2", "C3", 2), ("C3", "C4", 1), ("C1", "C4", 2)]
courses = [("C1", "First"), ("C2", "Second"), ("C3", "Third"), ("C4", "First")]
pattern = 1  


exam_schedule = schedule_exams(conflicts, courses, pattern)

# Output 
for day, exams in exam_schedule.items():
    print(f"Day {day}: {', '.join(exams)}")
