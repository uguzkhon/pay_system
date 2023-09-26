from database import get_db

from datetime import datetime
from database.models import Transaction, Card

from transaction import TransactionModel


#Создать транзакцию
def add_new_transaction_db(data: TransactionModel):
    db = next(get_db())

    #Получаем информацию о картах
    card_from = db.query(Card).filter_by(card_number=data.card_from).first()
    card_to = db.query(Card).filter_by(card_number=data.card_to).first()

    #Проверка баланса card_from
    if card_from.balance >= data.amount:
        card_from.balance -= data.amount
        card_from.balance -= data.amount
        card_to.balance += data.amount

        transaction_info = data.model_dump()
        new_transaction = Transaction(reg_date=datetime.now(), **transaction_info)

        db.add(new_transaction)
        db.commit()

        return True

    return False


#Увидеть транзакции определенной карты
def get_excact_card_db(user_id: int, card_id: int):
    db = next(get_db())

    exact_card_monitoring = db.query(Transaction).filter_by(user_id=user_id, card_from=card_id).all()

    return exact_card_monitoring


#Вывести список всех транзакций
def get_all_cards_monitoring_db(user_id: int):
    db = next(get_db())

    all_cards_monitoring = db.query(Transaction).filter_by(user_id=user_id).all()

    return all_cards_monitoring