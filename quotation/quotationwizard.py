from re import TEMPLATE
from traceback import format_list
from django.http import HttpResponseRedirect
from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from quotation.models import Quotation
from quotation.forms import *

TEMPLATES = {
    "":"quotation_wizard.html",
    "air_form": "quotation_wizard_air.html",
}

class QuotationWizard(SessionWizardView):
    form_list = [QuotationTypeForm]
    def get(self, request, *args, **kwargs):
        # if request.GET.get('next_step'):
        #     return HttpResponseRedirect(request.path)
        print("Treeeeee222222222")
        return super().get(request, *args, **kwargs)

    def get_template_names(self):
        return TEMPLATES[self.steps.current]

    def process_step(self, form):
        # This method is called for every step.
        # form is a form object.
        # You can do anything with it that you want.
        # The most important thing is to call .save() on it.
        # In this example, we use this method to modify the form
        # based on the previous step.
        import pdb; pdb.set_trace()
        form.save()
        return super().process_step(form)

    def done(self, form_list, **kwargs):
        # form_list is a list of forms on every step
        return render(self.request, 'quotation_list.html')