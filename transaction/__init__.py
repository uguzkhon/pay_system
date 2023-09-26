from pydantic import BaseModel, Field


class TransactionModel(BaseModel):
    card_from: int = Field(gt=8600000000000000)
    amount: float = Field(ge=0)
    card_to: int = Field(gt=8600000000000000)
    status: bool = False
    user_id: int