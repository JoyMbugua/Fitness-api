"""exercises model"""

class ExerciseModel:

    exercises = []

    def __init__(self, name,period, description):
        self.exercise_id = len(ExerciseModel.exercises) + 1
        self.name = name
        self.period = period
        self.description = description

    def save(self):
        data = dict(
            exercise_id = self.exercise_id,
            name = self.name,
            period = self.period,
            description = self.description
        )
        ExerciseModel.exercises.append(data)
        return ExerciseModel.exercises

    def get_exercise_by_id(self, id):
        for exercise in ExerciseModel.exercises:
            if exercise['exercise_id'] == id:
                return exercise

    # for a keywords search/search endpoint? # return a boolean
    def get_exercise_by_name(self, name):
        for exercise in ExerciseModel.exercises:
            if exercise['name'] == name:
                return exercise

    def get_all_exercises(self):
        return ExerciseModel.exercises

    def search_exercise(self, name):
        search_results = []
        for exercise in ExerciseModel.exercises:
            if exercise['name'] == self.name:
                search_results.append(exercise)
                return search_results
            else:
                return {
                    "status": "Ok",
                    "search_results": len(search_results)
                }
