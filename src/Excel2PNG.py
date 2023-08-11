workbook = Workbook("Book1.xlsx") # Input Excel Workbook here.
imgOptions = ImageOrPrintOptions()
imgOptions.setSaveFormat(SaveFormat.SVG)
sheet = workbook.getWorksheets().get(0)
sr = SheetRender(sheet, imgOptions)
for i in range(0, sr.getPageCount()):
	sr.toImage(i, "Worksheet2PNG-output%s" %(j) + ".png") # Converts sheet to PNG image
