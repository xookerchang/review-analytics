
data =[]
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完了, 總共有', len(data),'筆資料')


#--calculate the average lenght of each comment

sum_com = 0
for d in data:
	sum_com += len(d)
print('每個留言的平均程度為', sum_com/len(data))

#--adding filtering functon 
new = []
for c in data:
	if len(c) < 100:
		new.append(c)
print('一共有', len(c), '留言長度小於100')
print('------------------------------')
print(new[0])
print(new[1])
