#read

def read_file(filename):
	data = []
	count = 0
	with open(filename, 'r', encoding = 'UTF-8-sig') as f:
		for line in f:
			data.append(line)
			count += 1
			# if count % 100000 == 0:
			# 	print(len(data))
		print('檔案讀取完了,總共有', len(data), '筆資料')
		return data



data = read_file('reviews.txt')

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1


for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])


while True:
	userinput = input("請輸入想要查找的字，按q離開: ")
	if userinput == 'q':
		break
	elif userinput in wc:
		print(userinput, '共出現過', wc[userinput], '次' )
	else:
		print('你查找的字不再字典裡')

print('感謝使用查詢功能')


