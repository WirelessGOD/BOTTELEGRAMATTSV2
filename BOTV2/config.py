# -*- coding: utf-8 -*-
import openpyxl
TOKEN = '5143189222:AAE0QNN2QfA48fRubvkAhwcLR-8mCEr7Z74'
TOKEN58 = '5021433569:AAHHOcpdEjm0Fh-156bwx6lp6vxpTUzd85g' #БОТ ГРУППЫ 58
TOKEN59 = '5137928420:AAGLFYW4mlrKLMxOL35Kuexy8RocJWYfv7Y' #БОТ ГРУППЫ 59
TOKEN60 = '5151067116:AAEGJvO_yPbLDw8Y6r6Yhxfvm3I5Hkn6GPg' #БОТ ГРУППЫ 60
TOKEN61 = '5109458509:AAFyvOadzp3WgOnl4pc51UfuGnMJZbfgR1I' #БОТ ГРУППЫ 61
TOKEN62 = '5036839225:AAHW2I2eMNEhoOAiUp3a6X4287nvKBNQwe8' #БОТ ГРУППЫ 62














































xls = openpyxl.open("Расписания/PPKPC.xlsx", read_only=True)
sheet = xls.active

#ПОНЕДЕЛЬНИК 58 ГРУППА
oneparP58 = sheet[7][2].value
twoparP58 = sheet[8][2].value
threeparP58 = sheet[9][2].value
fourparP58 = sheet[10][2].value
fiveparP58 = sheet[11][2].value
sixparP58 = sheet[12][2].value
#ВТОРНИК 58 ГРУППА
oneparV58 = sheet[15][2].value
twoparV58 = sheet[16][2].value
threeparV58 = sheet[17][2].value
fourparV58 = sheet[18][2].value
fiveparV58 = sheet[19][2].value
sixparV58 = sheet[20][2].value
#СРЕДА 58 ГРУППА
oneparS58 = sheet[23][2].value
twoparS58 = sheet[24][2].value
threeparS58 = sheet[25][2].value
fourparS58 = sheet[26][2].value
fiveparS58 = sheet[27][2].value
sixparS58 = sheet[28][2].value
#ЧЕТВЕРГ 58 ГРУППА
onepar458 = sheet[31][2].value
twopar458 = sheet[32][2].value
threepar458 = sheet[33][2].value
fourpar458 = sheet[34][2].value
fivepar458 = sheet[35][2].value
sixpar458 = sheet[36][2].value
#ПЯТНИЦА 58 ГРУППА
oneparPI58 = sheet[39][2].value
twoparPI58 = sheet[40][2].value
threeparPI58 = sheet[41][2].value
fourparPI58 = sheet[42][2].value
fiveparPI58 = sheet[43][2].value
sixparPI58 = sheet[44][2].value
#СУББОТА 58 ГРУППА
oneparSU58 = sheet[47][2].value
twoparSU58 = sheet[48][2].value
threeparSU58 = sheet[49][2].value
fourparSU58 = sheet[50][2].value
fiveparSU58 = sheet[51][2].value
sixparSU58 = sheet[52][2].value

#КАБИНЕТЫ ПОНЕДЕЛЬНИК 58
kabP581 = sheet[7][4].value
kabP582 = sheet[8][4].value
kabP583 = sheet[9][4].value
kabP584 = sheet[10][4].value
kabP585 = sheet[11][4].value
kabP586 = sheet[12][4].value
#КАБИНЕТЫ ВТОРНИК 58
kabV581 = sheet[15][4].value
kabV582 = sheet[16][4].value
kabV583 = sheet[17][4].value
kabV584 = sheet[18][4].value
kabV585 = sheet[19][4].value
kabV586 = sheet[20][4].value
#КАБИНЕТЫ СРЕДА 58
kabS581 = sheet[23][4].value
kabS582 = sheet[24][4].value
kabS583 = sheet[25][4].value
kabS584 = sheet[26][4].value
kabS585 = sheet[27][4].value
kabS586 = sheet[28][4].value
#КАБИНЕТЫ ЧЕТВЕРГ 58
kab4581 = sheet[31][4].value
kab4582 = sheet[32][4].value
kab4583 = sheet[33][4].value
kab4584 = sheet[34][4].value
kab4585 = sheet[35][4].value
kab4586 = sheet[36][4].value
#КАБИНЕТЫ ПЯТНИЦА 58
kabPI581 = sheet[39][4].value
kabPI582 = sheet[40][4].value
kabPI583 = sheet[41][4].value
kabPI584 = sheet[42][4].value
kabPI585 = sheet[43][4].value
kabPI586 = sheet[44][4].value
#КАБИНЕТЫ СУББОТА 58
kabSU581 = sheet[47][4].value
kabSU582 = sheet[48][4].value
kabSU583 = sheet[49][4].value
kabSU584 = sheet[50][4].value
kabSU585 = sheet[51][4].value
kabSU586 = sheet[52][4].value

