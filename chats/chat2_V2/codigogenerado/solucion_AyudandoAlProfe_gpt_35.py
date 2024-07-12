def round_grade(grade):
    if grade < 38:
        return grade
    
    next_multiple_of_5 = ((grade // 5) + 1) * 5
    
    if next_multiple_of_5 - grade < 3:
        return next_multiple_of_5
    else:
        return grade

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    grades = list(map(int, data[1:N+1]))
    
    rounded_grades = [round_grade(grade) for grade in grades]
    
    for grade in rounded_grades:
        print(grade)

if __name__ == "__main__":
    main()
