from PyPDF2 import PdfMerger

merger = PdfMerger()

N=2
for N in range (N,37):
	archivo = f"Escáner_20250524 ({N}).pdf"
	merger.append(archivo)

merger.write("ompleto.pdf")
merger.close()

print ("listo")


