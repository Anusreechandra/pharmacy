from django.shortcuts import redirect, render
from app1.models import Medicine, Owner

# Create your views here.
def main_page(request):
    return render(request,'mainpage.html')

def login(request):
    msg = ''
    if request.method == 'POST':
        owner_email = request.POST['owner_email']
        owner_password = request.POST['owner_password']

        owner_exist = Owner.objects.filter(owner_email = owner_email,owner_password = owner_password)

        if owner_exist:
            owner_data = Owner.objects.get(owner_email = owner_email,owner_password = owner_password)
            request.session['owner'] = owner_data.owner_id
            return redirect('app1:owner_home')
        else:
            msg = 'Unknown Owner..!'
    return render(request,'login.html',{'msg':msg})

def owner_home(request):
    return render(request,'owner_home.html')

def add_medicine(request):
    msg =""
    if request.method == 'POST':
        name = request.POST['medicine_name']
        quantity = request.POST['medicine_quantity']
        price = request.POST['medicine_price']
        selling_cost = request.POST['selling_cost']
        purchace_price = request.POST['purchace_price']
        image = request.FILES['pimg']
        print(image)
        new_images = Medicine(medicine_image = image,medicine_name=name,medicine_quantity=quantity,medicine_price=price,purchace_price=purchace_price,selling_cost=selling_cost)
        new_images.save()

        msg = "added"
    return render(request,'add_medicine.html',{'msg':msg,})

def view_medicine(request):
    medicine = Medicine.objects.all()

    return render(request,'view_medicine.html',{'medicine':medicine,})
    
def billing(request):
    medicine = Medicine.objects.all()

    if request.method == 'POST':
        mid = request.POST['medicine']
        qty = request.POST['qty']
        medicineqty = Medicine.objects.get(id=mid)

        medicineqty.quantity = medicineqty.quantity - int(qty)
        medicineqty.save()
        return render(request,'bill.html',{'medicine':medicine,})

        
    return render(request,'bill.html',{'medicine':medicine,})
