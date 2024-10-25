@echo off
setlocal ENABLEDELAYEDEXPANSION

rem (C)2024, Jack Hwang, All Rights Reserved
rem
rem This DOS batch file uses ImageMagicK command "convert" to
rem    convert image files into PDF files.  Two caveats:
rem    1. It assume image filenames are in "000xxx.ext"
rem       format, e.g., 000100.jpg or 000201.png
rem    2. It does not include other pages with different
rem       prefixes, e.g., forward pages such as fow001.jpg.
rem       Please use the convert command to create their own
rem       respective PDF files.
rem    3. It handles up 0-999 pages. If there are more pages,
rem       please modify the script accordingly.
rem    4. If pages are not available, it will still try to
rem       convert but it won't generate the pdf file.  For
rem       example, if a book has only 400 pages, it will
rem       still try to convert 401~999 pages but there will
rem       not be respective pdf files generated.

set loop=0,1,2,3,4,5,6,7,8,9
set num1=0,1,2,3,4
set num2=5,6,7,8,9

for /L %%i in (0,1,8) do (
   set var=
   for %%j in (%num1%) do set var=!var! 000%%i%%j*
   rem echo !var!
   echo convert !var! book%%i_1.pdf
   convert -quiet !var! book%%i_1.pdf 2> nul
   set var=
   for %%j in (%num2%) do set var=!var! 000%%i%%j*
   rem echo !var!
   echo convert !var! book%%i_2.pdf
   convert -quiet !var! book%%i_2.pdf 2> nul
)