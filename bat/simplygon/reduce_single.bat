::C:\Users\Scott\Desktop\1

::SET path

::for /f %%f in ('dir /b C:\Users\Scott\Desktop\1') do SimplygonBatch.exe --SPL "C:\Users\Scott\Desktop\test.spl" --input %%f --output "C:\Users\Scott\Desktop\output" --verbose

::echo %%f

SimplygonBatch.exe --SPL "C:\Users\Scott\Desktop\test.spl" --input "C:\Users\Scott\Desktop\1" --output "C:\Users\Scott\Desktop\output" --verbose
