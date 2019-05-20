#!/usr/bin/python
# coding:utf-8

TABLE_CSS_STYLE = '''
<style>
    body{
        font-family:arial;
        font-size:17px;
        color:black;
    }
    table.altrowstable  {
        font-family: arial;
        font-size:16px;
        color:#333333;
        text-align:center;
        border-width: 1px;
        border-color: #a9c6c9;
        border-collapse: collapse;
    }
    table.altrowstable th,td{
        font-size:15px;
        border-width: 1px;
        padding: 1px;
        border-style: solid;
    }
</style>
'''
# git log 和jira log 都有的表格的表头
RELEASE_NOTE_TABLE_TH = """
<tr>
    <td colspan=\"2\" bgcolor=\"#D4E9A9\"><a href=\"http://%s/#/admin/projects/%s\">%s</a></td>
    <td colspan=\"1\" bgcolor=\"#D4E9A9\">HEAD=%s</td>
    <td colspan=\"1\" bgcolor=\"#D4E9A9\"><a href=\"http://%s/gitweb?p=%s.git;a=shortlog;h=refs/heads/%s\">%s</a></td>
    <td colspan=\"6\" bgcolor=\"#205081\"><a href=\"http://%s/#/admin/projects/%s\"><font color=\"white\">%s</font></a></td>
</tr>
<tr>
    <td colspan=\"4\" bgcolor=\"#D4E9A9\">git  log</td>
    <td colspan=\"6\" bgcolor=\"#205081\"><font color=\"white\">jira log</font></td>
</tr>
"""
# 只有git log时候用到的表格表头
CHANGE_LOG_TABLE_TH = """
<tr bgcolor=\"#D4E9A9\">
    <td colspan=\"2\"><a href=\"http://%s/#/admin/projects/%s\">%s</a></td>
    <td colspan=\"1\">HEAD=%s</td>
    <td colspan=\"1\"><a href=\"http://%s/gitweb?p=%s.git;a=shortlog;h=refs/heads/%s\">%s</a></td>
</tr>
"""

# 只有jira log的时候用到的表格的表头
CHANGE_LOG_TABLE_TH3 = """
<tr bgcolor=\"#205081\">
    <td colspan=\"6\" ><a href=\"http://%s/#/admin/projects/%s\"><font color=\"white\">%s</font></a></td>
</tr>
"""

# git log 和jira log都有的时候 表格的第二表头
RELEASE_NOTE_TABLE_TH1 = """
<tr>
    <th width=\"30%\">Subject</th>
    <th width=\"5%\">Author</th>
    <th width=\"10%\">Commit ID</th>
    <th width=\"5%\">Commit date</th>

    <th width=\"5%\">Jira ID</th>
    <th width=\"5%\">Jira Project</th>
    <th width=\"30%\">Summary</th>
    <th width=\"5%\">Issue Type</th>
    <th width=\"5%\">Assignee</th>
    <th width=\"5%\">Component</th>
</tr>
"""
# 只有git log的时候 表格的第二表头
CHANGE_LOG_TABLE_TH1 = """
<tr>
    <th width=\"30%\">Subject</th>
    <th width=\"5%\">Author</th>
    <th width=\"10%\">Commit ID</th>
    <th width=\"5%\">Commit date</th>
</tr>
"""

# 只有jira的 表格的第二表头
RELEASE_NOTE_TABLE_TH2 = """
<tr>
    <th width=\"10%\">Jira ID</th>
    <th width=\"20%\">Jira Project</th>
    <th width=\"30%\">Summary</th>
    <th width=\"5%\">Issue Type</th>
    <th width=\"10%\">Assignee</th>
    <th width=\"5%\">Component</th>
</tr>
"""

# 只有jira log的表格的的一行
RELEASE_NOTE_TABLE_TR1 = """
<tr>
    <td>%s</td>                    <!-- jira id -->
    <td  align=\"left\">%s</td>    <!-- jira project -->
    <td  align=\"left\">%s</td>    <!-- jira Summary -->
    <td>%s</td>                    <!-- jira Issue Type-->
    <td>%s</td>                    <!-- jira Assignee -->
    <td>%s</td>                    <!-- jira Component -->
</tr>
"""

