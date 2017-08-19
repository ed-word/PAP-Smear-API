import pickle
import os
from django.conf import settings
import numpy as np

Classifier = pickle.load(open(os.path.join(settings.PROJECT_ROOT, 'pickle/svm_pickle.p'), "rb" ))

def predict(hgb, wbclab, age, smoking, nonveg, OccupationType):

	age = int(age)
	smoking = int(smoking)
	nonveg = int(nonveg)
	OccupationType = int(OccupationType)

	smoking_1 = 0
	smoking_3 = 0
	if smoking==1:
		smoking_1=1
	else:
		smoking_3=1

	nonveg_0 = 0
	nonveg_1 = 0
	nonveg_2 = 0
	if nonveg==0:
		nonveg_0=1
	elif nonveg==1:
		nonveg_1=1
	else:
		nonveg_2=1

	OccupationType_9 = 0
	OccupationType_10 = 0
	OccupationType_15 = 0
	if OccupationType==9:
		OccupationType_9=1
	elif OccupationType==10:
		OccupationType_10=1
	else:
		OccupationType_15=1

	arr = np.array([hgb, wbclab, age, smoking_1,smoking_3, nonveg_0,nonveg_1,nonveg_2, OccupationType_9,OccupationType_10,OccupationType_15])
	arr = arr.reshape((1,-1))
	return str(int(Classifier.predict(arr)))