#ТРАНСФОРМАЦИЯ NONE В НЕТУ/НЕТ
if oneparP58 == None:
	oneparP58 = 'Нету'
if twoparP58 == None:
	twoparP58 = 'Нету'
if threeparP58 == None:
	threeparP58 = 'Нету'
if fourparP58 == None:
	fourparP58 = 'Нету'
if fiveparP58 == None:
	fiveparP58 = 'Нету'
if sixparP58 == None:
	sixparP58 = 'Нету'

if oneparV58 == None:
	oneparV58 = 'Нету'
if twoparV58 == None:
	twoparV58 = 'Нету'
if threeparV58 == None:
	threeparV58 = 'Нету'
if fourparV58 == None:
	fourparV58 = 'Нету'
if fiveparV58 == None:
	fiveparV58 = 'Нету'
if sixparV58 == None:
	sixparV58 = 'Нету'

if oneparS58 == None:
	oneparS58 = 'Нету'
if twoparS58 == None:
	twoparS58 = 'Нету'
if threeparS58 == None:
	threeparS58 = 'Нету'
if fourparS58 == None:
	fourparS58 = 'Нету'
if fiveparS58 == None:
	fiveparS58 = 'Нету'
if sixparS58 == None:
	sixparS58 = 'Нету'

if onepar458 == None:
	onepar458 = 'Нету'
if twopar458 == None:
	twopar458 = 'Нету'
if threepar458 == None:
	threepar458 = 'Нету'
if fourpar458 == None:
	fourpar458 = 'Нету'
if fivepar458 == None:
	fivepar458 = 'Нету'
if sixpar458 == None:
	sixpar458 = 'Нету'

if oneparPI58 == None:
	oneparPI58 = 'Нету'
if twoparPI58 == None:
	twoparPI58 = 'Нету'
if threeparPI58 == None:
	threeparPI58 = 'Нету'
if fourparPI58 == None:
	fourparPI58 = 'Нету'
if fiveparPI58 == None:
	fiveparPI58 = 'Нету'
if sixparPI58 == None:
	sixparPI58 = 'Нету'

if oneparSU58 == None:
	oneparSU58 = 'Нету'
if twoparSU58 == None:
	twoparSU58 = 'Нету'
if threeparSU58 == None:
	threeparSU58 = 'Нету'
if fourparSU58 == None:
	fourparSU58 = 'Нету'
if fiveparSU58 == None:
	fiveparSU58 = 'Нету'
if sixparSU58 == None:
	sixparSU58 = 'Нету'

if kabP581 == None:
	kabP581 = 'НЕТ'
if kabP582 == None:
	kabP582 = 'НЕТ'
if kabP583 == None:
	kabP583 = 'НЕТ'
if kabP584 == None:
	kabP584 = 'НЕТ'
if kabP585 == None:
	kabP585 = 'НЕТ'
if kabP586 == None:
	kabP586 = 'НЕТ'

if kabV581 == None:
	kabV581 = 'НЕТ'
if kabV582 == None:
	kabV582 = 'НЕТ'
if kabV583 == None:
	kabV583 = 'НЕТ'
if kabV584 == None:
	kabV584 = 'НЕТ'
if kabV585 == None:
	kabV585 = 'НЕТ'
if kabV586 == None:
	kabV586 = 'НЕТ'

if kabS581 == None:
	kabS581 = 'НЕТ'
if kabS582 == None:
	kabS582 = 'НЕТ'
if kabS583 == None:
	kabS583 = 'НЕТ'
if kabS584 == None:
	kabS584 = 'НЕТ'
if kabS585 == None:
	kabS585 = 'НЕТ'
if kabS586 == None:
	kabS586 = 'НЕТ'

if kab4581 == None:
	kab4581 = 'НЕТ'
if kab4582 == None:
	kab4582 = 'НЕТ'
if kab4583 == None:
	kab4583 = 'НЕТ'
if kab4584 == None:
	kab4584 = 'НЕТ'
if kab4585 == None:
	kab4585 = 'НЕТ'
