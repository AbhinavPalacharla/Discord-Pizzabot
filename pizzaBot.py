import discord
import asyncio
from discord.ext import commands
from pizzapi import *

client = discord.Client()
id = client.get_guild(key)

#pizza stuff
customer = Customer('Abhinav', 'Palacharla', 'email', 'phone number')
address = Address('address', 'city', 'state', 'zip')
store = address.closest_store()
#print(store.__dict__)
menu = store.get_menu()
#print(menu.__dict__)
order = Order(store, customer, address)
print(order)
card = PaymentObject('card number', 'expiration mmyy', 'cvc(security code)', 'zip')

async def order_pizza(message):
    #pizza globals
    global pizza_count
    global drink_count
    global item_count

    pizza_count = 0
    item_count = 0
    drink_count = 0

    #add items
    if message.content.lower() == "order a pizza":
        order.add_item("14SCDELUX")
        await message.channel.send("Placing Delux Pizza in cart")
        pizza_count += 1
        item_count += 1
    elif message.content.lower() == "order a vegitarian pizza":
        order.add_item("P14IREPV")
        await message.channel.send("Placing a vegitarian Pizza in cart")
        pizza_count += 1
        item_count += 1
    elif message.content.lower() == "order a meat pizza":
        order.add_item("14SCMEATZA")
        await message.channel.send("Placing MeatZZa in cart")
        pizza_count += 1
        item_count += 1
    elif message.content.lower() == "order coke":
        order.add_item("20BCOKE")
        await message.channel.send("Placing Coke in cart")
        drink_count += 1
        item_count += 1
    elif message.content.lower() == "order dr pepper":
        order.add_item("20BDRPEP")
        await message.channel.send("Placing dr pepper in cart")
        drink_count += 1
        item_count += 1
    elif message.content.lower() == "order fanta":
        order.add_item("20BORNG")
        await message.channel.send("Placing fanta in cart")
        drink_count += 1
        item_count += 1
    elif message.content.lower() == "order sprite":
        order.add_item("20BSPRITE")
        await message.channel.send("Placing sprite in cart")
        drink_count += 1
        item_count += 1
    elif message.content.lower() == "order diet coke":
        order.add_item("20BDCOKE")
        await message.channel.send("Placing diet coke in cart")
        drink_count += 1
        item_count += 1
    elif message.content.lower() == "order a salad":
        oder.add_item("PPSCSRSA")
        await message.channel.send("Placing Ceaser in cart")
        item_count += 1
    elif message.content.lower() == "order garlic bread":
        order.add_item("B8PCGT")
        await message.channel.send("Placing garlic bread in cart")
        item_count += 1

    #remove items
    if message.content.lower() == "remove a pizza":
        order.remove_item("14SCDELUX")
        await message.channel.send("Removing delux pizza from cart")
        pizza_count -= 1
        item_count -= 1
    elif message.content.lower() == "remove a vegitarian pizza":
        order.remove_item("P14IREPV")
        await message.channel.send("Removing vegetarian pizza from cart")
        pizza_count -= 1
        item_count -= 1
    elif message.content.lower() == "remove a meat pizza":
        order.remove_item("14SCMEATZA")
        await message.channel.send("Removing MeatZZa from cart")
        pizza_count -= 1
        item_count -= 1
    elif message.content.lower() == "remove coke":
        order.remove_item("20BCOKE")
        await message.channel.send("Removing coke from cart")
        drink_count -= 1
        item_count -= 1
    elif message.content.lower() == "remove dr pepper":
        order.remove_item("20BDRPEP")
        await message.channel.send("Removing dr pepper from cart")
        drink_count -= 1
        item_count -= 1
    elif message.content.lower() == "remove fanta":
        order.remove_item("20BORNG")
        await message.channel.send("Removing fanta from cart")
        drink_count -= 1
        item_count -= 1
    elif message.content.lower() == "remove sprite":
        order.remove_item("20BSPRITE")
        await message.channel.send("Removing sprite from cart")
        drink_count -= 1
        item_count -= 1
    elif message.content.lower() == "remove diet coke":
        order.remove_item("20BDCOKE")
        await message.channel.send("Removing diet coke from cart")
        drink_count -= 1
        item_count -= 1
    elif message.content.lower() == "remove a salad":
        oder.remove_item("PPSCSRSA")
        await message.channel.send("Removing Ceaser Salad from cart")
        item_count -= 1
    elif message.content.lower() == "remove garlic bread":
        order.remove_item("B8PCGT")
        await message.channel.send("Removing garlic bread from cart")
        item_count -= 1

    if message.content.lower() == "order summary":
        if pizza_count > 0:
            if pizza_count == 1:
                await message.channel.send("You have " + pizza_count + " pizza in your count")
            else:
                await message.channel.send("You have " + pizza_count + " pizzas in your count")
        if drink_count > 0:
            if drink_count == 1:
                await message.channel.send("You have " + drink_count + " drink in your count")
            else:
                await message.channel.send("You have " + drink_count + " drinks in your count")
        if item_count > 0:
            if item_count == 1:
                    await message.channel.send("You have " + item_count + " item total in your count")
            else:
                await message.channel.send("You have " + item_count + " items total in your count")
        if item_count == 0:
            await message.channel.send("there is nothing in your cart")

    if message.content.lower() == "place order":
            x = order.place(card)
            #x = order.pay_with(card)
            print(x)
            await message.channel.send("order placed")
    else:
        await message.channel.send("there is nothing in your cart, order not placed")

@client.event
async def on_message(message):
	await order_pizza(message)

client.run('key')