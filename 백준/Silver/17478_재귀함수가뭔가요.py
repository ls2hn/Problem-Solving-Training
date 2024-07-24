# 나의 제출 코드

a = int(input())
count = 0

def recur(a, count):
    answer1 = [
               '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
              '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.',
              '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
    ]
    answer2 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
    indents = "____" * count

    
    print(indents+'"재귀함수가 뭔가요?"')
    
    if a == 0:
        print(indents + answer2)

    else: 
        for item in answer1:
            print(indents + item)

    a -= 1
    count += 1
    if a>=0:
        recur(a, count)

    print(indents + "라고 답변하였지.")


print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
recur(a, count)



## 더 정리된 코드
# a = int(input())
# count = 0

# def recur(k, count):
#     answer1 = [
#         '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
#         '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.',
#         '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
#     ]
#     answer2 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
#     indents = "____" * count

#     print(indents + '"재귀함수가 뭔가요?"')

#     if k == 0:
#         print(indents + answer2)
#     else:
#         for item in answer1:
#             print(indents + item)
#         recur(k - 1, count + 1)         # !
    
#     print(indents + "라고 답변하였지.")


# print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# recur(a, count)