if kab4586 == None:
	kab4586 = 'НЕТ'

if kabPI581 == None:
	kabPI581 = 'НЕТ'
if kabPI582 == None:
	kabPI582 = 'НЕТ'
if kabPI583 == None:
	kabPI583 = 'НЕТ'
if kabPI584 == None:
	kabPI584 = 'НЕТ'
if kabPI585 == None:
	kabPI585 = 'НЕТ'
if kabPI586 == None:
	kabPI586 = 'НЕТ'

if kabSU581 == None:
	kabSU581 = 'НЕТ'
if kabSU582 == None:
	kabSU582 = 'НЕТ'
if kabSU583 == None:
	kabSU583 = 'НЕТ'
if kabSU584 == None:
	kabSU584 = 'НЕТ'
if kabSU585 == None:
	kabSU585 = 'НЕТ'
if kabSU586 == None:
	kabSU586 = 'НЕТ'


#ПОНЕДЕЛЬНИК 59 ГРУППА
oneparP59 = sheet[7][5].value
twoparP59 = sheet[8][5].value
threeparP59 = sheet[9][5].value
fourparP59 = sheet[10][5].value
fiveparP59 = sheet[11][5].value
sixparP59 = sheet[12][5].value
#ВТОРНИК 59 ГРУППА
oneparV59 = sheet[15][5].value
twoparV59 = sheet[16][5].value
threeparV59 = sheet[17][5].value
fourparV59 = sheet[18][5].value
fiveparV59 = sheet[19][5].value
sixparV59 = sheet[20][5].value
#СРЕДА 59 ГРУППА
oneparS59 = sheet[23][5].value
twoparS59 = sheet[24][5].value
threeparS59 = sheet[25][5].value
fourparS59 = sheet[26][5].value
fiveparS59 = sheet[27][5].value
sixparS59 = sheet[28][5].value
#ЧЕТВЕРГ 59 ГРУППА
onepar459 = sheet[31][5].value
twopar459 = sheet[32][5].value
threepar459 = sheet[33][5].value
fourpar459 = sheet[34][5].value
fivepar459 = sheet[35][5].value
sixpar459 = sheet[36][5].value
#ПЯТНИЦА 59 ГРУППА
oneparPI59 = sheet[39][5].value
twoparPI59 = sheet[40][5].value
threeparPI59 = sheet[41][5].value
fourparPI59 = sheet[42][5].value
fiveparPI59 = sheet[43][5].value
sixparPI59 = sheet[44][5].value
#СУББОТА 59 ГРУППА
oneparSU59 = sheet[47][5].value
twoparSU59 = sheet[48][5].value
threeparSU59 = sheet[49][5].value
fourparSU59 = sheet[50][5].value
fiveparSU59 = sheet[51][5].value
sixparSU59 = sheet[52][5].value

#КАБИНЕТЫ ПОНЕДЕЛЬНИК 59
kabP591 = sheet[7][7].value
kabP592 = sheet[8][7].value
kabP593 = sheet[9][7].value
kabP594 = sheet[10][7].value
kabP595 = sheet[11][7].value
kabP596 = sheet[12][7].value
#КАБИНЕТЫ ВТОРНИК 59
kabV591 = sheet[15][7].value
kabV592 = sheet[16][7].value
kabV593 = sheet[17][7].value
kabV594 = sheet[18][7].value
kabV595 = sheet[19][7].value
kabV596 = sheet[20][7].value
#КАБИНЕТЫ СРЕДА 59
kabS591 = sheet[23][7].value
kabS592 = sheet[24][7].value
kabS593 = sheet[25][7].value
kabS594 = sheet[26][7].value
kabS595 = sheet[27][7].value
kabS596 = sheet[28][7].value
#КАБИНЕТЫ ЧЕТВЕРГ 59
kab4591 = sheet[31][7].value
kab4592 = sheet[32][7].value
kab4593 = sheet[33][7].value
kab4594 = sheet[34][7].value
kab4595 = sheet[35][7].value
kab4596 = sheet[36][7].value
#КАБИНЕТЫ ПЯТНИЦА 59
kabPI591 = sheet[39][7].value
kabPI592 = sheet[40][7].value
kabPI593 = sheet[41][7].value
kabPI594 = sheet[42][7].value
kabPI595 = sheet[43][7].value
kabPI596 = sheet[44][7].value
#КАБИНЕТЫ СУББОТА 59
kabSU591 = sheet[47][7].value
kabSU592 = sheet[48][7].value
kabSU593 = sheet[49][7].value
kabSU594 = sheet[50][7].value
kabSU595 = sheet[51][7].value
kabSU596 = sheet[52][7].value

