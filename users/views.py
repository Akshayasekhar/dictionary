from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



def index(request):
    return render(request, 'index.html')

simple_detail=[
    {
        "id" : "1",
        "name":"Akshaya",
        "image":"fdghj.jpg"
    },

    {
        "id" : "2",
        'name': 'John Doe',
        'image': 'john.jpg',
    },
    {
         "id": "3",
         'name': 'Jane Smith',
        'image': 'jane.jpg',
    }

]

advanced_detail = [
    {
        'id':1,
        'f_name': 'akshaya',
        'l_name': 'p',
        'contact': '123-456-7890',
        'email': 'akshaya@example.com',
        'image': 'fgh.jpg',
    },
    {
        'id':2,
        'f_name': 'John',
        'l_name': 'Doe',
        'contact': '123-456-7890',
        'email': 'john.doe@example.com',
        'image': 'john.jpg',
    },
    {
        'id':3,
        'f_name': 'Jane',
        'l_name': 'Smith',
        'contact': '987-654-3210',
        'email': 'jane.smith@example.com',
        'image': 'jane.jpg',
    }
    ]
# @csrf_exempt
# def employee_detail(request, id=None):
#     if id:
#         # If an 'id' parameter is provided in the URL, retrieve the advanced detail.
#         for item in advanced_detail:
#             if item['id'] == id:
#                 return JsonResponse(item)
#     else:
#         # If no 'id' parameter is provided, return all simple details.
#         return JsonResponse(simple_detail, safe=False)
#
#     # If no matching item was found with the given 'id'.
#     return HttpResponse("Not found")
@csrf_exempt
def employee_detail(request,id=None):
    person = None
    if id:
       for item in advanced_detail:
         if item['id'] == id:
            person = item
            break

       if person:
        return JsonResponse(person)
       else:
        return HttpResponse("not found")
    else:
      return JsonResponse(simple_detail, safe=False)


# @csrf_exempt
# def simple_details(request):
#     return JsonResponse(simple_detail, safe=False)