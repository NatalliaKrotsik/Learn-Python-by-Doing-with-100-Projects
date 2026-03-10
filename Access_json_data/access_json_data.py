import requests

URL = "https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json"


def get_correct_answer(question_id):

    if not isinstance(question_id, int):
        return None

    response = requests.get(URL)
    quiz_data = response.json()

    for quiz in quiz_data["quizzes"]:
        for question in quiz["questions"]:
            if question["id"] == question_id:
                for choice, is_correct in question["choices"].items():
                    if is_correct:
                        return choice

    return None


if __name__ == "__main__":
    question_id = int(input("Enter question ID: "))
    answer = get_correct_answer(question_id)
    print(answer)