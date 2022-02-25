import random
from collections import OrderedDict
from hashlib import sha1

from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _

from userena import settings as userena_settings
from userena.models import UserenaSignup
from userena.utils import get_profile_model

attrs_dict = {"class": "required"}

USERNAME_RE = r"^[\.\w]+$"


class SignupForm(forms.Form):
    """
    Form for creating a new user account.

    Validates that the requested username and e-mail is not already in use.
    Also requires the password to be entered twice.
    """

    username = forms.RegexField(
        regex=USERNAME_RE,
        max_length=30,
        widget=forms.TextInput(attrs=attrs_dict),
        label=_("Username"),
        error_messages={
            "invalid": _(
                "Username must contain only letters, numbers, dots and underscores."
            )
        },
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs=dict(attrs_dict, maxlength=75)),
        label=_("Email"),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
        label=_("Create password"),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
        label=_("Repeat password"),
    )

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already in use.
        Also validates that the username is not listed in
        ``USERENA_FORBIDDEN_USERNAMES`` list.

        """
        try:
            get_user_model().objects.get(
                username__iexact=self.cleaned_data["username"]
            )
        except get_user_model().DoesNotExist:
            pass
        else:
            if (
                userena_settings.USERENA_ACTIVATION_REQUIRED
                and UserenaSignup.objects.filter(
                    user__username__iexact=self.cleaned_data["username"]
                ).exclude(activation_key=userena_settings.USERENA_ACTIVATED)
            ):
                raise forms.ValidationError(
                    _(
                        "This username is already taken but not confirmed. "
                        "Please check your email for verification steps."
                    )
                )
            raise forms.ValidationError(_("This username is already taken."))
        if (
            self.cleaned_data["username"].lower()
            in userena_settings.USERENA_FORBIDDEN_USERNAMES
        ):
            raise forms.ValidationError(_("This username is not allowed."))
        return self.cleaned_data["username"]

    def clean_email(self):
        """Validate that the e-mail address is unique."""
        if get_user_model().objects.filter(
            email__iexact=self.cleaned_data["email"]
        ):
            if (
                userena_settings.USERENA_ACTIVATION_REQUIRED
                and UserenaSignup.objects.filter(
                    user__email__iexact=self.cleaned_data["email"]
                ).exclude(activation_key=userena_settings.USERENA_ACTIVATED)
            ):
                raise forms.ValidationError(
                    _(
                        "This email is already in use but not confirmed. "
                        "Please check your email for verification steps."
                    )
                )
            raise forms.ValidationError(
                _(
                    "This email is already in use. Please supply a different email."
                )
            )
        return self.cleaned_data["email"]

    def clean(self):
        """
        Validates that the values entered into the two password fields match.
        Note that an error here will end up in ``non_field_errors()`` because
        it doesn't apply to a single field.

        """
        if (
            "password1" in self.cleaned_data
            and "password2" in self.cleaned_data
        ):
            if (
                self.cleaned_data["password1"]
                != self.cleaned_data["password2"]
            ):
                raise forms.ValidationError(
                    _("The two password fields didn't match.")
                )
        return self.cleaned_data

    def save(self):
        """Creates a new user and account. Returns the newly created user."""
        username, email, password = (
            self.cleaned_data["username"],
            self.cleaned_data["email"],
            self.cleaned_data["password1"],
        )

        new_user = UserenaSignup.objects.create_user(
            username,
            email,
            password,
            not userena_settings.USERENA_ACTIVATION_REQUIRED,
            userena_settings.USERENA_ACTIVATION_REQUIRED,
        )
        return new_user


class SignupFormOnlyEmail(SignupForm):
    """
    Form for creating a new user account but not needing a username.

    This form is an adaptation of :class:`SignupForm`. It's used when
    ``USERENA_WITHOUT_USERNAME`` setting is set to ``True``. And thus the user
    is not asked to supply an username, but one is generated for them. The user
    can than keep sign in by using their email.

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields["username"]

    def save(self):
        """Generate a random username before falling back to parent signup form"""
        while True:
            username = sha1(str(random.random()).encode("utf-8")).hexdigest()[
                :5
            ]
            try:
                get_user_model().objects.get(username__iexact=username)
            except get_user_model().DoesNotExist:
                break

        self.cleaned_data["username"] = username
        return super().save()


