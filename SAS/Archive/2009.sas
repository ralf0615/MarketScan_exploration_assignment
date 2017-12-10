libname temp "/rpscan/u071439/MarketScan_exploration_project/2009";

proc sql;
create table temp.trash1 as select *
from
ARCH2009.ccaea093
where client = 455;

proc sql;
create table temp.trash2 as select *
from
ARCH2009.ccaed093
where client = 455;

proc sql;
create table temp.trash3 as select *
from
ARCH2009.ccaee093
where client = 455;

proc sql;
create table temp.trash4 as select *
from
ARCH2009.ccaef093
where client = 455;

proc sql;
create table temp.trash5 as select *
from
ARCH2009.ccaei093
where client = 455;

proc sql;
create table temp.trash6 as select *
from
ARCH2009.ccaeo093
where client = 455;

proc sql;
create table temp.trash7 as select *
from
ARCH2009.ccaep093
where client = 455;

proc sql;
create table temp.trash8 as select *
from
ARCH2009.ccaer093
where client = 455;

proc sql;
create table temp.trash9 as select *
from
ARCH2009.ccaes093
where client = 455;

proc sql;
create table temp.trash10 as select *
from
ARCH2009.ccaet093
where client = 455;

proc export
data = temp.trash1
outfile="/rpscan/u071439/MarketScan_exploration_project/2009/ccaea093_2009.csv"
replace;
run;

proc export
data = temp.trash2
outfile="/rpscan/u071439/MarketScan_exploration_project/2009/ccaed093_2009.csv"
replace;
run;

proc export
data = temp.trash3
outfile="/rpscan/u071439/MarketScan_exploration_project/2009/ccaee093_2009.csv"
replace;
run;

proc export
data = temp.trash4
outfile="/rpscan/u071439/MarketScan_exploration_project/2009/ccaef093_2009.csv"
replace;
run;

proc export
data = temp.trash5
outfile="/rpscan/u071439/MarketScan_exploration_project/2009/ccaei093_2009.csv"
replace;
run;

proc export
data = temp.trash6
outfile="/rpscan/u071439/MarketScan_exploration_project/2009/ccaeo093_2009.csv"
replace;
run;

proc export
data = temp.trash7
outfile="/rpscan/u071439/MarketScan_exploration_project/2009/ccaep093_2009.csv"
replace;
run;

proc export
data = temp.trash8
outfile="/rpscan/u071439/MarketScan_exploration_project/2009/ccaer093_2009.csv"
replace;
run;

proc export
data = temp.trash9
outfile="/rpscan/u071439/MarketScan_exploration_project/2009/ccaes093_2009.csv"
replace;
run;

proc export
data = temp.trash10
outfile="/rpscan/u071439/MarketScan_exploration_project/2009/ccaet093_2009.csv"
replace;
run;


