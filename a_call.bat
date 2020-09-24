@ ECHO OFF
set STARTTIME=%TIME%
echo          ---------------
echo Start    : %STARTTIME% %0
echo          ---------------

: -------------------------------------------------


IF EXIST c:\Python27\python.exe (
    SET PYTHON_PATH=c:\Python27\python.exe
)

 
rem echo  "PYTHON_PATH=%PYTHON_PATH%



set CLONE_PATH=c:\Git\w01\
SET CPSS_PATH=%CLONE_PATH%\cpss
SET cpss_tool=%CPSS_PATH%\tools
SET tool_genScripts=%cpss_tool%\genScripts
SET tool_codeCheck=%tool_genScripts%\codeChecks
SET TOOL_COMMON=%cpss_tool%\common
set SCRIPT_DIR=%CPSS_PATH%\tools\admin

SET WORK_PATH=%CD%
SET WORK_DRIVE=%WORK_PATH:~0,2%


%WORK_DRIVE%
cd %WORK_PATH%


ECHO  "Call=%PYTHON_PATH% c:\Git\ws01\kino\del_adobe_dir_1.py%
%PYTHON_PATH% c:\Git\ws01\kino\del_adobe_dir_1.py

CALL %TOOL_COMMON%\duration.bat %STARTTIME% %0
