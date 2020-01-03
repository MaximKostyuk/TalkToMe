import time
import pickle
#Здесь должны храниться все данные о человеке. Нужно будет дополнить её.
personalData = {"Name":"Max","Age" : 21 }
#Прикол тоже можно доработать, а то как то не смешно.
print ("Вся собранная информация поступает в личное хранилище серверов США. Суперкомпьютеры на их базе обработают ваши личные данные и отправят их иллюминатам, чтобы те смогли отправить их внеземным цивилизациям. Спасибо за поддержку.")
#Входной опрос
print ("Привет, ты запустил программу Talk To Me.\nВскорее тебя обслужат.")
print ("Я готово тебя обслужить")
print ("Давай напишем твое имя, дабы я смогло называть тебя по имени.")
#Имя, возраст
writeName = input("Твое Имя: ")
personalData["Name"] = writeName
print ("Отлично. Теперь я хочу узнать твой возраст")
howOldIsYourSoul = int(input("How Old Is Your Soul: " ))
personalData["Age"] = howOldIsYourSoul
print ("Давай перепроверим все.")
print ("Твое имя %s, а твой возраст %s, верно?" % (personalData["Name"], personalData["Age"]))
#Если возраст < 18, то программа не должна тебя впустить. Но пока что, впринципе все равно сколько тебе лет. Многие ведь врут в интернете, да?
if personalData["Age"] < 18:
	print ("Прости, но ты, человек, слишком мал для этого.")
elif personalData["Age"] >= 18:
	print ("Не забудь, у тебя есть личный персональный дневник, можешь его вести когда хочешь.")
	print ("Приступаем...")
#Начало работы цикла
while True:
	print ("\nХочешь что то спросить у меня? Или, может, ты хочешь чтобы я что то спросило у тебя?")
	print ("Предложеные функции: 1.Хочу узнать информацию о моем персональном дневнике, 2.Хочу записать в дневник")
	order = int(input("Я хочу: "))
	if order == 1:
		personalNote = open('PersonalNote.txt')
		print("Имя файла: ", personalNote.name)
		print("Файл закрыт: ", personalNote.closed)
		print("В каком режиме файл открыт: ", personalNote.mode)
		personalNoteRead = personalNote.read()
		print ("В твоем дневнике записано следующее:")
		print (personalNoteRead)
		personalNote.close()
	if order == 2:
		personalNote = open('PersonalNote.txt', 'a+')
		print ("Записывай:")
		whatToWrite = input("")
		personalNote.write(whatToWrite)
		personalNoteRead = personalNote.read()
		print ("В твоем дневнике записано следующее:")
		print (personalNoteRead)
		personalNote.close()
		
#Конец
print ("Конец")
