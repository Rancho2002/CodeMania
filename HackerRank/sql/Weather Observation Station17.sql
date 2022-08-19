/*
Enter your query here.
*/
select round(LONG_W,4) FROM STATION where LAT_N=
(SELECT MIN(LAT_N) FROM STATION WHERE LAT_N>38.7780);