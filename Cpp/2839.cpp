#include "stdio.h"

int main() {
    int N;
    int ans = -1;

    scanf("%d", &N);

    while(true){
        if(N == 0 || N == 1 || N == 2 || N == 4 || N == 7) break;
        else if (N%5 == 0) {
            ans = N / 5;
            break;
        }
        else if(N%5 == 1) {
            ans = N/5 + 1;
            break;
        }
        else if(N%5 == 2){
            ans = N/5 + 2;
            break;
        }
        else if(N%5 == 3){
            ans = N/5 + 1;
            break;
        }
        else{
            ans = N/5 + 2;
            break;
        }
    }

    printf("%d", ans);

    return 0;
}