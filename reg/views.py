from django.shortcuts import render,redirect
from reg.form import Student_creation_form
# Create your views here.


def home(request):
    return render(request, 'reg/home.html')



def create_st(request):
    form = Student_creation_form()
    if request.method == 'POST':
        form = Student_creation_form(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'reg/stud_creation_form.html', context)



# def group_csv(requst):
#     response=HttpResponse(content_type ='text/csv')
#     response['Content-Disposition']= 'attachmet; filename=venuev.csv'
#     # create a csv writer
#     writer = csv.writer(response)
#     # desain the model
#     group = Groupss.objects.all()

#     # add column headings to the csv file
#     writer.writerow(['Group_name', 'Member1', 'Member2', 'Email M1','Email M2', 'Ph No M1', 'Ph No M2'])
#     for team in group:
#         writer.writerow([team.g_name, team.cn1, team.cn2, team.cn1em, team.cn2em, team.cn1ph, team.cn2ph, team.clg_name])
#     return response

# def group_csv_m(request):
#     response=HttpResponse(content_type ='text/csv')
#     response['content-disposition']='attachmet; filename=members.csv'

#     writer = csv.writer(response)

#     group = Groupss.objects.all()

#     writer.writerow(['Name','colleg','phone number', 'Emal'])
#     for team in group:
#         writer.writerow([team.cn1, team.clg_name, team.cn1ph, team.cn1em])
#         writer.writerow([team.cn2, team.clg_name, team.cn2ph, team.cn2em])
#     return response 


# def groups(request):
#     ls = Groupss.objects.all().order_by('-id')
    
#     filter = GroupFilter(request.GET,queryset=ls)
#     ls = filter.qs
#     context = {'ls' : ls,
#         'filter':filter    
#     }
#     return render(request, 'regi/full_lst.html',context)

# def detail(request,groupss_id):
#     # from django.shortcuts import get_object_or_404, render
#     # question = get_object_or_404(Question, pk=question_id)
#     try:
#         it = Groupss.objects.get(pk=groupss_id)
#     except:
#         raise Http404("Group does not exist")
#     return render(request,'regi/detail.html', {'it': it})
    
# 

# def updategroup(request,pk):
#     group = Groupss.objects.get(id=pk)
#     form = GroupForm(instance=group)

#     if request.method == 'POST':
#         form = GroupForm(request.POST,instance=group)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {'form':form}
#     return render(request,'regi/gp_c_form.html', context)


# def deletegroup(request,pk):
#     group = Groupss.objects.get(id=pk)
#     if request.method =='POST':
#         group.delete()
#         return redirect('/')
#     context = {'group':group}
#     return render(request,'regi/delete.html',context)
