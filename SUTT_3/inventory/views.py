from django.shortcuts import get_object_or_404, render, redirect
from inventory.models import inventory, IssueItem, Userlog, IsMod,Category,Moderatorlog
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from .filters import InventoryFilter
import datetime
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.template.loader import render_to_string

from .forms import SignUpForm,Additemform,Addcategoryform,Additemform_two
from .resources import inventoryResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
import xlwt
from django.db import IntegrityError
# Create your views here.

@login_required
def index(request):
        x = request.user
        y = IsMod.objects.get(id=1)
        if x==y.user :
            return redirect('moderatorview')

        else:






            user = request.user
            Item_list = inventory.objects.all()

        #    if request.method == 'GET':
        #        pt=request.GET.get('search')
        #        if pt!=None:
        #            Item_list = inventory.objects.filter(Item_name__icontains=pt)

            my_filter = InventoryFilter(request.GET, queryset=Item_list)
            Item_list=my_filter.qs

            Issue_Item_no = IssueItem.objects.all().count()
            dict = {'inventory': Item_list, 'number':Issue_Item_no,'user':user,'my_filter':my_filter}


            return render(request,'index3.html',dict)

@login_required
def detail(request,Item_id):
    x = request.user
    y = IsMod.objects.get(id=1)
    if x==y.user :
        return redirect('moderatorview')

    else:

        if request.method=='POST':

            Item = get_object_or_404(inventory, pk=Item_id)
            #Item.Quantity-=1
            #Item.save()
            user = request.user
            itemm = get_object_or_404(inventory, pk=Item_id)
            try:
                quantity = int(request.POST.get('quantity_value'))
                if quantity <= Item.Quantity:
                    issueItem = IssueItem(user = user,item = itemm,quantity = quantity,date=datetime.datetime.now())
                    issueItem.save()
                    Item.Quantity=Item.Quantity-quantity
                    Item.save()
                    userlog=Userlog.objects.create(user=user,issue_details=issueItem,copy_issue_item_name=issueItem.item.Item_name,copy_issue_item_quantity=issueItem.quantity,copy_issue_category=issueItem.item.category,copy_issue_item_date=issueItem.date,return_date=None)



                else:
                    messages.error(request,'You cannot issue more items than avialable in the inventory')
                    return redirect('detail', Item.id)

            except IntegrityError :
                messages.error(request,'Type appropriate quantity')
                return redirect('detail', Item.id)

            except ValueError :
                messages.error(request,'Type appropriate quantity')
                return redirect('detail', Item.id)

            # print(quantity)

            return redirect('inventory')



        return render(request,'detail.html')

#@login_required
#def cart(request):
#    if request.method == 'GET':
#        Item_list = IssueItem.objects.all()
#        dict = {'cart': Item_list}
#        return render(request,'cart.html',dict)

#def removefromcart(request,Issue_Item_id):
#    if request.method == 'POST':
#        Issue_item = get_object_or_404(IssueItem,pk=Item_id)
#        dict = {'cart': Item_list}
#        Issue_item.delete()
#        return render(request,'cart.html',dict)





#def checkoutview(request):
#    if request.method == 'GET':
#        Item_list = IssueItem.objects.all()
#        dict = {'cart': Item_list}
#        return render(request,'checkout.html',dict)

#def placeorder(request):

#    if request.method=='POST':
#        issued_items = IssueItem.objects.all()
#        user = request.user

#        for i in issued_items:
#            issue=Issue.objects.create(user=user,items=i.item)
#            userlog=Userlog.objects.create(user=user,issue_details=issue,copy_issue_item_name=issue.items.Item_name,copy_issue_item_date=issue.date,return_date=None)





    #    template = render_to_string('email.html',{'details':issued_items})
    #    email = EmailMessage(
    #    'Thank You for Issuing',
    #    template,
    #    settings.EMAIL_HOST_USER,
    #    ['f20212170@pilani.bits-pilani.ac.in']
    #    )

    #    IssueItem.objects.all().delete()
    #    return redirect('inventory')

