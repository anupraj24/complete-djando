from django.http import request
from django.shortcuts import render,HttpResponse
from poll.models import Question, Choice


#poll view..


def poll_view(request, pk):

    try:
        que = Question.objects.get(id=pk)
        choices = Choice.objects.filter(question=que)

        if request.method == "POST":
            selected_choice_id = request.POST.get("choice")
            selected_choice = Choice.objects.get(id=selected_choice_id)
            selected_choice.vote_count = selected_choice.vote_count + 1
            selected_choice.save()
            return render(
                request,
                "poll.html",
                {
                    "selected_choice": selected_choice,
                    "submitted": True,
                    "question": que,
                    "choices": choices,
                },
            )

    except:
        return render(request, "404.html")

    return render(
        request, "poll.html", {"submitted": False, "question": que, "choices": choices}
    )



# home page....
def home_view(request):
    ques = Question.objects.all()

    return render(request,'home.html',{'questions':ques})