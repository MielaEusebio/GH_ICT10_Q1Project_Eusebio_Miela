from pyscript import document, display

def create_order(e):
    document.getElementById("subtotal").innerHTML = " " # clears the previous
    document.getElementById("vat").innerHTML = " " # clears the previous
    document.getElementById("totalamount").innerHTML = " "

    prod9 = document.getElementById ("item9")
    prod8 = document.getElementById("item8")
    prod7 = document.getElementById("item7")
    prod6 = document.getElementById("item6")
    prod5 = document.getElementById("item5")
    prod4 = document.getElementById("item4")
    prod3 = document.getElementById("item3")
    prod2 = document.getElementById("item2")
    prod1 = document.getElementById("item1")

    #Calculate total by multiplying value by checked status (1 or 0)
    subtotal = (float(prod9.value) *prod9.checked) + (float(prod8.value) *prod8.checked) + (float(prod7.value) *prod7.checked) + (float(prod6.value) * prod6.checked) + (float(prod5.value) * prod5.checked) + (float(prod4.value) * prod4.checked) + (float(prod3.value) * prod3.checked) + (float (prod2.value) * prod2.checked) + (float(prod1.value)*prod1.checked)
    display(subtotal, target="subtotal")

    vat = subtotal * 0.12
    display(vat, target="vat")

    totalamount = subtotal + vat
    display(totalamount, target="totalamount")




