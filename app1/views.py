from django.shortcuts import render
from app1.models import Student

def test(request):
    results = Student.objects.all()
    for record in results:
        print(record)
    context = {
        "students": results
    }
    return render(request, 'app1/students.html', context)


def index(request):
    context = {
        "employees": [
            {
                "first_name": "Ram",
                "last_name": "Kulkarni"
            },
            {
                "first_name": "Emp1 First Name",
                "last_name": "Emp2 Last Name"
            }
        ]
    }
    return render(request, 'app1/index.html', context)
