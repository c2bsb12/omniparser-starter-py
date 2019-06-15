
import os
import json
import statistics
import pandas

def calculate_average_grade_from_csv(my_csv_filepath):
    df = pandas.read_csv(my_csv_filepath)

def calculate_average_grade_from_json(x):

    with open(x,"r") as f:
        #print(type(f))
        file_contents = f.read()
        #print(type(file_contents))

    gradebook = json.loads(file_contents)
    #print(gradebook)
    #print(type(gradebook))

    students = gradebook["students"]
    grades = [s["finalGrade"] for s in students]
    avg_grade = statistics.mean(grades)
    return avg_grade

    
    #rows = df.to_dict("records")
    #grades = [r["final_grade"]for r in rows]
    #avg_grade = statistics.mean(grades)
    
    avg_grade = df["final_grade"].mean()

    return avg_grade


if __name__ == "__main__":
    #print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")
    #gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")
    #gradebook_filepath = "/c/Users/sheridanbaker/Desktop/omniparser-starter-py/data/gradebook_2019.csv"
    #gradebook_filepath = "data/gradebook_2019.csv"
    #print(gradebook_filepath)
    #avg = calculate_average_grade_from_csv(gradebook_filepath)
    #print(avg)

    print("PARSING SOME JSON GRADEBOOK FILES HERE...")
    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2018.json")
    print(gradebook_filepath)
    print(os.path.isfile(gradebook_filepath))
    avg = calculate_average_grade_from_json(gradebook_filepath)
    print(avg)


