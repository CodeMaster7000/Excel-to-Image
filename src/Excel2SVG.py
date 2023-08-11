workbook = Workbook("Book1.xlsx") # Input workbook here.
imgOptions = ImageOrPrintOptions()
imgOptions.setSaveFormat(SaveFormat.SVG)
sheetCount = workbook.getWorksheets().getCount()
for i in range(0, sheetCount):
	sheet = workbook.getWorksheets().get(i)
	sr = SheetRender(sheet, imgOptions)
	for j in range(0, sr.getPageCount()):
	  sr.toImage(j, sheet.getName() + "%s" % j + "_output.svg") # Converts each sheet to an SVG.
