from django.utils import timezone

from django.shortcuts import render

# Create your views here.
def dtl_demo(request):
    context = {
        "my_name": "David",
        "courses": ["Python", "Django"],
        "age": 100,
        "is_logged_in": False,
        "today": timezone.now(),
        "grades": {
            "Math": 90,
            "English": 100,
            "Chemistry": 89,
            "Biology": 89
        }
    }
    return render(request, "dtl/dtl.html", context)