from fpdf import FPDF

pdf = FPDF()

j = 1


pdf.add_page()
pdf.set_font('Arial',size=11)
for k in range(1,79):
 f = open(f"Program_{k}.cpp",'r')
 for i in f:
  pdf.cell(200, 10, txt = i,ln = j)
  j += 1
 pdf.output(f"program_{k}.pdf")

