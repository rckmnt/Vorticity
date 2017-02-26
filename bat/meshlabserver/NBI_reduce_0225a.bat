@echo OFF
@title MultiMesh Scripting
cls

echo.
echo MultiMesh Scripting - Run a MLX Script on a Folder v1.0
echo ----------------------------------------------------------------

@set STARTTIME=%TIME%

::Switch to the MultiMesh program's working directory
C:
cd C:\multiMeshScripting

::Input Mesh File variables
@set inputFolder=input
::@set inputMeshFormat=obj, or *
@set inputMeshFormat=stl

::Output Mesh File variables
@set outputFolder=output
@set outputMeshFormat=stl
::@set outputMeshFormat=ply (binary), u3d, obj

::MLX script file variables
::the MLX scripts are stored in the C:\multiMeshScripting\scripts folder
@set mlxScriptFolder=scripts
@set mlxScriptFile=reduce_90_by_20_50_75.mlx

::OM Output Mesh Options
::These options specify what data types are exported by meshlabserver
@set outputMeshOptions=
::The standard om options are "-om vc fq wn" which give vertex colors, face colors, and wedge normals

::The available OM options are:
::vc -> vertex colors           ::vf -> vertex flags        ::vq -> vertex quality
::vn-> vertex normals           ::vt -> vert texture coords   ::fc -> face colors
::ff -> face flags              ::fq -> face quality        ::fn-> face normals
::wc -> wedge colors        ::wn-> wedge normals            ::wt -> wedge texture coords

::The meshlabserver program location: ::@set meshlabserverPath="C:\Program Files\VCG\MeshLab\meshlabserver.exe"
@set meshlabserverPath= meshlabserver

::------------------------------------------------------
::      List the Current Input Mesh Format
::------------------------------------------------------

echo ----------------------------------------------------------------
echo Processing meshes with the format: %inputMeshFormat%

::------------------------------------------------------
::           List the input Meshes
::------------------------------------------------------

echo ----------------------------------------------------------------
echo Input Folder Mesh List:
for %%X in (%inputFolder%\*.%inputMeshFormat%) do (echo "%%X")
::To get help on the "for" syntax use: for /?

echo ------------------------------------------------------
echo   Run a meshlabserver MLX script on a folder
echo ------------------------------------------------------

::Example syntax that is used inside the for loop:
::"C:\Program Files\VCG\MeshLab\meshlabserver.exe" -i input\boulder-mini1.ply -o output\boulder-mini1.ply -s scripts\simple_script.mlx -om vc fq wn

::Run the "for" loop from inside the input folder
cd %inputFolder%

for %%I in (*.%inputMeshFormat%) do ( %meshlabserverPath% -i %%I -o ..\%outputFolder%\%%~nI_thin.%outputMeshFormat% -s ..\%mlxScriptFolder%\%mlxScriptFile% %outputMeshOptions%)

::Go back down a directory
cd ..

::------------------------------------------------------
::           List the Output Meshes
::------------------------------------------------------
echo.
echo ----------------------------------------------------------------

echo.
echo Output Folder Mesh List:
for %%X in (%outputFolder%\*.*) do (echo "%%X")
::To get help on the "for" syntax use: for /?
echo.
@set ENDTIME=%time%
::------------------------------------------------------
::           Done Processing
::------------------------------------------------------

echo Start Time: %START%
echo End Time: %END%
@set /A DURATION=%ENDTIME%-%STARTTIME%
echo Duration: %DURATION%
echo Script Complete
echo.
PAUSE
