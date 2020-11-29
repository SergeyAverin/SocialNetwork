from django.http import HttpResponse


class DebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(1)
        response = self.get_response(request)
        print(2)
        
        return response

    def process_exception(self, request, exception):
        print(exception)
        print(3)

        return HttpResponse(f"ERROR: {exception}")