from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pickle
import os
import json

@csrf_exempt
def Main1(request):
    if request.method == 'POST':
        try:
            model_path = os.path.join(os.path.dirname(__file__), 'iphonefinal01')  # or 'iphonefinal01.pkl'
            model = pickle.load(open(model_path, 'rb'))

            # Try JSON payload first
            try:
                data = json.loads(request.body)
                brand = data.get('brand')
                battery = float(data.get('battery'))
                screen = int(data.get('screen'))
                years = int(data.get('years'))
            except:
                # Fallback to form data
                brand = request.POST.get('brand')
                battery = float(request.POST.get('battery'))
                screen = int(request.POST.get('screen'))
                years = int(request.POST.get('years'))

            input_data = [[brand, battery, screen, years]]
            prediction = model.predict(input_data)
            return JsonResponse({'predicted_price': prediction[0]})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Only POST method allowed'}, status=405)
