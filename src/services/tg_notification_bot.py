from httpx import AsyncClient

from src.config import settings

async def send_notification_tg(text: str) -> None:
    url = f"https://api.telegram.org/bot{settings.TG_BOT_APIKEY}/sendMessage"

    try:
        async with AsyncClient(proxy=settings.TG_PROXY, timeout=15.0) as client:
            for chat_id in settings.TG_ADMIN_CHAT_IDS:
                payload = {
                    "chat_id": chat_id,
                    "text": text,
                    "parse_mode": "HTML",
                }
                response = await client.post(url, json=payload, timeout=15.0)
                print(f"Ответ от Telegram: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Ошибка отправки сообщения в Telegram: {repr(e)}")

class TemplatesMessages:

    @staticmethod
    def consultation_message(
        client_name: str,
        client_number: str,
        client_car: str,
        client_comment: str | None = None
    ) -> str:
        comment_text = client_comment if client_comment else "Не указан"
        return (
            "🎨 <b>Новая заявка на консультацию!</b>\n\n"
            f"👤 <b>Клиент:</b> {client_name}\n"
            f"📞 <b>Телефон:</b> <code>{client_number}</code>\n"
            f"🚗 <b>Автомобиль:</b> {client_car}\n\n"
            f"💬 <b>Комментарий:</b>\n"
            f"<i>{comment_text}</i>"
        )

    @staticmethod
    def order_message(
        client_name: str,
        client_number: str,
        client_car: str,
        price: int,
        client_comment: str | None = None
    ) -> str:
        comment_text = client_comment if client_comment else "Не указан"
        formatted_price = f"{price:,}".replace(",", " ")
        return (
            "🔥 <b>Новый заказ с калькулятора!</b>\n\n"
            f"👤 <b>Клиент:</b> {client_name}\n"
            f"📞 <b>Телефон:</b> <code>{client_number}</code>\n"
            f"🚗 <b>Автомобиль:</b> {client_car}\n"
            f"💰 <b>Расчётная сумма:</b> <b>{formatted_price} ₽</b>\n\n"
            f"💬 <b>Комментарий:</b>\n"
            f"<i>{comment_text}</i>"
        )
