#include <stdio.h>
#include <math.h>

int main(){

    int C = 0, N = 0, sum = 0;
    int arr[1000] = {0,};
    double age, value;

    scanf("%d",&C);

    for(int i=0;i<C;i++){
        scanf("%d",&N);
        sum = 0;
        value = 0;
        for(int j=0;j<N;j++){
            scanf("%d",&arr[j]);
            sum += arr[j];
        }
        age = sum / (double)N;

        for(int j=0;j<N;j++){
            if(age < arr[j]){
                value += 100 / (double)N;
            }
        }
        printf("%.3lf%%\n", value);
    }

    return 0;
}