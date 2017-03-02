import os
import csv
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'var_db.settings'
django.setup()
from vars.models import *

genename = GeneName(GeneName = 'BRCA1')
genename.save()
print genename.GeneName

sequencer1=Sequencing(Sequencer="HiSeq")
sequencer2=Sequencing(Sequencer="MiSeq")
sequencer1.save()
sequencer2.save()

condition=Condition(Condition='Cancer')
condition.save()

class1 = Classification(Classification = '1')
class2 = Classification(Classification = '2')
class3 = Classification(Classification = '3')
class4 = Classification(Classification = '4')
class5 = Classification(Classification = '5')
class1.save()
class2.save()
class3.save()
class4.save()
class5.save()



with open('./BRCA1_Django_test_data.csv', 'r') as input:
	reader = csv.reader(input, delimiter=',')
	next(reader, None)
	for row in reader: 
		
		gene=GeneName.objects.get(GeneName="BRCA1")
		seq_plat=Sequencing.objects.get(Sequencer=row[4])		
		classif=Classification.objects.get(Classification=row[8])
		variant=Variant_Details(GeneName_ID=gene, Variant_cDNA=row[5], Variant_Protein=row[6], Variant_Genome=row[7],Platform=seq_plat,Class_ID=classif)
		variant.save()

		patient=Patient_Details(name=row[0],age=row[1]) 
		patient.save()
		

		variantid=Variant_Details.objects.latest('Variant_ID')
		patientid=Patient_Details.objects.latest('Patient_ID')
		table=Patient_Variant(Variant_ID=variantid,Patient_ID=patientid)
		table.save()


		 



