
import os
#import statistics
import pandas

def calculate_average_grade_from_csv(my_csv_filepath):
    df = pandas.read_csv(my_csv_filepath)

    
    #rows = df.to_dict("records")
    #grades = [r["final_grade"]for r in rows]
    #avg_grade = statistics.mean(grades)
    
    avg_grade = df["final_grade"].mean()

    return avg_grade


if __name__ == "__main__":
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")
    
    #gradebook_filepath = "/c/Users/sheridanbaker/Desktop/omniparser-starter-py/data/gradebook_2019.csv"

    #gradebook_filepath = "data/gradebook_2019.csv"


    print(gradebook_filepath)

    avg = calculate_average_grade_from_csv(gradebook_filepath)
    print(avg)