class SignupFormTos(SignupForm):
    """Add a Terms of Service button to the ``SignupForm``."""

    tos = forms.BooleanField(
        widget=forms.CheckboxInput(attrs=attrs_dict),
        label=_("I have read and agree to the Terms of Service"),
        error_messages={
            "required": _("You must agree to the terms to register.")
        },
    )


def identification_field_factory(label, error_required):
    """
    A simple identification field factory which enable you to set the label.

    :param label:
        String containing the label for this field.

    :param error_required:
        String containing the error message if the field is left empty.

    """
    return forms.CharField(
        label=label,
        widget=forms.TextInput(attrs=attrs_dict),
        max_length=75,
        error_messages={"required": error_required},
    )


class AuthenticationForm(forms.Form):
    """A custom form where the identification can be a e-mail address or username."""

    identification = identification_field_factory(
        _("Email or username"),
        _("Either supply us with your email or username."),
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
    )
    remember_me = forms.BooleanField(
        widget=forms.CheckboxInput(),
        required=False,
        label=_("Remember me for %(days)s")
        % {"days": _(userena_settings.USERENA_REMEMBER_ME_DAYS[0])},
    )

    def __init__(self, *args, **kwargs):
        """
        A custom init because we need to change the label if no usernames
        are used
        """
        super().__init__(*args, **kwargs)
        # Dirty hack, somehow the label doesn't get translated without declaring
        # it again here.
        self.fields["remember_me"].label = _("Remember me for %(days)s") % {
            "days": _(userena_settings.USERENA_REMEMBER_ME_DAYS[0])
        }
        if userena_settings.USERENA_WITHOUT_USERNAMES:
            self.fields["identification"] = identification_field_factory(
                _("Email"), _("Please supply your email.")
            )

    def clean(self):
        """
        Checks for the identification and password.

        If the combination can't be found will raise an invalid sign in error.

        """
        identification = self.cleaned_data.get("identification")
        password = self.cleaned_data.get("password")

        if identification and password:
            user = authenticate(
                identification=identification, password=password
            )
            if user is None:
                raise forms.ValidationError(
                    _(
                        "Please enter a correct username or email and password. "
                        "Note that both fields are case-sensitive."
                    )
                )
        return self.cleaned_data


class ChangeEmailForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs=dict(attrs_dict, maxlength=75)),
        label=_("New email"),
    )

    def __init__(self, user, *args, **kwargs):
        """
        The current ``user`` is needed for initialisation of this form so
        that we can check if the email address is still free and not always
        returning ``True`` for this query because it's the users own e-mail
        address.

        """
        super().__init__(*args, **kwargs)
        if not isinstance(user, get_user_model()):
            raise TypeError(
                "user must be an instance of %s" % get_user_model().__name__
            )
        else:
            self.user = user

    def clean_email(self):
        """Validate that the email is not already registered with another user"""
        if self.cleaned_data["email"].lower() == self.user.email:
            raise forms.ValidationError(
                _("You're already known under this email.")
            )
        if (
            get_user_model()
            .objects.filter(email__iexact=self.cleaned_data["email"])
            .exclude(email__iexact=self.user.email)
        ):
            raise forms.ValidationError(
                _(
                    "This email is already in use. Please supply a different email."
                )
            )
        return self.cleaned_data["email"]

    def save(self):
        """
        Save method calls :func:`user.change_email()` method which sends out an
        email with an verification key to verify and with it enable this new
        email address.

        """
        return self.user.userena_signup.change_email(
            self.cleaned_data["email"]
        )


class EditProfileForm(forms.ModelForm):
    """Base form used for fields that are always required"""

    first_name = forms.CharField(
        label=_("First name"), max_length=30, required=False
    )
    last_name = forms.CharField(
        label=_("Last name"), max_length=30, required=False
    )

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        # Put the first and last name at the top
        new_order = [
            ("first_name", self.fields["first_name"]),
            ("last_name", self.fields["last_name"]),
        ]
        new_order.extend(list(self.fields.items())[:-2])
        self.fields = OrderedDict(new_order)

    class Meta:
        model = get_profile_model()
        exclude = ["user"]

    def save(self, force_insert=False, force_update=False, commit=True):
        profile = super().save(commit=commit)
        # Save first and last name
        user = profile.user
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()

        return profile


class ActivationForm(forms.Form):
    """Form for activating an account."""

    pass
