libname temp "/rpscan/u071439/MarketScan_exploration_project/2005";

proc sql;
create table temp.trash1 as select *
from
ARCH2005.ccaea054
where client = 455;

proc sql;
create table temp.trash2 as select *
from
ARCH2005.ccaed054
where client = 455;

proc sql;
create table temp.trash3 as select *
from
ARCH2005.ccaee054
where client = 455;

proc sql;
create table temp.trash4 as select *
from
ARCH2005.ccaef054
where client = 455;

proc sql;
create table temp.trash5 as select *
from
ARCH2005.ccaei054
where client = 455;

proc sql;
create table temp.trash6 as select *
from
ARCH2005.ccaeo054
where client = 455;

proc sql;
create table temp.trash7 as select *
from
ARCH2005.ccaep054
where client = 455;

proc sql;
create table temp.trash8 as select *
from
ARCH2005.ccaer054
where client = 455;

proc sql;
create table temp.trash9 as select *
from
ARCH2005.ccaes054
where client = 455;

proc sql;
create table temp.trash10 as select *
from
ARCH2005.ccaet054
where client = 455;

proc export
data = temp.trash1
outfile="/rpscan/u071439/MarketScan_exploration_project/2005/ccaea054_2005.csv"
replace;
run;

proc export
data = temp.trash2
outfile="/rpscan/u071439/MarketScan_exploration_project/2005/ccaed054_2005.csv"
replace;
run;

proc export
data = temp.trash3
outfile="/rpscan/u071439/MarketScan_exploration_project/2005/ccaee054_2005.csv"
replace;
run;

proc export
data = temp.trash4
outfile="/rpscan/u071439/MarketScan_exploration_project/2005/ccaef054_2005.csv"
replace;
run;

proc export
data = temp.trash5
outfile="/rpscan/u071439/MarketScan_exploration_project/2005/ccaei054_2005.csv"
replace;
run;

proc export
data = temp.trash6
outfile="/rpscan/u071439/MarketScan_exploration_project/2005/ccaeo054_2005.csv"
replace;
run;

proc export
data = temp.trash7
outfile="/rpscan/u071439/MarketScan_exploration_project/2005/ccaep054_2005.csv"
replace;
run;

proc export
data = temp.trash8
outfile="/rpscan/u071439/MarketScan_exploration_project/2005/ccaer054_2005.csv"
replace;
run;

proc export
data = temp.trash9
outfile="/rpscan/u071439/MarketScan_exploration_project/2005/ccaes054_2005.csv"
replace;
run;

proc export
data = temp.trash10
outfile="/rpscan/u071439/MarketScan_exploration_project/2005/ccaet054_2005.csv"
replace;
run;


