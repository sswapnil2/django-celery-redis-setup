from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_celery.celery import fib


@api_view(["POST"])
def get_fib(request):
    if request.method == "POST":
        number = int(request.data.get("number", 50))
        task = fib.delay(number)
        return Response({
            "message": f"POST successful {task.id}"
        }, status=status.HTTP_200_OK)