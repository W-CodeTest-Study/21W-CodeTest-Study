#include <string>
#include <vector>

using namespace std;

int dfs(vector<int> numbers, int target){
	if(numbers.empty())
		return target == 0 ? 1 : 0;

	int last = numbers.back();
	numbers.pop_back();
	return dfs(numbers, target + last) + dfs(numbers, target - last);
}

int solution(vector<int> numbers, int target) {
	return dfs(numbers, target);
}
