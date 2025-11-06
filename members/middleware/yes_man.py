from datetime import timedelta
from django.utils import timezone

class YesMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        cookie = request.COOKIES.get("yes_man")
        if cookie != "yes_man":
            expires = timezone.now() + timedelta(days=365)
            response.set_cookie(
                key="yes_man",
                value="yes_man",
                expires=expires,
                httponly=True,
                samesite="Lax",
            )

        return response
