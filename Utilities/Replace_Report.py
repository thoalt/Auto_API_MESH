from Utilities import global_dir as gd

ReportName = "Report_Logout_21092022.html"
ReportFile = gd.REPORT_FILES_PATH + ReportName

ReportOut = ReportFile.replace(".html", "") + "_After.html"
with open(ReportFile, "rt") as fin:
    with open(ReportOut, "wt") as fout:
        for line in fin:
            fout.write(line.replace("Expected <", "Expected <\"").replace("equal to <", "equal to <\""))