#ТРАНСФОРМАЦИЯ NONE В НЕТУ/НЕТ
if oneparP59 == None:
	oneparP59 = 'Нету'
if twoparP59 == None:
	twoparP59 = 'Нету'
if threeparP59 == None:
	threeparP59 = 'Нету'
if fourparP59 == None:
	fourparP59 = 'Нету'
if fiveparP59 == None:
	fiveparP59 = 'Нету'
if sixparP59 == None:
	sixparP59 = 'Нету'

if oneparV59 == None:
	oneparV59 = 'Нету'
if twoparV59 == None:
	twoparV59 = 'Нету'
if threeparV59 == None:
	threeparV59 = 'Нету'
if fourparV59 == None:
	fourparV59 = 'Нету'
if fiveparV59 == None:
	fiveparV59 = 'Нету'
if sixparV59 == None:
	sixparV59 = 'Нету'

if oneparS59 == None:
	oneparS59 = 'Нету'
if twoparS59 == None:
	twoparS59 = 'Нету'
if threeparS59 == None:
	threeparS59 = 'Нету'
if fourparS59 == None:
	fourparS59 = 'Нету'
if fiveparS59 == None:
	fiveparS59 = 'Нету'
if sixparS59 == None:
	sixparS59 = 'Нету'

if onepar459 == None:
	onepar459 = 'Нету'
if twopar459 == None:
	twopar459 = 'Нету'
if threepar459 == None:
	threepar459 = 'Нету'
if fourpar459 == None:
	fourpar459 = 'Нету'
if fivepar459 == None:
	fivepar459 = 'Нету'
if sixpar459 == None:
	sixpar459 = 'Нету'

if oneparPI59 == None:
	oneparPI59 = 'Нету'
if twoparPI59 == None:
	twoparPI59 = 'Нету'
if threeparPI59 == None:
	threeparPI59 = 'Нету'
if fourparPI59 == None:
	fourparPI59 = 'Нету'
if fiveparPI59 == None:
	fiveparPI59 = 'Нету'
if sixparPI59 == None:
	sixparPI59 = 'Нету'

if oneparSU59 == None:
	oneparSU59 = 'Нету'
if twoparSU59 == None:
	twoparSU59 = 'Нету'
if threeparSU59 == None:
	threeparSU59 = 'Нету'
if fourparSU59 == None:
	fourparSU59 = 'Нету'
if fiveparSU59 == None:
	fiveparSU59 = 'Нету'
if sixparSU59 == None:
	sixparSU59 = 'Нету'

if kabP591 == None:
	kabP591 = 'НЕТ'
if kabP592 == None:
	kabP592 = 'НЕТ'
if kabP593 == None:
	kabP593 = 'НЕТ'
if kabP594 == None:
	kabP594 = 'НЕТ'
if kabP595 == None:
	kabP595 = 'НЕТ'
if kabP596 == None:
	kabP596 = 'НЕТ'

if kabV591 == None:
	kabV591 = 'НЕТ'
if kabV592 == None:
	kabV592 = 'НЕТ'
if kabV593 == None:
	kabV593 = 'НЕТ'
if kabV594 == None:
	kabV594 = 'НЕТ'
if kabV595 == None:
	kabV595 = 'НЕТ'
if kabV596 == None:
	kabV596 = 'НЕТ'

if kabS591 == None:
	kabS591 = 'НЕТ'
if kabS592 == None:
	kabS592 = 'НЕТ'
if kabS593 == None:
	kabS593 = 'НЕТ'
if kabS594 == None:
	kabS594 = 'НЕТ'
if kabS595 == None:
	kabS595 = 'НЕТ'
if kabS596 == None:
	kabS596 = 'НЕТ'

if kab4591 == None:
	kab4591 = 'НЕТ'
if kab4592 == None:
	kab4592 = 'НЕТ'
if kab4593 == None:
	kab4593 = 'НЕТ'
if kab4594 == None:
	kab4594 = 'НЕТ'
if kab4595 == None:
	kab4595 = 'НЕТ'
if kab4596 == None:
	kab4596 = 'НЕТ'

if kabPI591 == None:
	kabPI591 = 'НЕТ'
if kabPI592 == None:
	kabPI592 = 'НЕТ'
if kabPI593 == None:
	kabPI593 = 'НЕТ'
if kabPI594 == None:
	kabPI594 = 'НЕТ'
