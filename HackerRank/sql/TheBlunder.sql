/*
Enter your query here.
*/
SELECT CEIL(AVG(SALARY)-AVG(replace(replace(Salary,'0',' '),' ','')))  from EMPLOYEES ;

-- SELECT replace(replace(Salary,'0',' '),' ','')) from EMPLOYEES; -- OMMITING THE SPACES AND CONCATENATE