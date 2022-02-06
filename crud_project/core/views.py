from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from authentication.models import Student, CustomUser
from school.models import Course

@method_decorator(login_required, name='dispatch')
class HomePageView(TemplateView):

    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context= {
                'courses': Course.objects.all(),
            }
        # curso = context['courses']
        # print(context['courses'].name)
        return context