#과거에 공부했던 문제 cpp로 일단 생성.. 추후 수정 예정

#include <stdio.h>
#include <string.h>
int main(void)
{
 int i, j, max = 0;
 char line[5][15] = {0};

 for (i = 0; i < 5; i++)
 {
  scanf("%s", line[i]);
  if (strlen(line[i]) > max)
   max = strlen(line[i]);
 }

 for (i = 0; i < max; i++)
 {
  for (j = 0; j < 5; j++)
  {
   if (line[j][i] == NULL)
    continue;
   printf("%c", line[j][i]);
  }
 }
}

//출처: https://young21story.tistory.com/28 [코딩일지]
