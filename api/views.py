from django.http import JsonResponse


def api_overview(request):
    return JsonResponse("Api start point", safe=False)
