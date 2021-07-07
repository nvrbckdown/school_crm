

def get_salary(school, course):
    salary = 0
    for s in school:
        salary = salary + s.status.rank_number
    for c in course:
        salary = salary + (c.cost * 0.3)
    return salary