/*
Enter your query here.
*/

SELECT MAX(SALARY*MONTHS), COUNT(SALARY*MONTHS) FROM EMPLOYEE WHERE SALARY*MONTHS=
(SELECT MAX(SALARY*MONTHS) FROM EMPLOYEE);