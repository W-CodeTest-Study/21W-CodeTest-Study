#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool hit_time_cmp(vector<int> & a, vector<int> & b){
    return a[0] > b[0];
}

bool take_time_cmp(vector<int> & a, vector<int> & b){
    return a[1] > b[1];
}

int solution(vector<vector<int>> jobs) {
    int answer = 0, N = jobs.size();
    int time = 0, numOfRequested = 0;
    int & nr = numOfRequested;
    vector<int> current_job(2, -1);
    vector<vector<int>> requested_jobs(N, vector<int>(2, 1001));
    vector<vector<int>> & rj = requested_jobs;
    
    make_heap(jobs.begin(), jobs.end(), hit_time_cmp);
    
    while(jobs.size() > 0 || nr > 0)
    {
        while(jobs.size() > 0 && jobs[0][0] <= time){
            pop_heap(jobs.begin(), jobs.end(), hit_time_cmp);
            requested_jobs.push_back(jobs.back());
            jobs.pop_back();
            push_heap(rj.begin(), rj.end(), take_time_cmp);
            nr++;
        }
        if(jobs.size() > 0 && nr == 0)
            time = jobs[0][0];
        if(nr > 0 && current_job[0] == -1){
            pop_heap(rj.begin(), rj.end(), take_time_cmp);
            current_job[0] = rj.back()[0];
            current_job[1] = rj.back()[1];
            rj.pop_back();
            nr--;
        }
        if(current_job[0] != -1){
            time += current_job[1];
            answer += time - current_job[0];
            current_job[0] = -1;
        }
    }
    
    return answer / N;
}
