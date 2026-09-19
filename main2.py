from pyscript import document, display
def sku_generator(e):
    document.getElementById("show").innerHTML = " " # clears the previous

    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")
    prod6 = document.getElementById("item6")
    prod7 = document.getElementById("item7")
    prod8 = document.getElementById("item8")
    prod9 = document.getElementById("item9")
    prod10 = document.getElementById("item10")
    prod11 = document.getElementById("item11")
    prod12 = document.getElementById("item12")
    prod13 = document.getElementById("item13")
    prod14 = document.getElementById("item14")
    prod15 = document.getElementById("item15")
    prod16 = document.getElementById("item16")
    prod17 = document.getElementById("item17")
    prod18 = document.getElementById("item18")



    category = ((prod1.value)*prod1.checked) + ((prod2.value)*prod2.checked) + ((prod3.value)*prod3.checked) + '-' + ((prod4.value)*prod4.checked) + ((prod5.value)*prod5.checked) + ((prod6.value)*prod6.checked) + ((prod7.value)*prod7.checked) + ((prod8.value)*prod8.checked) + ((prod9.value)*prod9.checked) + ((prod10.value)*prod10.checked) + ((prod11.value)*prod11.checked) + ((prod12.value)*prod12.checked) + '-' + ((prod13.value)*prod13.checked) + ((prod14.value)*prod14.checked) + ((prod15.value)*prod15.checked) + ((prod16.value)*prod16.checked) + ((prod17.value)*prod17.checked) + ((prod18.value)*prod18.checked)

    display(category, target="show")