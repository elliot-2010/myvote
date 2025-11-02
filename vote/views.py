from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Candidate, Vote
from django.db.models import Count
# Create your views here.
def index(request):
    candidates = Candidate.objects.all()
    return render(request, "vote/index.html", {"candidates":candidates})
def submit_vote(request):
    if request.method == "POST":
        voter_name = request.POST.get("voter_name", "").strip()
        candidate_id = request.POST.get("candidate")

        if not voter_name or not candidate_id:
            # فیلدها خالی بودن → برگرد به صفحه اصلی
            return redirect("vote:index")

        try:
            candidate = Candidate.objects.get(id=candidate_id)
        except Candidate.DoesNotExist:
            return redirect("vote:index")

        # ایجاد رکورد جدید
        Vote.objects.create(voter_name=voter_name, candidate=candidate)
        return redirect("vote:stats")  # 👈 بعد از رأی به صفحه آمار برو

    return redirect("vote:index")
def stats(request):
    counts = Candidate.objects.annotate(votes_count=Count('votes')).order_by('-votes_count')
    return render(request, 'vote/stats.html', {'counts': counts})

def stats_data(request):
    # بازگرداندن JSON برای نمودار
    qs = Candidate.objects.annotate(votes_count=Count('votes')).order_by('-votes_count')
    labels = [c.name for c in qs]
    data = [c.votes_count for c in qs]
    return JsonResponse({'labels': labels, 'data': data})