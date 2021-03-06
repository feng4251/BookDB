# encoding: utf-8
from bookdb.models import *
from bookdb.forms import *
from django.http import *
#from django.template import Context,RequestContext
from django.shortcuts import *


def searchAuthor(request):
    post=request.POST
    if post:
        author=Author.objects.filter(Name=post['Name'])
        if author:
            book=Book.objects.filter(AuthorID=author[0].id)
            if book:
                return HttpResponseRedirect('http://127.0.0.1:8000/searchResult/'+str(author[0].id)+'/')
            else:
                return HttpResponseRedirect('http://127.0.0.1:8000/searchResult/none/')
        else:
            return HttpResponseRedirect('http://127.0.0.1:8000/searchResult/none/')
    else:
        return render_to_response("search.html",context_instance=RequestContext(request))

def searchResult(request,auid):
    if auid=='none':
        return render_to_response("searchNone.html",context_instance=RequestContext(request))
    else:
        allbook=Book.objects.filter(AuthorID=int(auid))
        return render_to_response('search_result.html',{'allbook':allbook,'Name':allbook[0].AuthorID.Name})

def book_list(request):
    book_lst=Book.objects.all()
    return render_to_response('book_list.html',{'allbook':book_lst})

def update_book(request,isbn):
    post=request.POST
    if post:
        book1=Book.objects.filter(ISBN=isbn)[0]
        author=Author.objects.filter(Name=post['Author'])
        if post['Author']==book1.AuthorID.Name:
            pass
        else:
            if author:
                while len(author)>1:
                    author[0].delete()
            else:
                Author.objects.create(Name=post['Author'],Age=-1,Country='Earth')
                author=Author.objects.filter(Name=post['Author'])
            book1.AuthorID=author[0]
        book1.Title=post['Title']
        book1.Publisher=post['Publisher']
        book1.PublishDate=post['PublishDate']
        book1.Price=post['Price']
        book1.save()
        if author[0].Age==-1:
            return HttpResponseRedirect('http://127.0.0.1:8000/update_author/'+str(author[0].id)+'/')
        else:
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        book=Book.objects.get(ISBN=isbn)
        csrfContent = RequestContext(request, {'book':book})
        return render_to_response("refresh_book.html", csrfContent)

def update_author(request,auid):
    post=request.POST
    a=Author.objects.get(pk=int(auid))
    if post:       
        a.Name=post['Name']
        a.Age=post['Age']
        a.Country=post['Country']
        a.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        csrfContent = RequestContext(request, {'author':a})
        return render_to_response("refresh_writer.html", csrfContent)

def detail(request,isbn):
    book=Book.objects.get(ISBN=isbn)
    csrfContent = RequestContext(request, {'book':book})
    return render_to_response("book_detail.html", csrfContent)

def delete(request,isbn):
    Book.objects.get(ISBN=isbn).delete()
    return HttpResponseRedirect('http://127.0.0.1:8000/')
    
def add(request):
    post=request.POST
    if post:
        author=Author.objects.filter(Name=post['Author'])
        if author:
            while len(author)>1:
                author[0].delete()
        else:
            Author.objects.create(Name=post['Author'],Age=-1,Country='Earth')
            author=Author.objects.filter(Name=post['Author'])
        Book.objects.create(ISBN=post['ISBN'],Title=post['Title'],AuthorID=author[0],Publisher=post['Publisher'],PublishDate=post['PublishDate'],Price=post['Price'])
        if author[0].Age==-1:
            return HttpResponseRedirect('http://127.0.0.1:8000/update_author/'+str(author[0].id)+'/')
        else:
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        return render_to_response("new_book.html",context_instance=RequestContext(request))
        
    
#def add(request):
#    if request.POST:
#        form=BookForm(request.POST)
#        if form.is_valid():
#            data=form.cleaned_data
#            new_author=data['Author']
#            print data['ISBN']
#            a=Author.objects.filter(Name=new_author)
#            if a:
#                while len(a)>1:
#                    a[0].delete()
#            else:
#                Author.objects.create(Name=new_author,Age=-1,Country='Earth')
#            auid=Author.objects.get(Name=new_author)                
#            new_book=Book(
#                ISBN=data['ISBN'],
#                Title=data['Title'],
#                AuthorID=auid,
#                Publisher=data['Publisher'],
#                PublishDate=data['PublishDate'],
#                Price=data['Price'],
#             )
#            new_book.save()
#            if auid.Age == -1:
#                return HttpResponseRedirect('http://127.0.0.1:8000/update_author/'+str(auid.id)+'/')
#            else:    
#                return HttpResponseRedirect('http://127.0.0.1:8000/')
#        else:
#            print 'here'
#            new_author=data['Author']
#            a=Author.objects.filter(Name=new_author)
#            if not a:
#                return HttpResponseRedirect('http://127.0.0.1:8000/update_author/1/')
#    else:
#        form=BookForm()
#        csrfContent = RequestContext(request, {'form':form,'title':u'添加图书|图书管理系统','posturl':'/add/'})
#        return render_to_response("input.html", csrfContent)

#def update_author(request,auid):
#    if request.POST:
#        form=AuthorForm(request.POST)
#        print form['Name']
#        if form.is_valid():
#            data=form.cleaned_data
#            a=Author.objects.get(pk=int(auid))
#            a.Name=data['Name']
#            a.Age=data['Age']
#            a.Country=data['Country']
#            a.save()
#            return HttpResponseRedirect('http://127.0.0.1:8000/')
#    else:
#        form=AuthorForm()
#        csrfContent=RequestContext(request,{'form':form,'title':u'新增作者|图书管理系统','posturl':'/update_author/'+auid+'/'})
#        return render_to_response("input.html",csrfContent)

#def update_book(request,isbn):
#    if request.POST:
#        form=UpdateForm(request.POST)
#        if form.is_valid():
#            data=form.cleaned_data
#            b=Book.objects.get(ISBN=isbn)
#            if data['Author']==b.AuthorID.Name:
#                pass
#            else:
#                a=Author.objects.filter(Name=data['Author'])
#                if a:
#                    b.AuthorID=a[0]
#                else:
#                    aa=Author.objects.create(Name=data['Author'],Age=-1,Country='Earth')
#                    b.AuthorID=aa
#            b.Title=data['Title']
#            b.Publisher=data['Publisher']
#            b.PublishDate=data['PublishDate']
#            b.Price=data['Price']
#            b.save()
#            aaa=Author.objects.get(Name=data['Author'])
#            if aaa.Age==-1:
#                return HttpResponseRedirect('http://127.0.0.1:8000/update_author/'+str(aaa.id)+'/')
#            else:
#                return HttpResponseRedirect('http://127.0.0.1:8000/')
#    else:
#        form=UpdateForm()
#        csrfContent = RequestContext(request, {'form':form,'title':u'更新图书|图书管理系统','posturl':'/update_book/'+isbn+'/'})
#        return render_to_response("input.html", csrfContent)
