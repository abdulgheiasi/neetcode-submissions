class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {course: [] for course in range(numCourses)}

        for course, pre in prerequisites:
            prereq[course].append(pre)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False

            if prereq[course] == []:
                return True

            visiting.add(course)

            for pre in prereq[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)

            prereq[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True