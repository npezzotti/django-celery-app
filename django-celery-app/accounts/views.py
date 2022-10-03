from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    success_message = "Account successfully created! Run 'docker logs celery-worker' to view the welcome email sent as a celery task."
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)