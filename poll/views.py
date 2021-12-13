from django.http import request
from django.shortcuts import render,HttpResponse
from poll.models import Question, Choice, UserVote


from django.contrib.auth.decorators import login_required


#poll view..


@login_required(login_url="/account/login/")
def poll_view(request, pk):

    try:
        que = Question.objects.get(id=pk)
        choices = Choice.objects.filter(question=que)
        user = request.user
        uvs = UserVote.objects.filter(user=user, question=que)

        d = {"submitted": False, "question": que, "choices": choices}
        if len(uvs):
            d['uservote'] = uvs[0]

        if request.method == "POST":
            selected_choice_id = request.POST.get("choice")
            selected_choice = Choice.objects.get(id=selected_choice_id)

            if len(uvs)==0:
                uservote = UserVote(user=user,question=que,selected_choice=selected_choice)
                uservote.save()
            else:
                uservote = uvs[0]
                pre_selected = uservote.selected_choice
                # print(pre_selected.id)
                if pre_selected!=selected_choice:
                    pre_selected.vote_count = pre_selected.vote_count -1
                    pre_selected.save()
                    selected_choice.vote_count = selected_choice.vote_count + 1
                    selected_choice.save()
                else:
                    uservote.selected_choice = selected_choice
                    uservote.save()
            
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
        request, "poll.html", d
    )



# home page....
def home_view(request):
    ques = Question.objects.all()

    return render(request,'home.html',{'questions':ques})