if kabPI595 == None:
	kabPI595 = 'НЕТ'
if kabPI596 == None:
	kabPI596 = 'НЕТ'

if kabSU591 == None:
	kabSU591 = 'НЕТ'
if kabSU592 == None:
	kabSU592 = 'НЕТ'
if kabSU593 == None:
	kabSU593 = 'НЕТ'
if kabSU594 == None:
	kabSU594 = 'НЕТ'
if kabSU595 == None:
	kabSU595 = 'НЕТ'
if kabSU596 == None:
	kabSU596 = 'НЕТ'



#ПОНЕДЕЛЬНИК 60 ГРУППА
oneparP60 = sheet[7][8].value
twoparP60 = sheet[8][8].value
threeparP60 = sheet[9][8].value
fourparP60 = sheet[10][8].value
fiveparP60 = sheet[1][8].value
sixparP60 = sheet[12][8].value
#ВТОРНИК 60 ГРУППА
oneparV60 = sheet[15][8].value
twoparV60 = sheet[16][8].value
threeparV60 = sheet[17][8].value
fourparV60 = sheet[18][8].value
fiveparV60 = sheet[19][8].value
sixparV60 = sheet[20][8].value
#СРЕДА 60 ГРУППА
oneparS60 = sheet[23][8].value
twoparS60 = sheet[24][8].value
threeparS60 = sheet[25][8].value
fourparS60 = sheet[26][8].value
fiveparS60 = sheet[27][8].value
sixparS60 = sheet[28][8].value
#ЧЕТВЕРГ 60 ГРУППА
onepar460 = sheet[31][8].value
twopar460 = sheet[32][8].value
threepar460 = sheet[33][8].value
fourpar460 = sheet[34][8].value
fivepar460 = sheet[35][8].value
sixpar460 = sheet[36][8].value
#ПЯТНИЦА 60 ГРУППА
oneparPI60 = sheet[39][8].value
twoparPI60 = sheet[40][8].value
threeparPI60 = sheet[41][8].value
fourparPI60 = sheet[42][8].value
fiveparPI60 = sheet[43][8].value
sixparPI60 = sheet[44][8].value
#СУББОТА 60 ГРУППА
oneparSU60 = sheet[47][8].value
twoparSU60 = sheet[48][8].value
threeparSU60 = sheet[49][8].value
fourparSU60 = sheet[50][8].value
fiveparSU60 = sheet[51][8].value
sixparSU60 = sheet[52][8].value

#КАБИНЕТЫ ПОНЕДЕЛЬНИК 60
kabP601 = sheet[7][10].value
kabP602 = sheet[8][10].value
kabP603 = sheet[9][10].value
kabP604 = sheet[10][10].value
kabP605 = sheet[11][10].value
kabP606 = sheet[12][10].value
#КАБИНЕТЫ ВТОРНИК 60
kabV601 = sheet[15][10].value
kabV602 = sheet[16][10].value
kabV603 = sheet[17][10].value
kabV604 = sheet[18][10].value
kabV605 = sheet[19][10].value
kabV606 = sheet[20][10].value
#КАБИНЕТЫ СРЕДА 60
kabS601 = sheet[23][10].value
kabS602 = sheet[24][10].value
kabS603 = sheet[25][10].value
kabS604 = sheet[26][10].value
kabS605 = sheet[27][10].value
kabS606 = sheet[28][10].value
#КАБИНЕТЫ ЧЕТВЕРГ 60
kab4601 = sheet[31][10].value
kab4602 = sheet[32][10].value
kab4603 = sheet[33][10].value
kab4604 = sheet[34][10].value
kab4605 = sheet[35][10].value
kab4606 = sheet[36][10].value
#КАБИНЕТЫ ПЯТНИЦА 60
kabPI601 = sheet[39][10].value
kabPI602 = sheet[40][10].value
kabPI603 = sheet[41][10].value
kabPI604 = sheet[42][10].value
kabPI605 = sheet[43][10].value
kabPI606 = sheet[44][10].value
#КАБИНЕТЫ СУББОТА 60
kabSU601 = sheet[47][10].value
kabSU602 = sheet[48][10].value
kabSU603 = sheet[49][10].value
kabSU604 = sheet[50][10].value
kabSU605 = sheet[51][10].value
kabSU606 = sheet[52][10].value

#ТРАНСФОРМАЦИЯ NONE В НЕТУ/НЕТ
if oneparP60 == None:
	oneparP60 = 'Нету'
