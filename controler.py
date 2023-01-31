import view
import model

def start():
    cl = model.set_class(view.input_class())
    while True:
        if cl != 1:
            break
        else:
            cl = model.set_class(view.input_class1())
    model.set_subject(view.input_subject())
    fl = model.open_file()
    while True:
        if fl != 1:
            break
        else:
            model.set_subject(view.input_subject1())
            fl = model.open_file()
    student = ''
    while True:
        journal = model.get_journal()
        view.list_of_child(journal)
        student = view.who_answer()
        if student == 'exit':
            break
        st = model.find_student(student)
        print(st)
        while True:
            if st != 1:
                break
            else:
                student = view.who_answer1()
                st = model.find_student(student)
        mark = int(view.what_mark())
        print(mark)
        model.student_mark(student, mark)
    model.save_file()
        
    
        

