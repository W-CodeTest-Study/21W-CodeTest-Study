# spicy.py
# 프로그래머스 - 더 맵게

# 모든 음식의 스코빌 지수가 K를 넘겼는지 판별 (안넘겼으면 True)
def notK(scoville, K):
	if(scoville[0] < K):
			return True
	return False

def solution(scoville, K):
	answer = 0

	scoville.sort()
	
	while(notK(scoville, K)):
		answer+=1
		try:
			scoville.append(scoville.pop(0) + (scoville.pop(0)*2))
			scoville.sort()
		except:
			return -1
		
	return answer