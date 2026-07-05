#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* myString) {
    int len = 0;
    while (myString[len] != '\0'){
        len++;
    }
    
    char* answer = (char*)malloc(sizeof(char) * (len + 1));
    
    for (int i = 0; i < len; i++){
        if (myString[i] >= 'a' && myString[i] <= 'z'){
            answer[i] = myString[i] - 32;
        }
        else {
            answer[i] = myString[i];
        }
    }
    
    answer[len] = '\0';
    return answer;
}