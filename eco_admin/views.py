from django.shortcuts import render

# Create your views here.
def admin_index(request):
    return render(request,'ecoadmin_templates/admin_index.html')

def approve(request):
     return render(request,'ecoadmin_templates/Approve.html')   

# def views_seller(request):
#     return render(request,'ecoadmin_templates/viewsellers.html')