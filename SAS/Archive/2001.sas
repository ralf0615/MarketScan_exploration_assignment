libname temp "/rpscan/u071439/MarketScan_exploration_project/2001";

proc sql;
create table temp.trash1 as select *
from
ARCH2001.ccaea013
where client = 455;

proc sql;
create table temp.trash2 as select *
from
ARCH2001.ccaed013
where client = 455;

proc sql;
create table temp.trash3 as select *
from
ARCH2001.ccaee013
where client = 455;

proc sql;
create table temp.trash4 as select *
from
ARCH2001.ccaef013
where client = 455;

proc sql;
create table temp.trash5 as select *
from
ARCH2001.ccaei013
where client = 455;

proc sql;
create table temp.trash6 as select *
from
ARCH2001.ccaeo013
where client = 455;

proc sql;
create table temp.trash7 as select *
from
ARCH2001.ccaep013
where client = 455;

proc sql;
create table temp.trash8 as select *
from
ARCH2001.ccaer013
where client = 455;

proc sql;
create table temp.trash9 as select *
from
ARCH2001.ccaes013
where client = 455;

proc sql;
create table temp.trash10 as select *
from
ARCH2001.ccaet013
where client = 455;

proc export
data = temp.trash1
outfile="/rpscan/u071439/MarketScan_exploration_project/2001/ccaea013_2001.csv"
replace;
run;

proc export
data = temp.trash2
outfile="/rpscan/u071439/MarketScan_exploration_project/2001/ccaed013_2001.csv"
replace;
run;

proc export
data = temp.trash3
outfile="/rpscan/u071439/MarketScan_exploration_project/2001/ccaee013_2001.csv"
replace;
run;

proc export
data = temp.trash4
outfile="/rpscan/u071439/MarketScan_exploration_project/2001/ccaef013_2001.csv"
replace;
run;

proc export
data = temp.trash5
outfile="/rpscan/u071439/MarketScan_exploration_project/2001/ccaei013_2001.csv"
replace;
run;

proc export
data = temp.trash6
outfile="/rpscan/u071439/MarketScan_exploration_project/2001/ccaeo013_2001.csv"
replace;
run;

proc export
data = temp.trash7
outfile="/rpscan/u071439/MarketScan_exploration_project/2001/ccaep013_2001.csv"
replace;
run;

proc export
data = temp.trash8
outfile="/rpscan/u071439/MarketScan_exploration_project/2001/ccaer013_2001.csv"
replace;
run;

proc export
data = temp.trash9
outfile="/rpscan/u071439/MarketScan_exploration_project/2001/ccaes013_2001.csv"
replace;
run;

proc export
data = temp.trash10
outfile="/rpscan/u071439/MarketScan_exploration_project/2001/ccaet013_2001.csv"
replace;
run;