if twoparP60 == None:
	twoparP60 = 'Нету'
if threeparP60 == None:
	threeparP60 = 'Нету'
if fourparP60 == None:
	fourparP60 = 'Нету'
if fiveparP60 == None:
	fiveparP60 = 'Нету'
if sixparP60 == None:
	sixparP60 = 'Нету'

if oneparV60 == None:
	oneparV60 = 'Нету'
if twoparV60 == None:
	twoparV60 = 'Нету'
if threeparV60 == None:
	threeparV60 = 'Нету'
if fourparV60 == None:
	fourparV60 = 'Нету'
if fiveparV60 == None:
	fiveparV60 = 'Нету'
if sixparV60 == None:
	sixparV60 = 'Нету'

if oneparS60 == None:
	oneparS60 = 'Нету'
if twoparS60 == None:
	twoparS60 = 'Нету'
if threeparS60 == None:
	threeparS60 = 'Нету'
if fourparS60 == None:
	fourparS60 = 'Нету'
if fiveparS60 == None:
	fiveparS60 = 'Нету'
if sixparS60 == None:
	sixparS60 = 'Нету'

if onepar460 == None:
	onepar460 = 'Нету'
if twopar460 == None:
	twopar460 = 'Нету'
if threepar460 == None:
	threepar460 = 'Нету'
if fourpar460 == None:
	fourpar460 = 'Нету'
if fivepar460 == None:
	fivepar460 = 'Нету'
if sixpar460 == None:
	sixpar460 = 'Нету'

if oneparPI60 == None:
	oneparPI60 = 'Нету'
if twoparPI60 == None:
	twoparPI60 = 'Нету'
if threeparPI60 == None:
	threeparPI60 = 'Нету'
if fourparPI60 == None:
	fourparPI60 = 'Нету'
if fiveparPI60 == None:
	fiveparPI60 = 'Нету'
if sixparPI60 == None:
	sixparPI60 = 'Нету'

if oneparSU60 == None:
	oneparSU60 = 'Нету'
if twoparSU60 == None:
	twoparSU60 = 'Нету'
if threeparSU60 == None:
	threeparSU60 = 'Нету'
if fourparSU60 == None:
	fourparSU60 = 'Нету'
if fiveparSU60 == None:
	fiveparSU60 = 'Нету'
if sixparSU60 == None:
	sixparSU60 = 'Нету'

if kabP601 == None:
	kabP601 = 'НЕТ'
if kabP602 == None:
	kabP602 = 'НЕТ'
if kabP603 == None:
	kabP603 = 'НЕТ'
if kabP604 == None:
	kabP604 = 'НЕТ'
if kabP605 == None:
	kabP605 = 'НЕТ'
if kabP606 == None:
	kabP606 = 'НЕТ'

if kabV601 == None:
	kabV601 = 'НЕТ'
if kabV602 == None:
	kabV602 = 'НЕТ'
if kabV603 == None:
	kabV603 = 'НЕТ'
if kabV604 == None:
	kabV604 = 'НЕТ'
if kabV605 == None:
	kabV605 = 'НЕТ'
if kabV606 == None:
	kabV606 = 'НЕТ'

if kabS601 == None:
	kabS601 = 'НЕТ'
if kabS602 == None:
	kabS602 = 'НЕТ'
if kabS603 == None:
	kabS603 = 'НЕТ'
if kabS604 == None:
	kabS604 = 'НЕТ'
if kabS605 == None:
	kabS605 = 'НЕТ'
if kabS606 == None:
	kabS606 = 'НЕТ'

if kab4601 == None:
	kab4601 = 'НЕТ'
if kab4602 == None:
	kab4602 = 'НЕТ'
if kab4603 == None:
	kab4603 = 'НЕТ'
if kab4604 == None:
	kab4604 = 'НЕТ'
if kab4605 == None:
	kab4605 = 'НЕТ'
if kab4606 == None:
	kab4606 = 'НЕТ'

if kabPI601 == None:
	kabPI601 = 'НЕТ'
if kabPI602 == None:
	kabPI602 = 'НЕТ'
if kabPI603 == None:
	kabPI603 = 'НЕТ'
if kabPI604 == None:
	kabPI604 = 'НЕТ'
if kabPI605 == None:
	kabPI605 = 'НЕТ'
if kabPI606 == None:
	kabPI606 = 'НЕТ'

if kabSU601 == None:
	kabSU601 = 'НЕТ'
if kabSU602 == None:
	kabSU602 = 'НЕТ'
