import os
import requests
from django.shortcuts import render
from .models import Order, OrderItem


def send_to_telegram(text):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    channel_id = os.environ.get("TELEGRAM_CHANNEL_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": channel_id, "text": text, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Помилка відправки: {e}")


def index(request):
    if request.method == 'POST':
        # Збір масивів динамічних товарів
        products = request.POST.getlist('product[]')
        flavors = request.POST.getlist('flavor[]')
        weights = request.POST.getlist('weight[]')
        quantities = request.POST.getlist('quantity[]')

        # Окремі загальні поля
        phone = request.POST.get('phone')
        payment = request.POST.get('payment')
        delivery_type = request.POST.get('delivery_type')
        address = request.POST.get('address')
        remind = request.POST.get('remind')
        total_price = request.POST.get('total_price_val')

        full_address = f"{delivery_type}: {address}"

        # 1. Збереження головного замовлення в PostgreSQL
        order = Order.objects.create(
            phone=phone,
            payment_method=payment,
            delivery_address=full_address,
            total_price=total_price,
            remind=remind
        )

        # 2. Збереження кожної позиції товару
        items_text = ""
        for i in range(len(products)):
            OrderItem.objects.create(
                order=order,
                product_name=products[i],
                flavor=flavors[i],
                weight=weights[i],
                quantity=int(quantities[i])
            )
            items_text += f"🛒 <b>Позиція #{i + 1}:</b> {products[i].capitalize()} ({flavors[i]}), {weights[i]} — {quantities[i]} шт.\n"

        # 3. Формування тексту для Telegram
        tg_message = (
            f"📦 <b>НОВЕ ЗАМОВЛЕННЯ №{order.id}</b>\n\n"
            f"{items_text}\n"
            f"💰 <b>Загальна сума:</b> {total_price} грн\n"
            f"💳 <b>Спосіб оплати:</b> {payment}\n"
            f"🚚 <b>Доставка:</b> {full_address}\n"
            f"📞 <b>Телефон:</b> {phone}\n"
            f"🔔 <b>Нагадати:</b> {remind}"
        )
        send_to_telegram(tg_message)

        # Повідомлення для виведення на екран користувачу за шаблоном завдання
        success_text = f"Ваше замовлення №{order.id} на суму {total_price} грн відправлено за адресою {full_address}"
        return render(request, 'index.html', {'message': success_text})

    return render(request, 'index.html')