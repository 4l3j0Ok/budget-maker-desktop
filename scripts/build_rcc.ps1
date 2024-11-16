param (
  [string]$inputFile = ".\src\resources.qrc",
  [string]$outputFile = ".\src\resources_rc.py"
)

rcc -g python $inputFile -o $outputFile