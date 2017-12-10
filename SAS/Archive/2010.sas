libname temp "/rpscan/u071439/MarketScan_exploration_project/2010";

proc sql;
create table temp.trash1 as select *
from
ARCH2010.ccaea103
where client = 455;

proc sql;
create table temp.trash2 as select *
from
ARCH2010.ccaed103
where client = 455;

proc sql;
create table temp.trash3 as select *
from
ARCH2010.ccaee103
where client = 455;

proc sql;
create table temp.trash4 as select *
from
ARCH2010.ccaef103
where client = 455;

proc sql;
create table temp.trash5 as select *
from
ARCH2010.ccaei103
where client = 455;

proc sql;
create table temp.trash6 as select *
from
ARCH2010.ccaeo103
where client = 455;

proc sql;
create table temp.trash7 as select *
from
ARCH2010.ccaep103
where client = 455;

proc sql;
create table temp.trash8 as select *
from
ARCH2010.ccaer103
where client = 455;

proc sql;
create table temp.trash9 as select *
from
ARCH2010.ccaes103
where client = 455;

proc sql;
create table temp.trash10 as select *
from
ARCH2010.ccaet103
where client = 455;

proc export
data = temp.trash1
outfile="/rpscan/u071439/MarketScan_exploration_project/2010/ccaea103_2010.csv"
replace;
run;

proc export
data = temp.trash2
outfile="/rpscan/u071439/MarketScan_exploration_project/2010/ccaed103_2010.csv"
replace;
run;

proc export
data = temp.trash3
outfile="/rpscan/u071439/MarketScan_exploration_project/2010/ccaee103_2010.csv"
replace;
run;

proc export
data = temp.trash4
outfile="/rpscan/u071439/MarketScan_exploration_project/2010/ccaef103_2010.csv"
replace;
run;

proc export
data = temp.trash5
outfile="/rpscan/u071439/MarketScan_exploration_project/2010/ccaei103_2010.csv"
replace;
run;

proc export
data = temp.trash6
outfile="/rpscan/u071439/MarketScan_exploration_project/2010/ccaeo103_2010.csv"
replace;
run;

proc export
data = temp.trash7
outfile="/rpscan/u071439/MarketScan_exploration_project/2010/ccaep103_2010.csv"
replace;
run;

proc export
data = temp.trash8
outfile="/rpscan/u071439/MarketScan_exploration_project/2010/ccaer103_2010.csv"
replace;
run;

proc export
data = temp.trash9
outfile="/rpscan/u071439/MarketScan_exploration_project/2010/ccaes103_2010.csv"
replace;
run;

proc export
data = temp.trash10
outfile="/rpscan/u071439/MarketScan_exploration_project/2010/ccaet103_2010.csv"
replace;
run;


