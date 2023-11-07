from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView, DeleteView

from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from .models import Request
from .forms import CreateRequestForm

# Create your views here.
def index(request):
    return render (request, 'main/index.html')
    # requests_list = Request.objects.all()
    # return render(request, 'index.html', {'requests_list': requests_list})

def home(request):
    return render(request, 'main/home.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            fio = form.cleaned_data['fio']

            user = form.save()
            user.first_name = fio
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def login_v(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error_message('Неправильный логин или пароль.')
        else:
            form.add_error_message('Пожалуйста, исправьте ошибки в форме.')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

# class RequestsView(generic.ListView):
#     model = Request
#     paginate_by = 4



# def requestView(generic.ListView):
#     requests_list = Request.objects.all()  # Получение всех заявок
#     return render(request, 'index.html', {'requests_list': requests_list})

def logout_view(request):
    logout(request)  # Выход пользователя
    return redirect('index')

class ViewRequests(ListView):
   model = Request
   template_name = 'main/profile.html'
   context_object_name = 'requests'
   def get_queryset(self):
       return Request.objects.filter(user=self.request.user)

class ViewProcessRequests(ListView):
    model = Request
    template_name = 'main/index.html'
    context_object_name = 'requests'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_of_accepted_requests"] = Request.objects.filter(status__exact='Принято в работу').count
        return context



class CreateRequest(CreateView):
    model = Request
    template_name = 'main/create_requests.html'
    success_url = reverse_lazy('index')
    form_class = CreateRequestForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeleteRequest(DeleteView):
    model = Request
    template_name = 'main/delete_request.html'
    success_url = reverse_lazy('index')

class DeleteRequestFilter(DeleteView):
    model = Request
    template_name = 'main/delete_request.html'
    success_url = reverse_lazy('index')