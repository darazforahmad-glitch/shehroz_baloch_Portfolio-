"""Contact form. Validated server-side; no database writes."""

from django import forms


class ContactForm(forms.Form):
    """Fields are rendered manually in the template, so widget attrs here
    only cover behaviour the browser needs (type, autocomplete, limits)."""

    name = forms.CharField(
        max_length=120,
        error_messages={"required": "Please tell me your name."},
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your name",
                "autocomplete": "name",
                "maxlength": "120",
            }
        ),
    )
    email = forms.EmailField(
        max_length=200,
        error_messages={
            "required": "An email address is needed so I can reply.",
            "invalid": "That email address doesn't look right.",
        },
        widget=forms.EmailInput(
            attrs={
                "placeholder": "you@company.com",
                "autocomplete": "email",
                "maxlength": "200",
            }
        ),
    )
    subject = forms.CharField(
        max_length=160,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "What is this about? (optional)",
                "maxlength": "160",
            }
        ),
    )
    message = forms.CharField(
        max_length=4000,
        error_messages={"required": "Please add a short message."},
        widget=forms.Textarea(
            attrs={
                "placeholder": "Tell me a little about the role or project...",
                "rows": "5",
                "maxlength": "4000",
            }
        ),
    )
    # Honeypot: bots fill every field, humans never see this one.
    company_website = forms.CharField(required=False, widget=forms.HiddenInput())

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if len(message) < 10:
            raise forms.ValidationError(
                "That message is very short -- please add a little more detail."
            )
        return message

    def clean_name(self):
        return self.cleaned_data["name"].strip()

    @property
    def looks_like_spam(self) -> bool:
        """True when the honeypot field was filled in.

        Checked only after `is_valid()`; the view then returns the normal
        success response without sending anything, so a bot learns nothing.
        """
        return bool(self.cleaned_data.get("company_website"))
