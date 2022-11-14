# pytest test_multiplication.py -v --junitxml="result.xml"

from Utilities import global_dir as gd

ReportName = "Report_All_12112022.html"
ReportFile = gd.REPORT_FILES_PATH + ReportName
# ReportFile = "E:\Auto_WorkingTesting\Auto_API_MESH\Report\Report_All_04102022.html"
ReportOut = ReportFile.replace(".html", "") + "_After.html"
with open(ReportFile, "rt") as fin:
    with open(ReportOut, "wt") as fout:
        for line in fin:
            fout.write(line.replace("Expected <", "Expected <\"").replace("equal to <", "equal to <\""))

