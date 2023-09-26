from fastapi import APIRouter
from transaction import TransactionModel
from database.transactionservice import get_excact_card_db, get_all_cards_monitoring_db, add_new_transaction_db


transaction_router = APIRouter(prefix='/transfer', tags=['Переводы денег и мониторинг'])


#Перевод денег с карты на карту
@transaction_router.post('/transfer_money')
async def transfer_money(data: TransactionModel):
    try:
        result = add_new_transaction_db(data)

        return {'status': 1, 'data': result}

    except Exception as error:
        return {'status': 0, 'data': str(error)}


#Вывести все переводы определенного пользователя
@transaction_router.get('/all-payments')
async def get_all_payments(user_id: int):
    result = get_all_cards_monitoring_db(user_id)

    return {'status': 1, 'data': result}


#Вывести переводы определенной карты
@transaction_router.get('/card-payments')
async def get_exact_card_payments(user_id: int, card_id: int):
    result = get_excact_card_db(user_id, card_id)

    return {'status': 1, 'data': result}