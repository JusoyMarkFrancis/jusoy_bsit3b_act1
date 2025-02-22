from django.shortcuts import render

def index(request):
    return render(request, "pages/dashboard.html")

def reports(request):
    return render(request, "pages/reports.html")

def settings(request):
    return render(request, "pages/settings.html")


#Sample Data
data = [
    {"title": "Users", "count": 100},
    {"title": "Orders", "count": 328},
    {"title": "Revenue", "count": 955},
]

#View function
def dashboard(request):
    return render(request, 'pages/dashboard.html', {'data': data})