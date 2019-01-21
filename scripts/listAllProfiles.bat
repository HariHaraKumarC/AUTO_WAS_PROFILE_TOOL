@REM Author: HariHaraKumar Chandrabose
@REM This file list all the created WAS profiles

@SETLOCAL
@ECHO OFF

ECHO This script will list all the WAS Profiles.(Arguments to be passed: WAS_INSTALL_DIR)

@REM Get WAS_DIR from the autoProfileTool.properties
FOR /F "tokens=1* delims==" %%A IN (autoProfileTool.properties) DO (
    IF "%%A"=="WAS_DIR" set WAS_INSTALL_DIR=%%B
)
ECHO WAS Installation directory is "%WAS_INSTALL_DIR%"

ECHO Continuing with fetching the WAS Profiles... Please wait...

@REM Fetching the list of WAS Server Profiles
@REM Parameters: (1 Parameter) WAS_INSTALL_DIR
CALL "%WAS_INSTALL_DIR%\bin\manageprofiles" -listProfiles
IF NOT ["%errorlevel%"]==["0"] (
    PAUSE
    ECHO Error occurs while fetching the list of WAS profiles.
    EXIT /b %errorlevel%
)

ECHO List of WAS Profiles fetched successfully.

@ENDLOCAL

