from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    hashed_password = Mapped[str]

    # Virtual link (not stored in DB!)
    items: Mapped[list["Item"]] = relationship(back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    # Actual foreign key (stored in DB)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    # Virtual link (not stored in DB!)
    owner: Mapped["User"] = relationship(back_populates="items")