# git log 和 jira log的表格的的一行
RELEASE_NOTE_TABLE_TR = """
<tr>
    <td align=\"left\">%s</td>
    <td><a href=\"mailto:%s\">%s</a></td>
    <td><a href=\"%s\">%s</a></td>
    <td>%s</td>

    <td>%s</td>    <!-- jira id -->
    <td>%s</td>    <!-- jira project -->
    <td>%s</td>    <!-- jira Summary -->
    <td>%s</td>    <!-- jira Issue Type-->
    <td>%s</td>    <!-- jira Assignee -->
    <td>%s</td>    <!-- jira Component -->
</tr>
"""

# 只有git log的表格的一行
CHANGE_LOG_TABLE_TR = """
<tr>
    <td align=\"left\">%s</td>
    <td><a href=\"mailto:%s\">%s</a></td>
    <td><a href=\"%s\">%s</a></td>
    <td>%s</td>
</tr>
"""

#delete projects use
CHANGE_LOG_TABLE_TH2 = """
<tr>
    <td>Delete Projects:</td>
</tr>
"""
#delete projects use
CHANGE_LOG_TABLE_TR1 ="""
<tr align=\"left\">
    <td><a href=\"http://%s/#/admin/projects/%s\">%s</a></td>
</tr>
"""

CHANGE_LOG_TABLE_BODY = """
<table table width=\"100%%\" class=\"altrowstable\" border=\"1\">
    %s
</table>
<br/>
<br/>
"""


CHANGE_LOG_H3 = "<h3>change log since:%s</h3>"

CHANGE_LOG_H3_1 = "<h3>Delete projects:</h3>"

CHANGE_LOG_H3_2="""
<h3>Change log since the last build</h3>
<h3>last build manifest: %s</h3>
"""
CHANGE_LOG_H3_3 = "<h3>New projects change log since:%s</h3>"

RELEASE_NOTE_H3 = "<h3>New projects release note since:%s</h3>"
RELEASE_NOTE_H3_1 = "<h3>Delete project: </h3>"
RELEASE_NOTE_H3_2 = "<h3>release note</h3>"

BUILD_H3   = "<h3>Build product: %s. Fail Reason: %s</h3>"
BUILD_H3_1 = "<h3>Build product: %s pass</h3>"
BUILD_H3_2 = "<h3>Build Environment</h3>"
BUILD_H3_3 = "<h3>Image Info</h3>"

BUILD_TABLE_BODY = """
<table table width=\"80%%\" class=\"altrowstable\" border=\"1\">
    %s
</table>
<br/>
"""
BUILD_TABLE_TH = """
<tr>
    <td colspan=\"2\">%s</td>
</tr>
"""
BUILD_TABLE_TR = """
<tr align=\"left\">
<td width=\"20%%\">%s</td>
<td>%s</td>
</tr>
"""
BUILD_TABLE_A = "<a href=\"%s\">%s</a>"

# 用来标记编译错误log的html标签
BUILD_PRE = \
"""
<pre>%s</pre>
"""
# 用来做gerrit超链接
Gerrit_Table1 = "<tr><td colspan=\"4\" bgcolor=\"#D4E9A9\"><a href=\"http://192.168.4.5:8083/#/admin/projects/androidO/%s\">%s</a></td></tr>" 
Gerrit_Table2 = "<tr><td colspan=\"4\" bgcolor=\"#D4E9A9\"><a href=\"http://192.168.4.6:8083/#/admin/projects/androidO/%s\">%s</a></td></tr>"
# 用来做gitweb超链接
Gitweb_Table1 = "<td><a href=\"http://192.168.4.5:8083/gitweb?p=androidO/%s.git;a=commit;h=%s\">%s</a></td>"
Gitweb_Table2 = "<td><a href=\"http://192.168.4.6:8083/gitweb?p=androidO/%s.git;a=commit;h=%s\">%s</a></td>"
# 用来做redmine超链接
Redmine_Talbe = "<td><a href=\"http://192.168.3.78:8006/redmine/issues/%s\">%s</a></td>"

# 用来标记编译错误log的那一行html标签
BUILD_ERROR_SPAN = "<span style=\"color:red;\">%s</span>"

CREATE_BRANCH_H3 = "<h3>How to fetch the code</h3>"

BR = "<br/>"

HTML = """
<html>
<head>
<meta charset="utf-8">
%s
</head>
<body>
<table>
%s
</table>
</body>
</html>
"""





