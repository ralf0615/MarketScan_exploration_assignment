libname temp "/rpscan/u071439/MarketScan_exploration_project/2014";

proc sql;
create table temp.trash5 as select *
from
ARCH2014.ccaei143
where client = 858;

proc export
data = temp.trash5
outfile="/rpscan/u071439/MarketScan_exploration_project/2014/ccaei143_2014_Des.csv"
replace;
run;


