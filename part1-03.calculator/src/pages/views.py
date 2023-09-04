from django.http import HttpResponse

# Create your views here.
# A request to the path add/ sums the values in the request GET parameters first and second together and 
# returns the response to the user. Note that the parameters are integers and should also be treated as such.
def addPageView(request):
    firstValue = int(request.GET.get('first'))
    secondValue = int(request.GET.get('second'))
    sum = str(firstValue + secondValue)
    return HttpResponse(sum)
	
# # A request to the path multiply/ multiplies the values in the request GET parameters first and second 
# # and returns the response to the user. Note that the parameters are numbers and should also be treated as such.
def multiplyPageView(request):
    firstValue = int(request.GET.get('first'))
    secondValue = int(request.GET.get('second'))
    multiplication = str(firstValue * secondValue)
    return HttpResponse(multiplication)
