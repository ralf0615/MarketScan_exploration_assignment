libname temp "/rpscan/u071439/MarketScan_exploration_project/2006";

proc sql;
create table temp.trash1 as select *
from
ARCH2006.ccaea063
where client = 455;

proc sql;
create table temp.trash2 as select *
from
ARCH2006.ccaed063
where client = 455;

proc sql;
create table temp.trash3 as select *
from
ARCH2006.ccaee063
where client = 455;

proc sql;
create table temp.trash4 as select *
from
ARCH2006.ccaef063
where client = 455;

proc sql;
create table temp.trash5 as select *
from
ARCH2006.ccaei063
where client = 455;

proc sql;
create table temp.trash6 as select *
from
ARCH2006.ccaeo063
where client = 455;

proc sql;
create table temp.trash7 as select *
from
ARCH2006.ccaep063
where client = 455;

proc sql;
create table temp.trash8 as select *
from
ARCH2006.ccaer063
where client = 455;

proc sql;
create table temp.trash9 as select *
from
ARCH2006.ccaes063
where client = 455;

proc sql;
create table temp.trash10 as select *
from
ARCH2006.ccaet063
where client = 455;

proc export
data = temp.trash1
outfile="/rpscan/u071439/MarketScan_exploration_project/2006/ccaea063_2006.csv"
replace;
run;

proc export
data = temp.trash2
outfile="/rpscan/u071439/MarketScan_exploration_project/2006/ccaed063_2006.csv"
replace;
run;

proc export
data = temp.trash3
outfile="/rpscan/u071439/MarketScan_exploration_project/2006/ccaee063_2006.csv"
replace;
run;

proc export
data = temp.trash4
outfile="/rpscan/u071439/MarketScan_exploration_project/2006/ccaef063_2006.csv"
replace;
run;

proc export
data = temp.trash5
outfile="/rpscan/u071439/MarketScan_exploration_project/2006/ccaei063_2006.csv"
replace;
run;

proc export
data = temp.trash6
outfile="/rpscan/u071439/MarketScan_exploration_project/2006/ccaeo063_2006.csv"
replace;
run;

proc export
data = temp.trash7
outfile="/rpscan/u071439/MarketScan_exploration_project/2006/ccaep063_2006.csv"
replace;
run;

proc export
data = temp.trash8
outfile="/rpscan/u071439/MarketScan_exploration_project/2006/ccaer063_2006.csv"
replace;
run;

proc export
data = temp.trash9
outfile="/rpscan/u071439/MarketScan_exploration_project/2006/ccaes063_2006.csv"
replace;
run;

proc export
data = temp.trash10
outfile="/rpscan/u071439/MarketScan_exploration_project/2006/ccaet063_2006.csv"
replace;
run;