if kabSU603 == None:
	kabSU603 = 'НЕТ'
if kabSU604 == None:
	kabSU604 = 'НЕТ'
if kabSU605 == None:
	kabSU605 = 'НЕТ'
if kabSU606 == None:
	kabSU606 = 'НЕТ'




























	#62 ГРУППА
	#ПОНЕДЕЛЬНИК 62 ГРУППА
oneparP62 = sheet[7][15].value
twoparP62 = sheet[8][15].value
threeparP62 = sheet[9][15].value
fourparP62 = sheet[10][15].value
fiveparP62 = sheet[11][15].value
sixparP62 = sheet[12][15].value
#ВТОРНИК 62 ГРУППА
oneparV62 = sheet[15][15].value
twoparV62 = sheet[16][15].value
threeparV62 = sheet[17][15].value
fourparV62 = sheet[18][15].value
fiveparV62 = sheet[19][15].value
sixparV62 = sheet[20][15].value
#СРЕДА 62 ГРУППА
oneparS62 = sheet[23][15].value
twoparS62 = sheet[24][15].value
threeparS62 = sheet[25][15].value
fourparS62 = sheet[26][15].value
fiveparS62 = sheet[27][15].value
sixparS62 = sheet[28][15].value
#ЧЕТВЕРГ 62 ГРУППА
onepar462 = sheet[31][15].value
twopar462 = sheet[32][15].value
threepar462 = sheet[33][15].value
fourpar462 = sheet[34][15].value
fivepar462 = sheet[35][15].value
sixpar462 = sheet[36][15].value
#ПЯТНИЦА 62 ГРУППА
oneparPI62 = sheet[39][15].value
twoparPI62 = sheet[40][15].value
threeparPI62 = sheet[41][15].value
fourparPI62 = sheet[42][15].value
fiveparPI62 = sheet[43][15].value
sixparPI62 = sheet[44][15].value
#СУББОТА 62 ГРУППА
oneparSU62 = sheet[47][15].value
twoparSU62 = sheet[48][15].value
threeparSU62 = sheet[49][15].value
fourparSU62 = sheet[50][15].value
fiveparSU62 = sheet[51][15].value
sixparSU62 = sheet[52][15].value
#КАБИНЕТЫ ПОНЕДЕЛЬНИК 62
kabP621 = sheet[7][17].value
kabP622 = sheet[8][17].value
kabP623 = sheet[9][17].value
kabP624 = sheet[10][17].value
kabP625 = sheet[15][17].value
kabP626 = sheet[12][17].value
#КАБИНЕТЫ ВТОРНИК 62
kabV621 = sheet[15][17].value
kabV622 = sheet[16][17].value
kabV623 = sheet[17][17].value
kabV624 = sheet[18][17].value
kabV625 = sheet[19][17].value
kabV626 = sheet[20][17].value
#КАБИНЕТЫ СРЕДА 62
kabS621 = sheet[23][17].value
kabS622 = sheet[24][17].value
kabS623 = sheet[25][17].value
kabS624 = sheet[26][17].value
kabS625 = sheet[27][17].value
kabS626 = sheet[28][17].value
#КАБИНЕТЫ ЧЕТВЕРГ 62
kab4621 = sheet[31][17].value
kab4622 = sheet[32][17].value
kab4623 = sheet[33][17].value
kab4624 = sheet[34][17].value
kab4625 = sheet[35][17].value
kab4626 = sheet[36][17].value
#КАБИНЕТЫ ПЯТНИЦА 62
kabPI621 = sheet[39][17].value
kabPI622 = sheet[40][17].value
kabPI623 = sheet[41][17].value
kabPI624 = sheet[42][17].value
kabPI625 = sheet[43][17].value
kabPI626 = sheet[44][17].value
#КАБИНЕТЫ СУББОТА 62
kabSU621 = sheet[47][17].value
kabSU622 = sheet[48][17].value
kabSU623 = sheet[49][17].value
kabSU624 = sheet[50][17].value
kabSU625 = sheet[51][17].value
kabSU626 = sheet[52][17].value


#ТРАНСФОРМАЦИЯ NONE В НЕТУ/НЕТ
if oneparP62 == None:
	oneparP62 = 'Нету'
if twoparP62 == None:
	twoparP62 = 'Нету'
if threeparP62 == None:
	threeparP62 = 'Нету'
if fourparP62 == None:
	fourparP62 = 'Нету'
if fiveparP62 == None:
	fiveparP62 = 'Нету'
