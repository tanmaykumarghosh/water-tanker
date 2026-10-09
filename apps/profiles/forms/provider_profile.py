from django import forms

from apps.accounts.models import User
from ..models import ProviderProfile
from django.utils import timezone

class ProviderProfileAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
        #if self.instance._state.adding:

            self.fields["first_name"].initial = self.instance.user.first_name
            self.fields["middle_name"].initial = self.instance.user.middle_name
            self.fields["last_name"].initial = self.instance.user.last_name
            self.fields["phone"].initial = self.instance.user.phone
            self.fields["email"].initial = self.instance.user.email

            self.fields["password"].required = False

    first_name = forms.CharField(max_length=100)

    middle_name = forms.CharField(
        max_length=100,
        required=False,
    )

    last_name = forms.CharField(
        max_length=100,
        required=False,
    )

    phone = forms.CharField(max_length=20)

    email = forms.EmailField(required=False)

    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        help_text="Leave blank to keep the current password."
    )

    class Meta:
        model = ProviderProfile
        exclude = ("user",)

    

    def save(self, commit=True):

        profile = super().save(commit=False)

        if self.instance._state.adding:

            user = User.objects.create_user(
                phone=self.cleaned_data["phone"],
                password=self.cleaned_data["password"],
                first_name=self.cleaned_data["first_name"],
                middle_name=self.cleaned_data["middle_name"],
                last_name=self.cleaned_data["last_name"],
                email=self.cleaned_data["email"],
                role=User.Role.PROVIDER,
            )

            profile.user = user

            # Only needed if your database doesn't provide defaults.
            profile.created_at = timezone.now()
            profile.updated_at = timezone.now()

        else:

            user = profile.user

            user.first_name = self.cleaned_data["first_name"]
            user.middle_name = self.cleaned_data["middle_name"]
            user.last_name = self.cleaned_data["last_name"]
            user.phone = self.cleaned_data["phone"]
            user.email = self.cleaned_data["email"]

            password = self.cleaned_data.get("password")
            if password:
                user.set_password(password)

            user.save()

            profile.updated_at = timezone.now()

        if commit:
            profile.save()

        return profile