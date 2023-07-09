from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Text

def get_texts(request):
    texts = Text.objects.all()
    if texts:
        data = [text.content for text in texts]
        return JsonResponse({'data': data})
    else:
        return JsonResponse({'text': 'Its Empty'})

def get_text(request):
    text = Text.objects.first()
    if text:
        return JsonResponse({'text': text.content})
    else:
        return JsonResponse({'text': 'No Data from db'})
    


@csrf_exempt
def text_view(request):
    if request.method == 'POST':
        data = request.POST.getlist('text')
        # Assuming your model is named 'Text' with a 'content' field
        for item in data:
            Text.objects.create(content=item)
        return JsonResponse({'message': 'Data received and written to database.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'})
