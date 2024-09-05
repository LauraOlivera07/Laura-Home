"""
Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s)
having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""
def finding_second_lowest(list):
    list_scores=[float(list[x][1]) for x in range(len(list))]
    lowest=min(list_scores)
    second_lowest=100

    for elem in list_scores:
        if elem<second_lowest and elem!=lowest:
            second_lowest=elem
    return second_lowest

def finding_names(list, n2):
    names_list=[]
    for elem in list:
        if elem[1]==n2:
            names_list.append(elem[0])
    names_list.sort()
    return names_list

try:
    N_STUDENTS= int(input())
    list=[]

    for x in range(N_STUDENTS):
        name = input()
        score = float(input())
        list+=[[name, score]]

    number=finding_second_lowest(list)
    names_list=finding_names(list, number)

    for elem in names_list:
        print(elem)

except ValueError:
    print('INTEGERS PLEASE')

