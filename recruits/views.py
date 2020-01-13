from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from .models import Recruit, Answer, Master, RecruitStatus, Question
from .forms import RecruitForm
from django.forms.models import modelformset_factory
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


class IndexView(TemplateView):
    template_name = 'recruits/index.html'


class RecruitCreateView(CreateView):
    form_class = RecruitForm
    model = Recruit

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        RecruitStatus.objects.create(recruit_id=self.object.id)
        return HttpResponseRedirect(self.get_success_url())


def answer_create(request, pk):
    extra = Question.objects.all()
    AnswerFormSet = modelformset_factory(Answer, fields=['question', 'answer'], extra=len(extra))
    form = AnswerFormSet(queryset=Question.objects.filter(question=True))

    if request.method == "POST":
        form = AnswerFormSet(request.POST, queryset=Question.objects.filter(question=True))

        if form.is_valid():
            answers = form.save(commit=False)
            for answer in answers:
                answer.recruit = Recruit.objects.get(pk=pk)
                answer.save()
        return redirect('index')

    return render(request, 'recruits/answer_form.html', {"form": form})


class MasterListView(ListView):
    context_object_name = "masters"
    model = Master


class RecruitListView(ListView):
    model = Recruit

    def get_context_data(self, **kwargs):
        status = RecruitStatus.objects.filter(status=False)
        context = []
        for i in status:
            recruit = Recruit.objects.get(pk=i.recruit.id)
            context.append(recruit)
        return {'context': context}


class RecruitDetailView(DetailView):
    context_object_name = 'recruit_detail'
    model = Recruit

    def get_object(self, queryset=None):
        return get_object_or_404(Recruit, pk=self.kwargs.get('id'))


class AnswerListView(ListView):
    context_object_name = 'answers'
    model = Answer

    def get_queryset(self, *args, **kwargs):
        return Answer.objects.filter(recruit__pk=self.kwargs['pk'])


class RecruitStatusUpdateView(UpdateView):
    fields = ("master", "status")
    model = RecruitStatus
    context_object_name = 'recruit'

    def form_valid(self, form):
        # masters = RecruitStatus.objects.get(master=self.kwargs["master"])
        # if len(masters) >= 3:
        form.save()

        # Sending email
        recruit = get_object_or_404(Recruit, pk=self.kwargs.get('pk'))
        email_address = recruit.email
        subject = "Education"
        message = "You are enrolled"
        from_email = settings.EMAIL_HOST_USER
        send_mail(message=message, subject=subject, from_email=from_email, recipient_list=[email_address], fail_silently=False)
        return super(RecruitStatusUpdateView, self).form_valid(form)

