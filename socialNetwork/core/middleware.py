from django.http import HttpResponse


class DebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        return response

    def process_exception(self, request, exception):
        print(f"ERROR: {exception}")

        return HttpResponse(f"ERROR: {exception}")
