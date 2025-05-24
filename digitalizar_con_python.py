from PyPDF2 import PdfMerger

merger = PdfMerger()

N=2
for N in range (N,37,1):
	merger.append("'Escáner_20250524 ('+str(N)+').pdf'")

merger.write("ompleto.pdf")
merger.close()

print ("listo")


