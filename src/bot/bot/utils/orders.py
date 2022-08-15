from bot.database.models import Order


async def create_orders(data: dict):
    order = Order(category=data['category'],
                  datatime=data['datatime'],
                  price=data['price'],
                  url_user=data["link"],
                  url_document=data['url'])
    await order.save()
    return order.id
