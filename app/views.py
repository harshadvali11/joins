from django.shortcuts import render

# Create your views here.
from app.models import *
def emp_join(request):
    #Displaying the details of emp and dept tables
    QLTO=Emp.objects.select_related('DEPTNO').all()
    
    #Displaying the details of emp and dept tables of deptno10
    QLTO=Emp.objects.select_related('DEPTNO').filter(DEPTNO=10)
    
    #Displaying the details of emp and dept tables of dNAME OPERATIONS
    QLTO=Emp.objects.select_related('DEPTNO').filter(DEPTNO__DNAME='OPERATIONS')
    
    #Displaying the details of emp and dept tables of dNAME OPERATIONS AND JOB IS SALESMAN
    QLTO=Emp.objects.select_related('DEPTNO').filter(DEPTNO__DNAME='OPERATIONS',JOB='SALESMAN')
    
    #Displaying the details of emp and dept tables of dNAME OPERATIONS AND comm is null

    QLTO=Emp.objects.select_related('DEPTNO').filter(DEPTNO__DNAME='OPERATIONS',COMM__isnull=True)
    
    QLTO=Emp.objects.select_related('DEPTNO').filter(COMM__isnull=False)
    
    QLTO=Emp.objects.select_related('DEPTNO').all()    
    d={'QLTO':QLTO}
    return render(request,'emp_join.html',d)


def self_joins(request):
    EANDM=Emp.objects.prefetch_related('emp_set').filter(MGR__isnull=False)
    d={'EANDM':EANDM}
    return render(request,'self_joins.html',d)
















