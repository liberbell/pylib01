import bisect

values = [5, 7, 13, 20, 25, 31, 36, 43, 47, 49, 50, 75]

print(bisect.bisect(values, 25))
print(bisect.bisect_right(values, 25))
print(bisect.bisect_left(values, 25))

breakpoint = [60, 70, 80, 90]
gradeLetters = 'FDCBA'
scores = [81, 68, 53, 91, 90, 82, 76, 71, 84]

def calsGrade(score):
    i = 0
    return gradeLetters[i]

results = [calsGrade(score) for score in scores]
