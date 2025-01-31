from django.http import JsonResponse
from django.utils.timezone import now

def api_info(request):
    data = {
        "email": "cecilmutero66@gmail.com",
        "current_datetime": now().isoformat(),
        "github_url": "https://github.com/CeciliaMutero",
    }
    return JsonResponse(data)
