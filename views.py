from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import django_filters
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from shop1.models import Phones,PhonesImage,Poster,Cart,Product,Tv,Laptop,Itemcount,TvsImage
from django.db.models import Q
from django.contrib.auth.decorators import login_required
def index(request):
    phonelst = Phones.objects.all()
    posterlst = Poster.objects.all()
    tvs = Tv.objects.all()
    i=0
    lst=[]
    for k in phonelst:
        lst.append(k)
        i=i+1
        if i==6:
            break
    return render(request,'home.html',{'lst':lst,'posterlst':posterlst,'tvs':tvs})

def returnhome(request):
    return redirect(index)

def signup(request):
    global user
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False

            # user.save()
            email = form.cleaned_data.get("email")
            try:
                user = User.objects.get(email=email)
                #print(user)
                messages.success(request, f'email already exist {email}!')
                return redirect(signup)
            except User.DoesNotExist:
                current_site = get_current_site(request)
                mail_subject = 'Activate your blog account.'
                message = render_to_string('acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                            mail_subject, message, to=[to_email]
                )
                email.send()
                return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()

    return render(request, 'register.html', {'form': form})

def activate(request, uidb64, token):
    # try:
    #     uid = force_text(urlsafe_base64_decode(uidb64))
    #     # user = User.objects.get(pk=uid)
    # except(TypeError, ValueError, OverflowError, User.DoesNotExist):
    #     user = None
    var=None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        var=user
        #login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def user_login(request):
    global user
    context={}
    if request.method=='POST':
        email=request.POST["email"]
        password=request.POST['password']
        #print(User)
        try:
            username = User.objects.get(email=email)
            #print(user)
            user=authenticate(request,username=username,password=password)
            print(user)
            if user:
                login(request,user)
                messages.success(request,f'login as {username}')
                return redirect(index)
            else:
                context["error"]="provide valid credential !"
                messages.success(request,f'provide valid credential !')
                return redirect(index)
        except User.DoesNotExist:
            messages.success(request, f'email does not exist {email}!')
            return redirect(signup)

def user_logout(request):
    logout(request)
    return redirect(index)

def phones_details(request):
    data = Phones.objects.all()
    stu = {
    "phonesdetail": data
     }
    return render_to_response("home.html", stu)

def single(request,id):
    lst2=[]
    id1=id
    id=''
    c=0
    lst1 = Phones.objects.all().filter(modelno=id1)
    lsttv = Tv.objects.all().filter(modelno=id1)
    phonesimage = PhonesImage.objects.all().filter(property=id1)
    tvimage = TvsImage.objects.all().filter(property=id1)
    #print(type(id))
    for i in lst1:
        if i.modelno == id1:
            lst2 = i
            c = 1
    for i in lsttv:
        if i.modelno == id1:
            print(i.modelno)
            c = 1

    if c == 0:
        return HttpResponse('<h1>Page not found</h1>')
    else:
        #lst2.description = lst2.description.split('\n')
        return render(request,'single.html',{'lst2':lst2,'phonesimage':phonesimage,'lsttv':lsttv,'tvimage':tvimage})

def phonepage(request):
    phonelst=Poster.objects.all()
    return render(request,'phonepage.html',{'phonelst':phonelst})

def Search(request):
    if request.method=='POST':
        query=request.POST["q"]
        str1='%'
        query1=query.strip()
        search_lst=Phones.objects.all()
        print(query)
        search_lst=search_lst.filter(Q(BrandName__icontains=query)
        |Q(modelname__icontains=query)
        |Q(modelname__istartswith=query)
        )
        print(search_lst)
        return render(request,'search.html',{'search_lst':search_lst})

@login_required(login_url='/home')
def add_cart(request,item):
    cart= Cart.objects.all()
    cart = cart.filter(user=request.user)
    if len(cart)==0:
        cart = Cart.objects.create(user=request.user,Price=0)
        cart.save()
    else:
        cart = cart.filter(user=request.user)
    px=Product.objects.all().filter(cartitemmodelno=item)
    if len(px)==0:
        px=Product.objects.create(cartitemmodelno=item,quantity=1)
        px.save()
    else:
        print("item exist in product")
    py=Product.objects.get(cartitemmodelno=item)
    cart=Cart.objects.all().filter(user=request.user)
    cart1 = Cart.objects.get(user=request.user)
    if py not in cart1.product.all():
        cart1.product.add(py)
    else:
        print("item exit in user cart")
    itemcount = Itemcount.objects.create(user=request.user,quantity=1,itemmodelno=item)
    return redirect(user_cart)


@login_required(login_url='/home')
def user_cart(request):
    cart=Cart.objects.get(user=request.user)
    ls=cart.product.all()
    cart_lst = Phones.objects.none()
    cart_lst1 = Phones.objects.none()
    cart_lst2 = Phones.objects.none()
    cart_lst3 = Phones.objects.none()
    s=0
    p=0
    for i in ls:
        cart_lst |= Phones.objects.all().filter(modelno=i.cartitemmodelno)
        cart_lst1 |= Tv.objects.all().filter(modelno=i.cartitemmodelno)
        cart_lst2 |= Laptop.objects.all().filter(modelno=i.cartitemmodelno)
    
    for i in cart_lst:
        s = s + i.Price
    
    for i in cart_lst1:
        p = p + i.Price
    cart.Price = p + s   
 
    cart.save()
    print(cart.Price)
    cartlstx = Cart.objects.all().filter(user=request.user)
    dcharge = 100
    total = dcharge+cart.Price
    itemcountlst=Itemcount.objects.all().filter(user=request.user)
    return render(request, 'cart.html', {'cart_lst1':cart_lst1,'cart_lst': cart_lst, 'ls': ls, 'cartlstx': cartlstx,'itemcountlst':itemcountlst})

@login_required(login_url='/home')
def Removefromcart(request,modelid):
    cart1=Cart.objects.get(user=request.user)
    py=Product.objects.get(cartitemmodelno=modelid)
    cart1.product.remove(py)
    cart1.save()
    return redirect(user_cart)

@login_required(login_url='/home')
def quantity(request,quantityid):
    if request.method=='POST':
        quantity=request.POST["quantity"]
        itemcount=Itemcount.objects.get(user=request.user,itemmodelno=quantityid)
        #py=Product.objects.get(cartitemmodelno=quantityid)
        itemcount.quantity=quantity
        itemcount.save()
        print(quantity)
        return redirect(user_cart)
    else:
        return redirect(user_cart)

def Phonesproduct(request,brandname):
    phonelst=Phones.objects.all().filter(BrandName__icontains=brandname)
    return render(request,'phonepage.html',{'phonelst':phonelst})



def checkout(request,checkid):
    print(checkid)
    if request.method == 'POST':
        name=request.POST['name']
        pincode=request.POST['pincode']
        modileno=request.POST['mobileno']
    if checkid == 'all':
        cartlstx = Cart.objects.all().filter(user=request.user)
        return render(request, 'checkout.html', {'cartlstx': cartlstx,})

    else:
        checklst = Phones.objects.all().filter(modelno=checkid)
        checklst1 = Tv.objects.all().filter(modelno=checkid)    
        return render(request, 'checkout.html',{'checklst': checklst,'checklst1':checklst1})

def payment(request):
    return render(request,'payment.html')



def review(request):
    if request.method == 'POST':
        rating = request.POST['rating']
        print(rating)
        return redirect(index)
    else:
        return redirect(index)
