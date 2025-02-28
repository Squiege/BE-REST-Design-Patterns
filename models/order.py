from sqlalchemy.orm import Mapped, mapped_column
from database import db, Base
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ = 'orders'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(db.Integer, nullable=False)
    total_price: Mapped[float] = mapped_column(db.Float, nullable=False)

    # Relationships
    customer = relationship("Customer", back_populates="orders")
    product = relationship("Product", back_populates="orders")

