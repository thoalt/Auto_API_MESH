REM Run testcase
for /f "skip=1" %%i in ('wmic os get localdatetime') do if not defined fulldate set fulldate=%%i
set year=%fulldate:~0,4%
set month=%fulldate:~4,2%
set day=%fulldate:~6,2%
set foldername=Report\%year%_%month%_%day%
md %foldername%

pytest -v -s testcase/Group_1/AddNewNode --html=foldername\AddNewNode.html
timeout /t 30



REM pytest -v -s tests/MOD/RuleInputCAP --html=report\HTML\Report_19012021_RuleInputCAP.html --capture=tee-sys --excelreport=report\Excel\report.xls
