libname temp "/rpscan/u071439/MarketScan_exploration_project/2007";

proc sql;
create table temp.trash1 as select *
from
ARCH2007.ccaea073
where client = 455;

proc sql;
create table temp.trash2 as select *
from
ARCH2007.ccaed073
where client = 455;

proc sql;
create table temp.trash3 as select *
from
ARCH2007.ccaee073
where client = 455;

proc sql;
create table temp.trash4 as select *
from
ARCH2007.ccaef073
where client = 455;

proc sql;
create table temp.trash5 as select *
from
ARCH2007.ccaei073
where client = 455;

proc sql;
create table temp.trash6 as select *
from
ARCH2007.ccaeo073
where client = 455;

proc sql;
create table temp.trash7 as select *
from
ARCH2007.ccaep073
where client = 455;

proc sql;
create table temp.trash8 as select *
from
ARCH2007.ccaer073
where client = 455;

proc sql;
create table temp.trash9 as select *
from
ARCH2007.ccaes073
where client = 455;

proc sql;
create table temp.trash10 as select *
from
ARCH2007.ccaet073
where client = 455;

proc export
data = temp.trash1
outfile="/rpscan/u071439/MarketScan_exploration_project/2007/ccaea073_2007.csv"
replace;
run;

proc export
data = temp.trash2
outfile="/rpscan/u071439/MarketScan_exploration_project/2007/ccaed073_2007.csv"
replace;
run;

proc export
data = temp.trash3
outfile="/rpscan/u071439/MarketScan_exploration_project/2007/ccaee073_2007.csv"
replace;
run;

proc export
data = temp.trash4
outfile="/rpscan/u071439/MarketScan_exploration_project/2007/ccaef073_2007.csv"
replace;
run;

proc export
data = temp.trash5
outfile="/rpscan/u071439/MarketScan_exploration_project/2007/ccaei073_2007.csv"
replace;
run;

proc export
data = temp.trash6
outfile="/rpscan/u071439/MarketScan_exploration_project/2007/ccaeo073_2007.csv"
replace;
run;

proc export
data = temp.trash7
outfile="/rpscan/u071439/MarketScan_exploration_project/2007/ccaep073_2007.csv"
replace;
run;

proc export
data = temp.trash8
outfile="/rpscan/u071439/MarketScan_exploration_project/2007/ccaer073_2007.csv"
replace;
run;

proc export
data = temp.trash9
outfile="/rpscan/u071439/MarketScan_exploration_project/2007/ccaes073_2007.csv"
replace;
run;

proc export
data = temp.trash10
outfile="/rpscan/u071439/MarketScan_exploration_project/2007/ccaet073_2007.csv"
replace;
run;


