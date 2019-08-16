from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import  UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.messages import success
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from vote.forms import LoginForm, VotingForm
from vote.models import VoteCategory


@method_decorator(login_required, name='dispatch')
class IndexView(FormView):
    form_class = VotingForm
    template_name = 'index.html'
    success_url = reverse_lazy('vote:index')

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'categories' not in kwargs:
            kwargs['categories'] = VoteCategory.eligible_category(self.request.user)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        vote = form.save()
        success(self.request, f'You have successfully voted for {vote.candidate} for {vote.category.name}')
        return super().form_valid(form)

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
            'request': self.request
        }

        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs


class AuthLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse('vote:index')


class ResultView(UserPassesTestMixin, TemplateView):
    template_name = 'results.html'
    login_url = reverse_lazy('vote:index')

    def test_func(self):
        """ Results is only available to Admin or Staff"""
        return self.request.user.is_staff or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = {}
        for category in VoteCategory.objects.all():
            res = {}
            winner_count = 0
            winner = list()
            for candidate in category.candidates.all():
                candidate_count = category.votes.filter(candidate=candidate).count()
                if candidate_count > 0:
                    if candidate_count >= winner_count:
                        winner_count = candidate_count
                        winner += [candidate, ]
                res[candidate] = candidate_count
            results[category] = {'winner': winner, 'items': res}
        context['results'] = results
        return context


def test_flowcell(request):
    c = RequestContext(request, {'other_context':'details here'})
    if request.method == 'POST': # If the form has been submitted...
        form = ImportExcelForm(request.POST,  request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            excel_parser= ExcelParser()
            success, log  = excel_parser.read_excel(request.FILES['file'] )
            if success:
                return redirect(reverse('admin:index') + "pages/flowcell_good/") ## redirects to aliquot page ordered by the most recent
            else:
                errors = '* Problem with flowcell * <br><br>log details below:<br>' + "<br>".join(log)
                c['errors'] = mark_safe(errors)
        else:
            c['errors'] = form.errors 
    else:
        form = ImportExcelForm() # An unbound form
    c['form'] = form
    return render_to_response('sequencing/file_upload.html')
