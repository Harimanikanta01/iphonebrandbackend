from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pickle
import os

@csrf_exempt
def Main1(request):
    if request.method == 'POST':
        # Load model using relative path (works on Render)
        model_path = os.path.join(os.path.dirname(__file__), 'iphonefinal01')
        model = pickle.load(open(model_path, 'rb'))

        # Get POST values
        brand = request.POST.get('brand')
        battery = float(request.POST.get('battery'))
        screen = int(request.POST.get('screen'))
        years = int(request.POST.get('years'))

        # Prepare input & predict
        input_data = [[brand, battery, screen, years]]
        prediction = model.predict(input_data)

        return HttpResponse(str(prediction[0]))
    else:
        return HttpResponse("Only POST allowed", status=405)
