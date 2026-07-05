#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// num_list_len은 배열 num_list의 길이입니다.
int solution(int num_list[], size_t num_list_len) {
    int multiply = 1;
    int sum = 0;
    
    // 곱, 합 구하기
    for (int i = 0; i < num_list_len; i++){
        multiply *= num_list[i];    
        sum += num_list[i];
    }
    
    return (multiply < sum*sum) ? 1 : 0;
}