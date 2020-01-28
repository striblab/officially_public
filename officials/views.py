from django.shortcuts import render
from django.views.generic import ListView, DetailView

from officials.models import Agency, Position, PublicOfficial

class AgencyList(ListView):
    model = Agency


class AgencyDetail(DetailView):
    context_object_name = 'agency'
    queryset = Agency.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['distinct_positions'] = self.get_object().position_set.all().values('Title').distinct()

        context['officials'] = PublicOfficial.objects.filter(positions__AgencyNo=self.object).distinct().order_by('POLastName', 'POFirstName')
        return context


class PublicOfficialDetail(DetailView):
    context_object_name = 'public-official'
    queryset = PublicOfficial.objects.all()
