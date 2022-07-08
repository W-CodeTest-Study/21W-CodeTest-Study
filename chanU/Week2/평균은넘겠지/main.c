#include <stdio.h>
#include <stdlib.h>

int main(void){
	int n;
	double N;

	scanf("%d", &n);

	for(int i = 0 ; i < n ; i ++ ){
		int * stu;
		double avg = 0, goodStu = 0;
		scanf("%lf", &N);
		stu = (int *)malloc(sizeof(int) * N);
		for(int j = 0 ; j < N ; j ++){
			scanf("%d", &stu[j]);
			avg += stu[j];
		}
		avg = avg / N;

		for(int j = 0 ; j < N ; j ++){
			if(avg < stu[j])
				goodStu += 1.0;
		}

		printf("%.3f%%\n", (goodStu/N) * 100);
		free(stu);
	}
}
