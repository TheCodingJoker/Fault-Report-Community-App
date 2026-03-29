from django.shortcuts import render


def report_a_fault(request):
    return render(request, 'report_fault/report_a_fault.html')