if sixparP62 == None:
	sixparP62 = 'Нету'

if oneparV62 == None:
	oneparV62 = 'Нету'
if twoparV62 == None:
	twoparV62 = 'Нету'
if threeparV62 == None:
	threeparV62 = 'Нету'
if fourparV62 == None:
	fourparV62 = 'Нету'
if fiveparV62 == None:
	fiveparV62 = 'Нету'
if sixparV62 == None:
	sixparV62 = 'Нету'

if oneparS62 == None:
	oneparS62 = 'Нету'
if twoparS62 == None:
	twoparS62 = 'Нету'
if threeparS62 == None:
	threeparS62 = 'Нету'
if fourparS62 == None:
	fourparS62 = 'Нету'
if fiveparS62 == None:
	fiveparS62 = 'Нету'
if sixparS62 == None:
	sixparS62 = 'Нету'

if onepar462 == None:
	onepar462 = 'Нету'
if twopar462 == None:
	twopar462 = 'Нету'
if threepar462 == None:
	threepar462 = 'Нету'
if fourpar462 == None:
	fourpar462 = 'Нету'
if fivepar462 == None:
	fivepar462 = 'Нету'
if sixpar462 == None:
	sixpar462 = 'Нету'

if oneparPI62 == None:
	oneparPI62 = 'Нету'
if twoparPI62 == None:
	twoparPI62 = 'Нету'
if threeparPI62 == None:
	threeparPI62 = 'Нету'
if fourparPI62 == None:
	fourparPI62 = 'Нету'
if fiveparPI62 == None:
	fiveparPI62 = 'Нету'
if sixparPI62 == None:
	sixparPI62 = 'Нету'

if oneparSU62 == None:
	oneparSU62 = 'Нету'
if twoparSU62 == None:
	twoparSU62 = 'Нету'
if threeparSU62 == None:
	threeparSU62 = 'Нету'
if fourparSU62 == None:
	fourparSU62 = 'Нету'
if fiveparSU62 == None:
	fiveparSU62 = 'Нету'
if sixparSU62 == None:
	sixparSU62 = 'Нету'

if kabP621 == None:
	kabP621 = 'НЕТ'
if kabP622 == None:
	kabP622 = 'НЕТ'
if kabP623 == None:
	kabP623 = 'НЕТ'
if kabP624 == None:
	kabP624 = 'НЕТ'
if kabP625 == None:
	kabP625 = 'НЕТ'
if kabP626 == None:
	kabP626 = 'НЕТ'

if kabV621 == None:
	kabV621 = 'НЕТ'
if kabV622 == None:
	kabV622 = 'НЕТ'
if kabV623 == None:
	kabV623 = 'НЕТ'
if kabV624 == None:
	kabV624 = 'НЕТ'
if kabV625 == None:
	kabV625 = 'НЕТ'
if kabV626 == None:
	kabV626 = 'НЕТ'

if kabS621 == None:
	kabS621 = 'НЕТ'
if kabS622 == None:
	kabS622 = 'НЕТ'
if kabS623 == None:
	kabS623 = 'НЕТ'
if kabS624 == None:
	kabS624 = 'НЕТ'
if kabS625 == None:
	kabS625 = 'НЕТ'
if kabS626 == None:
	kabS626 = 'НЕТ'

if kab4621 == None:
	kab4621 = 'НЕТ'
if kab4622 == None:
	kab4622 = 'НЕТ'
if kab4623 == None:
	kab4623 = 'НЕТ'
if kab4624 == None:
	kab4624 = 'НЕТ'
if kab4625 == None:
	kab4625 = 'НЕТ'
if kab4626 == None:
	kab4626 = 'НЕТ'

if kabPI621 == None:
	kabPI621 = 'НЕТ'
if kabPI622 == None:
	kabPI622 = 'НЕТ'
if kabPI623 == None:
	kabPI623 = 'НЕТ'
if kabPI624 == None:
	kabPI624 = 'НЕТ'
if kabPI625 == None:
	kabPI625 = 'НЕТ'
if kabPI626 == None:
	kabPI626 = 'НЕТ'

if kabSU621 == None:
	kabSU621 = 'НЕТ'
if kabSU622 == None:
	kabSU622 = 'НЕТ'
if kabSU623 == None:
	kabSU623 = 'НЕТ'
if kabSU624 == None:
	kabSU624 = 'НЕТ'
if kabSU625 == None:
	kabSU625 = 'НЕТ'
if kabSU626 == None:
	kabSU626 = 'НЕТ'









