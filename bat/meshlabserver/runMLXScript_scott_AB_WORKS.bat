@echo OFF
@title MultiMesh Scripting
cls

echo.
echo MultiMesh Scripting - Run a MLX Script on a Folder v1.0
echo ----------------------------------------------------------------

::Switch to the MultiMesh program's working directory
C:
cd C:\multiMeshScripting

::Input Mesh File variables
@set inputFolder=input
::Note: You can choose a specific mesh format for input or
::use an asterix (*) for all files in the input meshes folder
::@set inputMeshFormat=obj
@set inputMeshFormat=stl
::@set inputMeshFormat=*


::Output Mesh File variables
@set outputFolder=output
@set outputMeshFormat=stl
::@set outputMeshFormat=ply
::Note: If you use the PLY output format it is saved as a BINARY PLY file
::@set outputMeshFormat=u3d

::MLX script file variables
::the MLX scripts are stored in the C:\multiMeshScripting\scripts folder
::@set mlxScriptFile=reduce_90.mlx
@set mlxScriptFolder=scripts
@set mlxScriptFile="C:\multiMeshScripting\scripts\reduce_90.mlx"

::OM Output Mesh Options
::These options specify what data types are exported by meshlabserver
@set outputMeshOptions=
::The standard om options are "-om vc fq wn" which give vertex colors, face colors, and wedge normals

::The available OM options are:
::vc -> vertex colors           ::vf -> vertex flags
::vq -> vertex quality          ::vn-> vertex normals
::vt -> vertex texture coords   ::fc -> face colors
::ff -> face flags              ::fq -> face quality
::fn-> face normals             ::wc -> wedge colors
::wn-> wedge normals            ::wt -> wedge texture coords

::The meshlabserver program location:
::@set meshlabserverPath="C:\Program Files\VCG\MeshLab\meshlabserver.exe"
@set meshlabserverPath= meshlabserver

::------------------------------------------------------
::      List the Current Input Mesh Format
::------------------------------------------------------
echo ----------------------------------------------------------------
echo Processing meshes with the format:
echo %inputMeshFormat%

::------------------------------------------------------
::           List the input Meshes
::------------------------------------------------------

echo ----------------------------------------------------------------
echo Input Folder Mesh List:
for %%X in (%inputFolder%\*.%inputMeshFormat%) do (echo "%%X")
::To get help on the "for" syntax use: for /?
echo.

echo ------------------------------------------------------
echo   Run a meshlabserver MLX script on a folder
echo ------------------------------------------------------

::Example syntax that is used inside the for loop: 
::"C:\Program Files\VCG\MeshLab\meshlabserver.exe" -i input\boulder-mini1.ply -o output\boulder-mini1.ply -s scripts\simple_script.mlx -om vc fq wn

::Run the "for" loop from inside the input folder
cd %inputFolder%

for %%I in (*.%inputMeshFormat%) do ( %meshlabserverPath% -i %%I -o ..\%outputFolder%\%%~nI.%outputMeshFormat% -s %mlxScriptFile% %outputMeshOptions%
timeout /t 2 )
::To get help on the "for" syntax use: for /?

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

::------------------------------------------------------
::           Done Processing
::------------------------------------------------------

echo. 
echo Script Complete
echo.
PAUSE