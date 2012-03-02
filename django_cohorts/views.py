from django.views.generic.simple import direct_to_template
from django_cohorts.analysis import CohortAnalysis
def cohort_analysis(request):
    if request.method == 'POST':
        form = CohortAnalysisForm(request.POST)
        if form.is_valid():
            pass# Do something to change the analysis shown
    analysis = CohortAnalysis()
    cohorts = analysis.get_cohorts()
    variables = {
        "analysis": analysis,
        "cohorts":cohorts,
    }
    return direct_to_template(request, 'cohorts/cohort_analysis.html', variables)
