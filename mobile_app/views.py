from django.shortcuts import render, reverse, get_object_or_404, HttpResponseRedirect,redirect
from .models import Mobile
from .forms import MobileForm
from django.views import generic
from django.contrib import messages

# Create your views here.

#class MobileListView(generic.ListView):
 #   template_name = 'mobile_list.html'
  #  queryset = Mobile.objects.all()

def index(request):
    mobile_list = Mobile.objects.all()
    dict = {'mobile_list':mobile_list}
    return render(request, 'mobile_list.html', context=dict)





def mobile_create(request):
    form = MobileForm()

    if request.method == 'POST':
        form = MobileForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)


    dict = {'form': form}
    return render(request, 'mobile_create.html', context=dict)


def delete_mobile(request, pk):
    mobile = Mobile.objects.get(id=pk)
    if request.method == 'POST':
       mobile.delete()
       return redirect('mobile_list')

    return render(request, 'delete.html')


#class MobileDeleteView(generic.DeleteView):
 #   template_name = 'delete.html'
#
 #   def get_object(self):
  #      id = self.kwargs.get('id')
   #     return get_object_or_404(Mobile, id=id)
#
 #   def get_success_url(self):
  #      messages.success(self.request, ('This Mobile model is Deleted!!'))
   #     return HttpResponseRedirect('mobile_list')



