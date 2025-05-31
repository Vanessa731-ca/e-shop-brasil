rem Windows 11 Quiet Period

pushd %~dp0

ver | findstr 10.0.2
if %errorlevel%==0 goto WIN11

:WIN10
echo label=false> HermesTarget.inf
goto END

:WIN11
echo label=true> HermesTarget.inf

:END

popd
