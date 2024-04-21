from models.database import Database

class ProjectController:
    def __init__(self):
        self.db = Database()

    def get_projects(self):
        projects = self.db.get_projects()
        sorted_projects = self.db.merge_sort(list(projects))
        return sorted_projects

# Define other controllers as needed
