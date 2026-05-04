import matplotlib.pyplot as plt
students = ['sanjay', 'suresh', 'ramesh', 'mahesh', 'rajesh', 'vinod', 'tungtungsahur', 'srijoy']
marks = [91, 80, 70, 60, 50, 40, 90, 1]
mark_perc = []
for x in marks:
    res = (x / 100) * 100
    mark_perc.append(res)

print(mark_perc)
def mark_line_chart():
    plt.plot(students, mark_perc)
    plt.title('Marks of Students')
    plt.xlabel('Students')
    plt.ylabel('Marks Percentage')
    plt.show()

mark_line_chart()

def percentage_bar_chart():
    plt.bar(students, mark_perc)
    plt.title('Marks of Students')
    plt.xlabel('Students')
    plt.ylabel('Marks Percentage')
    plt.show()

percentage_bar_chart()