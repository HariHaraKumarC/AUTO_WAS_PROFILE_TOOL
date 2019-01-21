@REM Author: HariHaraKumar Chandrabose
@REM This file create the deletes the existing WAS Server profile

@SETLOCAL
@ECHO OFF

ECHO This script will delete an WebSphere 7 application server profile.(Arguments to be passed: PROFILE_NAME)

@REM Get WAS_DIR from the autoProfileTool.properties
FOR /F "tokens=1* delims==" %%A IN (autoProfileTool.properties) DO (
    IF "%%A"=="WAS_DIR" set WAS_INSTALL_DIR=%%B
)
ECHO WAS Installation directory is "%WAS_INSTALL_DIR%"

@REM Check for arguments
ECHO Checking for the arguments...
IF %1 == "" (
    ECHO Argument PROFILE_NAME cannot be empty.
    ECHO WAS Profile Creation Stopped.
    EXIT)
ECHO Arguments are ok.
ECHO Continuing with WAS Profile Deletion... Please wait..

@REM Set other variables
SET PROFILE_NAME=%1

@REM Deleting the WAS Server Profile
@REM Parameters: (2 Parameter) WAS_INSTALL_DIR,PROFILE_NAME
CALL "%WAS_INSTALL_DIR%\bin\manageprofiles" -delete -profileName %PROFILE_NAME%
IF NOT ["%errorlevel%"]==["0"] (
    PAUSE
    ECHO [9999].Error occurs while deleting the WAS profile.
    EXIT /b %errorlevel%
)

ECHO [0000].WAS Profile %PROFILE_NAME% deleted successfully.

@ENDLOCAL