@login_required
def profile(request):
    x = request.user
    y = IsMod.objects.get(id=1)
    if x==y.user :
        return redirect('moderatorview')
    else:
        if request.method == 'GET':
            user = request.user
            final_issued = IssueItem.objects.filter(user=user)
            dict={'final_issued':final_issued}
            #print("get")
            return render(request,'profile.html',dict)
        # if request.method == "POST":
        #     final_issued_item_id = int(request.POST.get('item_id'))
        #     return_item = get_object_or_404(IssueItem, pk=final_issued_item_id)
        #     user_log=Userlog.objects.get(issue_details=return_item)
        #     user_log.return_date=datetime.datetime.now()
        #     user_log.save()
        #     inventory_list = inventory.objects.all()
        #     dict = {'return_item':return_item}
        #     for i in inventory_list:
        #         if i.Item_name == return_item.item.Item_name:
        #             i.Quantity=i.Quantity + return_item.quantity
        #             i.save()
        #             IssueItem.objects.filter(pk=final_issued_item_id).delete()
        #
        #     return redirect('profile')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            try:
                account_status = request.user.ismod.ismod
            except:
                account_status = False
            if account_status:
                pass
            else:
                IsMod.objects.create(user=request.user, isMod=True)

    else:
        form = SignUpForm()
    return render(request, 'moderator.html', {'form': form})


@login_required
def moderatorview(request):

            x = request.user
            y = IsMod.objects.get(id=1)
            if x==y.user :

                inventory_list=inventory.objects.all()
                dict={'inventory_list':inventory_list}


                return render(request,'moderator2.html',dict)
            else:
                return redirect('inventory')

@login_required
def additems(request):

                x = request.user
                y = IsMod.objects.get(id=1)
                if x==y.user :

                    form = Additemform_two()
                    dict = {'form':form}

                    if request.method == 'POST':
                        form = Additemform_two(request.POST)
                        if form.is_valid():
                            if inventory.objects.filter(Item_name=form.cleaned_data['Item_name'],category=form.cleaned_data['category']).exists():
                                messages.error(request,'Item already exists')
                                return redirect('additems')
                            else:
                                item_name=form.cleaned_data['Item_name']
                                quantity=form.cleaned_data['Quantity']
                                category=form.cleaned_data['category']
                                if quantity>=1:
                                    inventory.objects.create(Item_name=item_name,Quantity=quantity,category=category)
                                    Moderatorlog.objects.create(Item_name=item_name,Quantity=quantity,category=category,date_added=datetime.datetime.now())
                                    return redirect('moderatorview')
                                else:
                                    messages.error(request,'Quantity cannot be less than 1')
                                    return redirect('additems')
                    return render(request,'additems.html',dict)
                else:
                    return redirect('inventory')


@login_required
def addcategory(request):

            x = request.user
            y = IsMod.objects.get(id=1)
            if x==y.user :


                form = Addcategoryform()
                dict={'form':form}

                if request.method == 'POST':
                    form = Addcategoryform(request.POST)

                    if form.is_valid():
                        category=form.cleaned_data['category']
                        if Category.objects.filter(category=category).exists():
                            messages.error(request,'This category already exists')
                        else:
                            Category.objects.create(category=category)
                            return redirect('moderatorview')
                return render(request,'addcategory.html',dict)

            else:
                return redirect('inventory')

@login_required
def editinventory(request,item_id):

            x = request.user
            y = IsMod.objects.get(id=1)
            if x==y.user :

                item = inventory.objects.get(id=item_id)
                form = Additemform(instance=item)
                dict = {'form':form}

                initial_dict = {'Item_name':item.Item_name,'Quantity':item.Quantity}
                print(initial_dict)

                if request.method == 'POST':

                    item = inventory.objects.get(id=item_id)
                    form = Additemform(request.POST or None, instance=item)
                    if form.is_valid():
                        form.save()
                        return redirect('moderatorview')
                return render(request,'editinventory.html',dict)

            else:
                return redirect('inventory')


