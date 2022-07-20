from re import TEMPLATE
from traceback import format_list
from django.http import HttpResponseRedirect
from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from quotation.models import Quotation
from quotation.forms import *
import snoop


TEMPLATES = {
    "0":"quotation_wizard.html",
    "1": "quotation_wizard_air.html",
}

class QuotationWizard(SessionWizardView):
    form_list = [QuotationTypeForm,Quotation_Air]
    def get(self, request, *args, **kwargs):
        # if request.GET.get('next_step'):
        #     return HttpResponseRedirect(request.path)
        return super().get(request, *args, **kwargs)


    def get_template_names(self):
        print(self.steps.current)
        return TEMPLATES[self.steps.current]

    def get_form_initial(self, step):
        # This method is used to initialize the form fields with some
        # useful information.
        if step == '0':
            return {'owner': self.request.user}
        return super().get_form_initial(step)

    def process_step(self, form):
        # This method is called for every step.
        # form is a form object.
        # You can do anything with it that you want.
        # The most important thing is to call .save() on it.
        # In this example, we use this method to modify the form
        # based on the previous step.
        form.save()

        print("process step:"+self.steps.current)
        return super().process_step(form)

    def done(self, form_list, **kwargs):
        # form_list is a list of forms on every step
        return render(self.request, 'quote_list.html')