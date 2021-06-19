#reviews-analytics

data = []
count = 0
#count1 = 0
#strlen = 0
#c = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 ==0:
			print(len(data))

print('檔案讀取玩了,總共有', len(data), '筆資料')

			#data = []  (selfmade)
			#with open('reviews.txt', 'r') as f:
			#	for line in f:
			#		count1 += 1
			#		data.append(line)
			#		c = len(data[count1 - 1])
			#		strlen = strlen + c
			#l = len(data)
								
			#print('每筆留言平均長度是', strlen / l, '字')
sum_len = 0
for d in data:
	sum_len += len(d)
print('留言平均長度為', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆資料留言小於100')