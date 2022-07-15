# 프로그래머스 - 네트워크
# network.py

network = []
visited = []

def recursive(p):
	result = []
	global network
	global visited

	if(visited[p]):
		return []
	else:
		visited[p] = 1

	# 빈 리스트는 for문 안들어가고 바로 빈리스트 반환
	for nw in network[p]: 
		result += ([nw] + recursive(nw))
	return result

def solution(n, computers):
	answer = 0
	start = 0

	global visited
	visited = [0] * n

	#컴퓨터별 연결정보 리스트 저장
	global network
	network = [[]] * n

	for idx, computer in enumerate(computers):
		network[idx] = [i for i, value in enumerate(computer) if idx != i and value==1]
		if computer.count(1) == 1: #다른 컴퓨터와 연결이 없는 컴퓨터일 경우
			visited[idx] = 1
			answer += 1
	
	while(visited.count(0)): # 모두 방문 했을 경우 종료
		result = recursive(start)
		if(result): # 방문 했던 노드가 아니였을 때 네트워크 수 추가
			answer += 1
		start += 1

	return answer