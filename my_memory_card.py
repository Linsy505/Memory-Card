from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QPushButton, QButtonGroup)
from random import*

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question("На какой территории было создано Древнерусское государство?","Современная Украина","Москва","Беларусь","Питерград"))
question_list.append(Question("Когда Русь приняла христианство?","988","948","895","970"))
question_list.append(Question("Когда произошла Куликовская битва?","1380","1397","1345","1267"))
question_list.append(Question("Кто победил в Куликовской битве?","Дмитрий Донской","Сталин","Ленин","Хрущёв"))
question_list.append(Question("От какого государства попала в зависимость Русь в ХIII веке?","Золотая орда","Великое княжество Литовское","Германия","Норвегия"))
question_list.append(Question("Какое имя в истории получил царь Иван IV?","Грозный","Сильный","Короткий","Святой"))
question_list.append(Question("Когда началась Великая Отечественная война?","1941","1945","1879","1989"))
question_list.append(Question("Когда Советский Союз распался?","1991","1948","1879","1889"))
question_list.append(Question("Сколько лет правил Ленин СССР?","2 года","4 года","5 лет","1 год"))
question_list.append(Question("В каком году сложился СССР?","1922","1945","1899","1934"))




app = QApplication([])
main_win = QWidget()
main_win.resize(400,200)
main_win.setWindowTitle('Memory Card')

btn_OK = QPushButton("Ответить")
question = QLabel("Какой национальности не существует?")

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результат теста")
lb_result = QLabel("Прав ты или нет?")
lb_correct = QLabel("Ответ будет тут")
layout_ans4 = QVBoxLayout()
layout_ans4.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_ans4.addWidget(lb_correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_ans4)





layout_line = QVBoxLayout()
layout_line.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line.addWidget(RadioGroupBox)
layout_line.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line.addWidget(btn_OK, stretch=2)
main_win.setLayout(layout_line)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Продолжить")

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask (q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    lb_result.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print("Статистика\n Всего вопросов -", main_win.total, "\nКоличество правильных ответов - ", main_win.score)
        print("Рейтинг: ", main_win.score/main_win.total*100,"%")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print("Рейтинг: ", main_win.score/main_win.total*100,"%")


def next_question():
    main_win.total +=1
    print("Статистика\n Всего вопросов -", main_win.total, "\nКоличество правильных ответов - ", main_win.score)
    cur_question = randint(0,len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)



def click_OK():
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()

main_win.total = 0
main_win.score = 0
btn_OK.clicked.connect(click_OK)
next_question()



main_win.show()
app.exec_()