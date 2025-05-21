#начни тут создавать приложение с умными заметками
import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout

'''Заметки в json'''
notes = {
    "Добро пожаловать!" : {
        "текст" : "Это самое лучшее приложение для заметок в мире!",
        "теги" : ["добро", "инструкция"]
    }
}

with open("meow.json", "w") as file:
    json.dump(notes, file)


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Умные заметки')
main_win.resize(900, 600)

list_notes = QListWidget()
list_namen = QLabel("Список заметок")

list_tags = QListWidget()
list_namet = QLabel("Список тегов")

btn_create = QPushButton("Создать заметку")
btn_delete = QPushButton("Удалить заметку")
btn_save = QPushButton("Сохранить заметку")

field_tag = QLineEdit()
field_tag.setPlaceholderText('Введите тег...')

big_field = QTextEdit()

btn_plus = QPushButton("Добавить к заметкам")
btn_minus = QPushButton("Открепить от заметки")
btn_search = QPushButton("Искать заметки по тегу")

layout_main = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(big_field)

col_2 = QVBoxLayout()
col_2.addWidget(list_namen)
col_2.addWidget(list_notes)

hol_3 = QHBoxLayout()
hol_3.addWidget(btn_create)
hol_3.addWidget(btn_delete)

hol_4 = QHBoxLayout()
hol_4.addWidget(btn_save)

col_2.addLayout(hol_3)
col_2.addLayout(hol_4)

col_2.addWidget(list_namet)
col_2.addWidget(list_tags)

col_2.addWidget(field_tag)

hol_5 = QHBoxLayout()
hol_5.addWidget(btn_plus)
hol_5.addWidget(btn_minus)

col_2.addLayout(hol_5)
col_2.addWidget(btn_search)

layout_main.addLayout(col_1)
layout_main.addLayout(col_2)
main_win.setLayout(layout_main)

def add_note():
    note_name, ok = QInputDialog.getText(main_win, "Добавить заметку", "Название заметки: ")
    if ok and note_name != "":
        notes[note_name] = {"текст" : "", "теги" : []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]["теги"])
        print(notes)

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        big_field.clear()
        list_notes.addItems(notes)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Заметка для удаления не выбрана!")

def save_notes():
    key = list_notes.selectedItems()[0].text()
    field_text = self.notetextEdit.toPlainText()
    notes[key]["текст"] = field_text
    with open('meow.json', 'w') as file:
        json.dump(notes, file, sort_keys=True)
    print(notes)

def show_notes():
    name = list_notes.selectedItems()[0].text()
    big_field.setText(notes[name]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[name]["теги"])

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open("meow.json", "w") as file:
            json.dump(notes, file, sort_keys=True)
    else:
        print('Заметка для добавления тега не выбрана!')

def del_tag():
    if list_tags.selectedItems():
        key = list_tags.selectedItems()[0].text()
        notes[list_notes.selectedItems()[0].text()]["теги"].remove(key)
        list_tags.clear()
        list_tags.addItems(notes[list_notes.selectedItems()[0].text()]["теги"])
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)

def search_tag():
    tag = field_tag.text()
    if btn_search.text() == "Искать заметки по тегу" and tag:
        notes_filtered = {} #Словарь с поиском тегов
        for note in notes:
            if tag in notes[note]["теги"]:
                notes_filtered[note]=notes[note]
        btn_search.setText("Сбросить поиск")
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
    elif btn_search.text() == "Сбросить поиск":
        field_tag.clear()
        list_tags.clear()
        list_notes.clear()
        list_notes.addItems(notes)
        btn_search.setText("Искать заметки по тегу")
    else:
        pass
    
#Подключение функций, обработка
list_notes.itemClicked.connect(show_notes)
btn_create.clicked.connect(add_note)
btn_delete.clicked.connect(del_note)
btn_plus.clicked.connect(add_tag)
btn_minus.clicked.connect(del_tag)
btn_search.clicked.connect(search_tag)
btn_save.clicked.connect(save_notes)

main_win.show()
with open("meow.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)
app.exec_()
