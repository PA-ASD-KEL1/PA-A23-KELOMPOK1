from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['mydatabase']

    def get_projects(self):
        return self.db.projects.find()

    def get_freelancers(self):
        return self.db.freelancers.find()

    # Methods to fetch other data (companies, contracts, etc.)

    # Method to perform sorting (Merge Sort)
    def merge_sort(self, data):
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i]['field'] < right_half[j]['field']:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1
