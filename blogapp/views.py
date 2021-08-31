from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import post, comment, comment_reply
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    post_data = post.objects.all()
    return render(request, 'blogapp/blog.html',{'post':post_data})


def post_view(request,id):
    post_view_data = post.objects.filter(post_id = id)
    load_comment = comment.objects.filter(comment_post=id)
    reply_data = comment_reply.objects.filter(rply_post=id)
    comments_length = len(reply_data)+len(load_comment)
    return render(request, 'blogapp/post_view.html',{'post':post_view_data,'load_comment':load_comment,'reply':reply_data,'comments_length':comments_length})

def search_data(request):
    query = request.GET.get('search')
    print(query)
    print('working')
    datatemp = post.objects.all()
    data = []
    search = False
    
    for item in datatemp:
        if query in item.title.lower() or query in item.h1heading.lower() or query in item.h1content.lower() or query in item.h2heading.lower() or query in item.h2content.lower():
            data.append(item)
            search = True
        elif query =='':
            data.append(item)
        
           
    return render(request, 'blogapp/blog.html',{'post':data,'txt_query':query,'search':search})

def post_comment(request, postid):
    if request.method == 'POST':
        print('working')
        comment_text = request.POST['comment']
        user = request.user
        post_id = post.objects.get(post_id=postid)
        comment_data = comment(comment=comment_text, user=user, comment_post=post_id)
        comment_data.save()
        messages.success(request,'Your comment has been posted successfully')      
        return HttpResponse(post_view(request,postid))

    
def handle_reply(request, postid, sno):
    
    if request.method == 'POST':
        rply = request.POST['rply']
        user = request.user
        post_id = post.objects.get(post_id=postid)
        on_comment = comment.objects.get(comment_id = sno)
        reply_data = comment_reply(rply = rply,comment_sno=sno, user= user, comment=on_comment, rply_post=post_id)
        reply_data.save()   
        messages.success(request,'Your rply has been posted successfully')
    return redirect('/blog/post_view/'+str(postid))   
    
def delete_rply(request, rid,pid):
    reply_data = comment_reply.objects.get(rply_id = rid)
    reply_data.delete()
    messages.success(request,'Your comment has been deleted successfully')
    return redirect('/blog/post_view/'+str(pid)) 

def delete_comment(request, cid, pid):
    comment_data = comment.objects.get(comment_id = cid)
    comment_data.delete()
    messages.success(request,'Your comment has been deleted successfully')
    return redirect('/blog/post_view/'+str(pid)) 

def create_blog(request):

    return render(request,'blogapp/create_blog.html')


def save_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = request.POST['image']
        content = request.POST['content']
        post_data= post(title=title, content=content, image='shop/images/'+image)
        post_data.save()
        print(content)
        return render(request,'blogapp/blog.html')