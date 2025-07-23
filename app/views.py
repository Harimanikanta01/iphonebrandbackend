import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pickle

@csrf_exempt  # Only for development or testing; not safe for production without protection
def Main1(request):
    if request.method == 'POST':
        # Load the trained model
        model = pickle.load(open(r'C:\Users\ADMIN\Desktop\iph\my\app\iphonefinal01', 'rb'))

        try:
            # Read and parse JSON body
            data = json.loads(request.body)

            # Extract and convert values
            brand = int(data.get('brand'))
            battery = float(data.get('battery'))
            screen = int(data.get('screen'))
            years = float(data.get('years'))

            # Run prediction
            prediction = model.predict([[brand, battery, screen, years]])
            result = int(prediction[0])

            return JsonResponse({"predicted": result})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Only POST requests allowed"}, status=405)
