# disk.py

def solution(jobs):
	answer = 0 # 평균 작업 시간 저장
	current = 0 # 현재 몇ms가 흐른 상태인지
	finish = [] # 종료한 job의 인덱스 저장

	jobs.sort()

	while(len(finish) != len(jobs)): # 모든 job을 clear했으면 종료
		for idx in range(len(jobs)):
			# 인덱스를 늘리면서 처리되지 않은 job들을 찾음
			if idx not in finish:
				if jobs[idx][0] > current:
					current = jobs[idx][0]
					break
				vaild = [] # 현 시점에서 처리가능한 job들을 모아둠 (현재시간보다 요청시간이 이전이거나 같은 경우)
				for job, i in zip(jobs[idx:], range(idx,len(jobs))):
					if job[0] > current: # 작업의 요청시간이 현재보다 클 경우
						break
					if i not in finish:
						vaild.append(job + [i])
				next_job = sorted(vaild, key=lambda x : (x[1]))[0]
				finish.append(next_job[2])
				answer += (current - next_job[0] + next_job[1])
				current += next_job[1]
				break
	return answer // (len(jobs))