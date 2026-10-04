# •	2.00 – 2.99 - "Fail"
# •	3.00 – 3.49 - "Poor"
# •	3.50 – 4.49 - "Good"
# •	4.50 – 5.49 - "Very Good"
# •	5.50 – 6.00 - "Excellent"

def grade (grade_data):

    if 2 <= grade_data <= 2.99:
        return "Fail"
    elif 3 <= grade_data <= 3.49:
        return "Poor"
    elif 3.50 <= grade_data <= 4.49:
        return "Good"
    elif 4.50 <= grade_data <= 5.49:
        return "Very Good"
    elif 5.50 <= grade_data <= 6:
        return "Excellent"


given_grade = float(input())

result = grade(given_grade)

print(result)



# build_in = list(dir(__builtins__))
#
# for item in build_in:
#     print(item)