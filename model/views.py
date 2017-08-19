from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect


from .models import SVM_model
from .serializers import SVM_model_serializer

from .forms import FeatureForm
from .Classifier import predict

from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from rest_framework.response import Response

from rest_framework.renderers import JSONRenderer

def formmm(request):
    if request.method == "POST":
        form = FeatureForm(request.POST)
        if form.is_valid():
            mod = form.save(commit=False)
            mod.save()
            return redirect('model_view',pk=mod.pk)
    else:
        form = FeatureForm()
    return render(request, 'model/form.html', {'form': form})

def model_view(request,pk):
    model = SVM_model.objects.get(pk=pk)
    attr = predict(float(model.Haemoglobin), float(model.WBC), int(model.Age), int(model.Smoking), int(model.Nonveg), int(model.OccupationType))
    setattr(model, "FI_FDiagnosis", attr)
    return render(request, 'model/model_view.html', {'model': model})





@api_view()
@renderer_classes((JSONRenderer,))
def predict_out(request, hgb, wbc, age, smk, nveg, occ):

	hgb = float(hgb)
	wbc = float(wbc)
	age = int(age)
	smk = int(smk)
	nveg = int(nveg)
	occ = int(occ)

	model = SVM_model.objects.create(Haemoglobin=hgb, WBC=wbc, Age=age, Smoking=smk, Nonveg=nveg, OccupationType=occ)

	attr = predict(float(model.Haemoglobin), float(model.WBC), int(model.Age), int(model.Smoking), int(model.Nonveg), int(model.OccupationType))
	setattr(model, "FI_FDiagnosis", attr)
	
	serializer_output = SVM_model_serializer(model)
	return Response(serializer_output.data)

#http://127.0.0.1:8000/api/input/hgb=12.3/wbc=12.0/age=44/smk=1/nveg=1/occ=15