from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from core.forms import SkinAssessmentForm
from core.models import UserProfile
# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def calculate_skin_type(answers):
    """
    answers: dict from SkinAssessmentForm.cleaned_data
    returns: (primary_skin_type, flags)
    """

    scores = {
        "oily": 0,
        "dry": 0,
        "combination": 0,
        "normal": 0,
        "sensitive": 0,
        "acne_prone": 0,
    }

    # 1. Skin feel after washing
    feel = answers.get("feel")

    if feel == "tight":
        scores["dry"] += 3
    elif feel == "shiny":
        scores["oily"] += 3
    elif feel == "tzone":
        scores["combination"] += 3
    elif feel == "comfortable":
        scores["normal"] += 3

    # 2. Oil production by midday
    if answers.get("oil_midday") == "yes":
        scores["oily"] += 2
    else:
        scores["dry"] += 1
        scores["normal"] += 1

    # 3. Breakouts frequency
    breakouts = answers.get("breakouts")

    if breakouts == "often":
        scores["acne_prone"] += 3
        scores["oily"] += 1
    elif breakouts == "sometimes":
        scores["acne_prone"] += 1

    # 4. Sensitivity check
    if answers.get("sting") == "yes":
        scores["sensitive"] += 3

    # 5. Determine primary skin type
    primary_skin_type = max(
        ["oily", "dry", "combination", "normal"],
        key=lambda skin: scores[skin]
    )

    flags = {
        "sensitive": scores["sensitive"] >= 2,
        "acne_prone": scores["acne_prone"] >= 2,
    }

    return primary_skin_type, flags


@login_required
def skin_assessment(request):
    if request.method == "POST":
        form = SkinAssessmentForm(request.POST)
        if form.is_valid():
            answers = form.cleaned_data

            skin_type, flags = calculate_skin_type(answers)

            profile, created = UserProfile.objects.get(user=request.user)
            profile.skin_type = skin_type
            profile.sensitive = flags["sensitive"]
            profile.acne_prone = flags["acne_prone"]
            profile.age_range = answers["age_range"]
            profile.gender = answers["gender"]

            profile.assessment_data = answers
            profile.save()

            return redirect("index")
    else:
        form = SkinAssessmentForm()

    return render(request, "core/skin_assessment.html", {"form": form})

def skin_type(request):
    if not request.user.is_authenticated:
        return redirect('login')

    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return redirect('skin_assessment')

    context = {
        'skin_type': profile.skin_type,
        'sensitive': profile.sensitive,
        'acne_prone': profile.acne_prone,
    }

    return render(request, 'core/skin_type.html', context)
