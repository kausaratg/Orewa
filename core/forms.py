from django import forms


class SkinAssessmentForm(forms.Form):

    AGE_RANGES = [
        ("under_18", "Under 18"),
        ("18_24", "18–24"),
        ("25_34", "25–34"),
        ("35_44", "35–44"),
        ("45_plus", "45+"),
    ]

    GENDERS = [
        ("female", "Female"),
        ("male", "Male"),
        ("other", "Other / Prefer not to say"),
    ]

    age_range = forms.ChoiceField(
        choices=AGE_RANGES,
        widget=forms.RadioSelect,
        label="Age range"
    )

    gender = forms.ChoiceField(
        choices=GENDERS,
        widget=forms.RadioSelect,
        label="Gender"
    )

    # existing fields ↓
    FEEL_CHOICES = [
        ("tight", "Tight / flaky"),
        ("comfortable", "Comfortable"),
        ("shiny", "Very shiny"),
        ("tzone", "Shiny in T-zone only"),
    ]

    feel = forms.ChoiceField(choices=FEEL_CHOICES, widget=forms.RadioSelect)
    oil_midday = forms.ChoiceField(
        choices=[("yes", "Yes"), ("no", "No")],
        widget=forms.RadioSelect
    )
    breakouts = forms.ChoiceField(
        choices=[("rare", "Rarely"), ("sometimes", "Sometimes"), ("often", "Often")],
        widget=forms.RadioSelect
    )
    sting = forms.ChoiceField(
        choices=[("yes", "Yes"), ("no", "No")],
        widget=forms.RadioSelect
    )
