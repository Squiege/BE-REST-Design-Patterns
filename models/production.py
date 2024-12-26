from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import db, Base
from sqlalchemy.orm import relationship

class Production(Base):
    __tablename__ = 'production'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('product.id'), nullable=False)
    product = db.relationship("Product", back_populates="production_schemas")
    quantity_produced: Mapped[int] = mapped_column(db.Integer, nullable=False)
    date_produced: Mapped[Date] = mapped_column(db.Date, nullable=False)
