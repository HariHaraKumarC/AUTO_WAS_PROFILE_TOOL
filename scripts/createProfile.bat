@REM Author: HariHaraKumar Chandrabose
@REM This file create the empty WAS Server profile

@SETLOCAL
@ECHO OFF

ECHO This script will create an WebSphere 7 application server profile.Before running the script, you must have,WebSphere 7 installed on your machine.(Arguments to be passed: APP_PREFIX,WAS_INSTALL_DIR)

@REM Get WAS_DIR from the autoProfileTool.properties
FOR /F "tokens=1* delims==" %%A IN (autoProfileTool.properties) DO (
    IF "%%A"=="WAS_DIR" set WAS_INSTALL_DIR=%%B
)
ECHO WAS Installation directory is "%WAS_INSTALL_DIR%"

@REM Check for arguments
ECHO Checking for the arguments...
IF %1 == "" (
    ECHO Argument APP_PREFIX cannot be empty.
    ECHO WAS Profile Creation Stopped.
    EXIT)
ECHO Arguments are ok.
ECHO Continuing with WAS Profile Creation.

@REM Set other variables
SET APP_PREFIX=%1
SET PROFILE_NAME=%APP_PREFIX%_PROFILE
SET PROFILE_PATH=%WAS_INSTALL_DIR%\profiles\%PROFILE_NAME%
SET PATH=%PATH%;%WAS_INSTALL_DIR%\bin
SET CELL_NAME=%APP_PREFIX%_CELL
SET NODE_NAME=%APP_PREFIX%_NODE
SET SERVER_NAME=%APP_PREFIX%_SERVER

@REM Confirm inputs
ECHO A server profile will be created using the following settings:(- profile name: %PROFILE_NAME% , - profile path: %PROFILE_PATH% , - cell name: %CELL_NAME% , - node name: %NODE_NAME% , - server name: %SERVER_NAME%)
ECHO The server profile is now being created...Please wait...

@REM Creating Empty WAS Server Profile
@REM Parameters: (6 Parameters) WAS_INSTALL_DIR,PROFILE_NAME,PROFILE_PATH,CELL_NAME,NODE_NAME,SERVER_NAME
CALL "%WAS_INSTALL_DIR%\bin\manageprofiles" -create -profileName %PROFILE_NAME% -templatePath default -profilePath "%PROFILE_PATH%" -enableAdminSecurity false -cellName %CELL_NAME% -nodeName %NODE_NAME% -serverName %SERVER_NAME% -applyPerfTuningSettings development -isDeveloperServer -omitAction defaultAppDeployAndConfig
IF NOT ["%errorlevel%"]==["0"] (
    PAUSE
    ECHO Server Profile Creation Failed. Please check your inputs.
    EXIT /b %errorlevel%
)

ECHO Server profile created successfully.

@ENDLOCAL