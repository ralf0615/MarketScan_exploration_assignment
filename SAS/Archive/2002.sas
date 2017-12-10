libname temp "/rpscan/u071439/MarketScan_exploration_project";

proc sql;
create table temp.trash1 as select *
from
ARCH2002.ccaea023
where client = 455;

proc sql;
create table temp.trash2 as select *
from
ARCH2002.ccaed023
where client = 455;

proc sql;
create table temp.trash3 as select *
from
ARCH2002.ccaee023
where client = 455;

proc sql;
create table temp.trash4 as select *
from
ARCH2002.ccaef023
where client = 455;

proc sql;
create table temp.trash5 as select *
from
ARCH2002.ccaei023
where client = 455;

proc sql;
create table temp.trash6 as select *
from
ARCH2002.ccaeo023
where client = 455;

proc sql;
create table temp.trash7 as select *
from
ARCH2002.ccaep023
where client = 455;

proc sql;
create table temp.trash8 as select *
from
ARCH2002.ccaer023
where client = 455;

proc sql;
create table temp.trash9 as select *
from
ARCH2002.ccaes023
where client = 455;

proc sql;
create table temp.trash10 as select *
from
ARCH2002.ccaet023
where client = 455;

proc export
data = temp.trash1
outfile="/rpscan/u071439/MarketScan_exploration_project/2002/ccaea023_2002.csv"
replace;
run;

proc export
data = temp.trash2
outfile="/rpscan/u071439/MarketScan_exploration_project/2002/ccaed023_2002.csv"
replace;
run;

proc export
data = temp.trash3
outfile="/rpscan/u071439/MarketScan_exploration_project/2002/ccaee023_2002.csv"
replace;
run;

proc export
data = temp.trash4
outfile="/rpscan/u071439/MarketScan_exploration_project/2002/ccaef023_2002.csv"
replace;
run;

proc export
data = temp.trash5
outfile="/rpscan/u071439/MarketScan_exploration_project/2002/ccaei023_2002.csv"
replace;
run;

proc export
data = temp.trash6
outfile="/rpscan/u071439/MarketScan_exploration_project/2002/ccaeo023_2002.csv"
replace;
run;

proc export
data = temp.trash7
outfile="/rpscan/u071439/MarketScan_exploration_project/2002/ccaep023_2002.csv"
replace;
run;

proc export
data = temp.trash8
outfile="/rpscan/u071439/MarketScan_exploration_project/2002/ccaer023_2002.csv"
replace;
run;

proc export
data = temp.trash9
outfile="/rpscan/u071439/MarketScan_exploration_project/2002/ccaes023_2002.csv"
replace;
run;

proc export
data = temp.trash10
outfile="/rpscan/u071439/MarketScan_exploration_project/2002/ccaet023_2002.csv"
replace;
run;


