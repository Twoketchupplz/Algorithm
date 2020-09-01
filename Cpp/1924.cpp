#include "stdio.h"

int main() {
    int month, day, idx;
    int period = 0;

    scanf("%d %d", &month, &day);

    period = (month-1)*30;
    for(int i = 1; i < month; i+=2) period++;
    if(month > 6) period++;
    if(month == 12) period--;
    if(month > 2) period -= 2;
    period += day;

    char *day_of_week[7] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
    idx = period%7;
    printf("%s", day_of_week[idx]);
    return 0;
}

//오답입니다.