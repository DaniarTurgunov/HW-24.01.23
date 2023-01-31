import controler
journal = {}
path = ''
subject = ''

def set_class(class_path: str):
    global path
    path = 'practic 24.01.23\classes/' + class_path + '.txt'
    try:
        with open(path, 'r', encoding='UTF-8') as data:
            data.readlines()
    except IOError as data:
        return 1
   

def set_subject(our_subject: str):
    global subject
    subject = our_subject

def open_file():
    count = 0
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] == subject:
            for study in sub.split(';')[1].strip().split(', '):
                journal[study.split(':')[0]] = list(map(int, study.split(':')[1].split()))
        else:
            count += 1
    if count == len(file):
        return 1
            
def save_file():
    new_file = []
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] != subject:
            new_file.append(sub.strip())
    item = []
    for student, marks in journal.items():
        item.append(student + ':' + ' '.join(list(map(str, marks))))
    item = subject + ';' + ', '.join(item)
    new_file.append(item)
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(new_file))

def student_mark(student: str, mark: int):
    marks = journal.get(student)
    marks.append(mark)
    journal[student] = marks

            
def get_journal():
    return journal
    
def find_student(student:str):
    count = 0
    for key in journal:
        if student == key:
            return student
        else: 
            count +=1
    if count == len(journal):
        return 1 
