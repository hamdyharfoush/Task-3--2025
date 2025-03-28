using System;
using System.Collections.Generic;
using System.Linq;

class ExamScheduler
{
    class Course
    {
        public int Id;
        public int Level;
        public List<int> Conflicts;

        public Course(int id, int level)
        {
            Id = id;
            Level = level;
            Conflicts = new List<int>();
        }
    }

    static void Main()
    {
        List<Course> courses = new List<Course>
        {
            new Course(1, 1), new Course(2, 2), new Course(3, 3),
            new Course(4, 1), new Course(5, 2), new Course(6, 3)
        };

        Dictionary<int, List<int>> conflicts = new Dictionary<int, List<int>>
        {
            { 1, new List<int> { 2, 3 } },
            { 2, new List<int> { 1, 4 } },
            { 3, new List<int> { 1, 5 } },
            { 4, new List<int> { 2, 6 } },
            { 5, new List<int> { 3, 6 } },
            { 6, new List<int> { 4, 5 } }
        };

        int[][] patterns = new int[][]
        {
            new int[] { 1, 3, 2 },
            new int[] { 3, 1, 2 }
        };

        int[] bestSchedule = null;
        int minCost = int.MaxValue;

        foreach (var pattern in patterns)
        {
            var schedule = GenerateSchedule(courses, conflicts, pattern);
            int cost = CalculateCost(schedule, conflicts);
            
            if (cost < minCost)
            {
                minCost = cost;
                bestSchedule = schedule;
            }
        }

        Console.WriteLine("Optimal Exam Schedule:");
        for (int i = 0; i < bestSchedule.Length; i++)
        {
            Console.WriteLine("Day {i + 1}: Course {bestSchedule[i]}");
        }
    }

    static int[] GenerateSchedule(List<Course> courses, Dictionary<int, List<int>> conflicts, int[] pattern)
    {
        List<int> schedule = new List<int>();
        List<Course> remainingCourses = new List<Course>(courses);
        int index = 0;

        while (remainingCourses.Count > 0)
        {
            int currentLevel = pattern[index % pattern.Length];
            var availableCourses = remainingCourses.Where(c => c.Level == currentLevel).ToList();

            if (availableCourses.Count > 0)
            {
                var selectedCourse = availableCourses.First();
                schedule.Add(selectedCourse.Id);
                remainingCourses.Remove(selectedCourse);
            }

            index++;
        }

        return schedule.ToArray();
    }

    static int CalculateCost(int[] schedule, Dictionary<int, List<int>> conflicts)
    {
        int cost = 0;

        for (int i = 0; i < schedule.Length - 1; i++)
        {
            for (int j = i + 1; j < schedule.Length; j++)
            {
                if (conflicts.ContainsKey(schedule[i]) && conflicts[schedule[i]].Contains(schedule[j]))
                {
                    cost++;
                }
            }
        }

        return cost;
    }
}
