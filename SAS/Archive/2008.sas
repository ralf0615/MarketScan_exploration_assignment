libname temp "/rpscan/u071439/MarketScan_exploration_project/2008";

proc sql;
create table temp.trash1 as select *
from
ARCH2008.ccaea083
where client = 455;

proc sql;
create table temp.trash2 as select *
from
ARCH2008.ccaed083
where client = 455;

proc sql;
create table temp.trash3 as select *
from
ARCH2008.ccaee083
where client = 455;

proc sql;
create table temp.trash4 as select *
from
ARCH2008.ccaef083
where client = 455;

proc sql;
create table temp.trash5 as select *
from
ARCH2008.ccaei083
where client = 455;

proc sql;
create table temp.trash6 as select *
from
ARCH2008.ccaeo083
where client = 455;

proc sql;
create table temp.trash7 as select *
from
ARCH2008.ccaep083
where client = 455;

proc sql;
create table temp.trash8 as select *
from
ARCH2008.ccaer083
where client = 455;

proc sql;
create table temp.trash9 as select *
from
ARCH2008.ccaes083
where client = 455;

proc sql;
create table temp.trash10 as select *
from
ARCH2008.ccaet083
where client = 455;

proc export
data = temp.trash1
outfile="/rpscan/u071439/MarketScan_exploration_project/2008/ccaea083_2008.csv"
replace;
run;

proc export
data = temp.trash2
outfile="/rpscan/u071439/MarketScan_exploration_project/2008/ccaed083_2008.csv"
replace;
run;

proc export
data = temp.trash3
outfile="/rpscan/u071439/MarketScan_exploration_project/2008/ccaee083_2008.csv"
replace;
run;

proc export
data = temp.trash4
outfile="/rpscan/u071439/MarketScan_exploration_project/2008/ccaef083_2008.csv"
replace;
run;

proc export
data = temp.trash5
outfile="/rpscan/u071439/MarketScan_exploration_project/2008/ccaei083_2008.csv"
replace;
run;

proc export
data = temp.trash6
outfile="/rpscan/u071439/MarketScan_exploration_project/2008/ccaeo083_2008.csv"
replace;
run;

proc export
data = temp.trash7
outfile="/rpscan/u071439/MarketScan_exploration_project/2008/ccaep083_2008.csv"
replace;
run;

proc export
data = temp.trash8
outfile="/rpscan/u071439/MarketScan_exploration_project/2008/ccaer083_2008.csv"
replace;
run;

proc export
data = temp.trash9
outfile="/rpscan/u071439/MarketScan_exploration_project/2008/ccaes083_2008.csv"
replace;
run;

proc export
data = temp.trash10
outfile="/rpscan/u071439/MarketScan_exploration_project/2008/ccaet083_2008.csv"
replace;
run;


