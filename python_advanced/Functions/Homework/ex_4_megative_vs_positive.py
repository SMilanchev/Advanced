nums_list = list(map(int, input().split(' ')))
negatives = [num for num in nums_list if num < 0]
positives = [num for num in nums_list if num > 0]
sum_positives = sum(positives)
sum_negatives = sum(negatives)
print(sum_negatives)
print(sum_positives)

if sum_positives > abs(sum_negatives):
    result = 'The positives are stronger than the negatives'
else:
    result = 'The negatives are stronger than the positives'
print(result)