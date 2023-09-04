from django.shortcuts import render
from django.template import loader
from django.db import transaction
from .models import Account


# Create your views here.
def transfer(sender, receiver, amount):
    with transaction.atomic():
        # if amount < 0:
        #     return

        senderAccount = Account.objects.get(iban=sender)
        receiverAccount = Account.objects.get(iban=receiver)

        if (
            amount < 0
            or senderAccount.balance < amount
            or senderAccount.iban == receiverAccount.iban
        ):
            return

        # if senderAccount.iban == receiverAccount.iban:
        #     return

        if amount > 0 and senderAccount.balance > amount:
            senderAccount.balance -= amount
            receiverAccount.balance += amount
            senderAccount.save()
            receiverAccount.save()


def homePageView(request):
    if request.method == "POST":
        sender = request.POST.get("from")
        receiver = request.POST.get("to")
        amount = int(request.POST.get("amount"))
        transfer(sender, receiver, amount)

    accounts = Account.objects.all()
    context = {"accounts": accounts}
    return render(request, "pages/index.html", context)
