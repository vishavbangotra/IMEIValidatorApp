from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView


# This method is to render the homepage
def HompageRender(request):
    return render(request, 'Index.html')

# This method handles the case when digit of the IMEI number is greater than 4
def sumOfTwo(n):
    sum = 0
    sum = n % 10
    n = int(n / 10)
    sum += n % 10
    return sum

# This method returns the sum of all the digits of the IMEI number, If invalid IMEI is entered it returns 0
def IMEICheck(number):
    s = str(number)
    l = len(s)
    if l != 15:
        return 0
    sum = 0
    it = 1
    for i in range(15, 0, -1):
        p = number % 10
        if it % 2 == 0:
            p *= 2
            sum += sumOfTwo(p)
        else:
            sum += p
        p /= 10
        it = it + 1
        number = int(number/10)
    return sum

# This method handles the case when IMEI is invalid and return the number by which we can change the last digit of IMEI to get a valid IMEI number
def IMEIBad(number, sum):
    n = number % 10
    s = sum % 10

    if n >= s:
        ans = n - s
    else:
        ans = n + 10 - s
    return ans

# This is the main API view
class IMEICheckView(APIView):
    def get(self, request, number):
        if IMEICheck(number) == 0:
            return JsonResponse({"Status":"Invalid input. IMEI needs to be 15 digit number"})
        if IMEICheck(number) % 10 == 0:    
            res = {
                "Status": str(number) + " is Valid IMEI"
            }
        else:
            res = {
                "Status":"Change the last digit of IMEI number to "+ str(IMEIBad(number, IMEICheck(number)))
            }
        return JsonResponse(res)