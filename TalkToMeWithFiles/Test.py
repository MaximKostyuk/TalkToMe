my_file = open("Congratulations.txt")
print("Имя файла: ", my_file.name)
print("Файл закрыт: ", my_file.closed)
print("В каком режиме файл открыт: ", my_file.mode)
my_string = my_file.read()
print ("Было прочитано:")
print (my_string)
my_file.close()

"""
openCongratulations = open('Congratulations.txt', 'r')
readCongratulations = openCongratulations.read()
print ( readCongratulations)
openCongratulations.close()

Добавление в файл. Метод write()
Если вы хотите не перезаписать файл полностью (что делает метод write в случае открытия файла в режиме 'w'), а только добавить какой-либо текст, то файл следует открывать в режиме 'a' - appending. После чего использовать все тот же метод write.

Например:

?
1
2
3
4
5
6
7
8
# Удалит существующую информацию в some.txt и запишет "Hello".
my_file = open("some.txt", 'w')
my_file.write("Hello")
my_file.close()
# Оставит существующую информацию в some.txt и добавит "Hello".
my_file = open("some.txt", 'a')
my_file.write("Hello")
my_file.close()
"""
