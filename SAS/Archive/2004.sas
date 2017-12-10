libname temp "/rpscan/u071439/MarketScan_exploration_project/2004";

proc sql;
create table temp.trash1 as select *
from
ARCH2004.ccaea045
where client = 455;

proc sql;
create table temp.trash2 as select *
from
ARCH2004.ccaed045
where client = 455;

proc sql;
create table temp.trash3 as select *
from
ARCH2004.ccaee045
where client = 455;

proc sql;
create table temp.trash4 as select *
from
ARCH2004.ccaef045
where client = 455;

proc sql;
create table temp.trash5 as select *
from
ARCH2004.ccaei045
where client = 455;

proc sql;
create table temp.trash6 as select *
from
ARCH2004.ccaeo045
where client = 455;

proc sql;
create table temp.trash7 as select *
from
ARCH2004.ccaep045
where client = 455;

proc sql;
create table temp.trash8 as select *
from
ARCH2004.ccaer045
where client = 455;

proc sql;
create table temp.trash9 as select *
from
ARCH2004.ccaes045
where client = 455;

proc sql;
create table temp.trash10 as select *
from
ARCH2004.ccaet045
where client = 455;

proc export
data = temp.trash1
outfile="/rpscan/u071439/MarketScan_exploration_project/2004/ccaea045_2004.csv"
replace;
run;

proc export
data = temp.trash2
outfile="/rpscan/u071439/MarketScan_exploration_project/2004/ccaed045_2004.csv"
replace;
run;

proc export
data = temp.trash3
outfile="/rpscan/u071439/MarketScan_exploration_project/2004/ccaee045_2004.csv"
replace;
run;

proc export
data = temp.trash4
outfile="/rpscan/u071439/MarketScan_exploration_project/2004/ccaef045_2004.csv"
replace;
run;

proc export
data = temp.trash5
outfile="/rpscan/u071439/MarketScan_exploration_project/2004/ccaei045_2004.csv"
replace;
run;

proc export
data = temp.trash6
outfile="/rpscan/u071439/MarketScan_exploration_project/2004/ccaeo045_2004.csv"
replace;
run;

proc export
data = temp.trash7
outfile="/rpscan/u071439/MarketScan_exploration_project/2004/ccaep045_2004.csv"
replace;
run;

proc export
data = temp.trash8
outfile="/rpscan/u071439/MarketScan_exploration_project/2004/ccaer045_2004.csv"
replace;
run;

proc export
data = temp.trash9
outfile="/rpscan/u071439/MarketScan_exploration_project/2004/ccaes045_2004.csv"
replace;
run;

proc export
data = temp.trash10
outfile="/rpscan/u071439/MarketScan_exploration_project/2004/ccaet045_2004.csv"
replace;
run;


