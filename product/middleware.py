class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"Request path1: {request.path}, Method: {request.method}")
        response = self.get_response(request)
        return response
