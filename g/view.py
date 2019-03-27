from django.http import HttpResponse
# NUMEBER IS USED TOGET A INT VALUE FROM URL
def homePageView(request,number):

    n = int(number)
    a = ''

    if n > 1:

        # Iterate from 2 to n / 2
        for i in range(2, n // 2):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (n % i) == 0:
                  a = "is not a prime number"
                  #{} IS USED FOR ASSSING n VALUE TO DISPLAY
                  #.FORMATE IS IMPORTANT
                  return HttpResponse('{}{}'.format(n, a))
                  break

        else:
            a = "is a prime number"
        return HttpResponse('{}{}'.format(n, a))



    else:
        a = "is not a prime number"
        return HttpResponse('{}{}'.format(n, a))