def upload(request):

        x = request.user
        y = IsMod.objects.get(id=1)
        if x==y.user :
            if request.method == 'POST':
                inventory_resource = inventoryResource
                dataset = Dataset()
                try:
                    new_inventory = request.FILES['myfile']


                except KeyError:
                    messages.error(request,'Please upload an excel file')
                    return redirect('upload')

                if new_inventory.name.endswith('.xlsx'):
                    imported_data = dataset.load(new_inventory.read(),format='xlsx')

                    for data in imported_data:
                        category, _ =Category.objects.get_or_create(category=data[3])
                        if inventory.objects.filter(Item_name=data[1],category=category).exists():
                            messages.error(request,f'{data[1]} not been added because they already exist in {data[3]} category')
                            continue
                        if data[2]<=0:
                            messages.error(request,f'{data[1]} has not been added as its quantity is less than or equal to zero')
                            continue    
                        value = inventory(
                            data[0],
                            data[1],
                            data[2],
                            category.id
                            )

                        value.save()
                        p = inventory.objects.get(Item_name=data[1])
                        Moderatorlog.objects.create(Item_name=data[1],Quantity=data[2],category=p.category,date_added=datetime.datetime.now())
                    return redirect('moderatorview')

                else:
                        messages.error(request,'Please upload a valid excel File')
                        return redirect('upload')

            return render(request,'upload.html')
        else:
            return redirect('inventory')


def returndetail(request,Return_item_id):

    if request.method=='POST':

        item_to_return=get_object_or_404(IssueItem,pk=Return_item_id)
        quantity = int(request.POST.get('quantity_value'))
        if item_to_return.quantity>quantity:
            item_to_return.quantity=item_to_return.quantity-quantity
            item_to_return.save()
            userlogupdate=Userlog.objects.get(issue_details=item_to_return)
            userlogupdate.quantity_to_be_returned=item_to_return.quantity
            userlogupdate.save()
            inventory_update=inventory.objects.get(Item_name=item_to_return.item.Item_name,category=item_to_return.item.category)

            inventory_update.Quantity=inventory_update.Quantity+quantity
            inventory_update.save()


        elif item_to_return.quantity==quantity:
            userlogupdate=Userlog.objects.get(issue_details=item_to_return)
            userlogupdate.return_date=datetime.datetime.now()
            item_to_return.quantity=item_to_return.quantity-quantity
            userlogupdate.quantity_to_be_returned=item_to_return.quantity
            userlogupdate.save()
            item_to_return.save()
            inventory_update=inventory.objects.get(Item_name=item_to_return.item.Item_name,category=item_to_return.item.category)

            inventory_update.Quantity=inventory_update.Quantity+quantity
            inventory_update.save()
            item_to_return.delete()

        else:
            messages.error(request,'You cannot return more than you have')





        return redirect('profile')

    return render(request,'returndetail.html')

def export_excel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=inventory' +  str(datetime.datetime.now()) + '.xls'

    wb =  xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('inventory')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold = True

    coloumns = ['Item_name','Quantity','category']

    for col_num in range(len(coloumns)):
        ws.write(row_num,col_num,coloumns[col_num],font_style)

    rows=inventory.objects.all().values_list('Item_name','Quantity','category')

    font_style=xlwt.XFStyle()
    for row in rows:
        row_num +=1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)

    wb.save(response)
    print('Hi')

    return response








# def returnitem(request,final_issued_item_id):
#     if request.method == 'POST':
#         return_item = get_object_or_404(Issue, pk = final_issued_item_id)
#         print(return_item)
#         inventory = inventory.objects.all()
#         dict = {'return_item':return_item}
#         for i in inventory:
#             if i.Item_name == return_item.items.Item_name:
#                 i.Quantity+=1
#                 Issue.objects.filter(pk=final_issued_item_id).delete()
#         return redirect('profile')
#     return render(request,'profile.html')
