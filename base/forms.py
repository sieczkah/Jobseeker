from django import forms

from .models import JobOffer


class JobOfferForm(forms.ModelForm):
    company_name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={"list": "companies-list"}),
    )

    class Meta:
        model = JobOffer
        fields = [
            "link",
            "posistion",
            "company_name",
            "description",
            "status",
            "salary",
        ]

    def __init__(self, *args, **kwargs):
        initial = kwargs.get("initial", {})
        if kwargs.get("instance"):
            initial["company_name"] = kwargs["instance"].company.name
        kwargs["initial"] = initial
        super(JobOfferForm, self).__init__(*args, **kwargs)
