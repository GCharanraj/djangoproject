from django.shortcuts import render

# Create your views here.
def func(request):
    a= request.POST.get('sname')
    return render(request,'index.html',{'res':a})


def func2(request):
    result=None
    if request.method=="GET":
        a=request.GET.get('num')
        print(type(a))
        b=len(str(a))
        sum=0
        temp = a
        while a > 0:
            n=a%10
            sum+=n**b
            a=a//10
        if sum == temp:
            result=True
        else:
            result=False
    return render(request,'armstrong.html',{'res':result})