libname temp "/rpscan/u071439/MarketScan_exploration_project/2003";

proc sql;
create table temp.trash1 as select *
from
ARCH2003.ccaea033
where client = 455;

proc sql;
create table temp.trash2 as select *
from
ARCH2003.ccaed033
where client = 455;

proc sql;
create table temp.trash3 as select *
from
ARCH2003.ccaee033
where client = 455;

proc sql;
create table temp.trash4 as select *
from
ARCH2003.ccaef033
where client = 455;

proc sql;
create table temp.trash5 as select *
from
ARCH2003.ccaei033
where client = 455;

proc sql;
create table temp.trash6 as select *
from
ARCH2003.ccaeo033
where client = 455;

proc sql;
create table temp.trash7 as select *
from
ARCH2003.ccaep033
where client = 455;

proc sql;
create table temp.trash8 as select *
from
ARCH2003.ccaer033
where client = 455;

proc sql;
create table temp.trash9 as select *
from
ARCH2003.ccaes033
where client = 455;

proc sql;
create table temp.trash10 as select *
from
ARCH2003.ccaet033
where client = 455;

proc export
data = temp.trash1
outfile="/rpscan/u071439/MarketScan_exploration_project/2003/ccaea033_2003.csv"
replace;
run;

proc export
data = temp.trash2
outfile="/rpscan/u071439/MarketScan_exploration_project/2003/ccaed033_2003.csv"
replace;
run;

proc export
data = temp.trash3
outfile="/rpscan/u071439/MarketScan_exploration_project/2003/ccaee033_2003.csv"
replace;
run;

proc export
data = temp.trash4
outfile="/rpscan/u071439/MarketScan_exploration_project/2003/ccaef033_2003.csv"
replace;
run;

proc export
data = temp.trash5
outfile="/rpscan/u071439/MarketScan_exploration_project/2003/ccaei033_2003.csv"
replace;
run;

proc export
data = temp.trash6
outfile="/rpscan/u071439/MarketScan_exploration_project/2003/ccaeo033_2003.csv"
replace;
run;

proc export
data = temp.trash7
outfile="/rpscan/u071439/MarketScan_exploration_project/2003/ccaep033_2003.csv"
replace;
run;

proc export
data = temp.trash8
outfile="/rpscan/u071439/MarketScan_exploration_project/2003/ccaer033_2003.csv"
replace;
run;

proc export
data = temp.trash9
outfile="/rpscan/u071439/MarketScan_exploration_project/2003/ccaes033_2003.csv"
replace;
run;

proc export
data = temp.trash10
outfile="/rpscan/u071439/MarketScan_exploration_project/2003/ccaet033_2003.csv"
replace;
run;


