from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
import hashlib
import secrets


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    salt: Mapped[str] = mapped_column(String(32))

    # Virtual link (not stored in DB!)
    items: Mapped[list["Item"]] = relationship(back_populates="owner")

    def set_password(self, password: str):
        """Hashes password with random salt using SHA-256"""
        self.salt = secrets.token_hex(16)
        self.hashed_password = hashlib.sha256(
            (password + self.salt).encode()
        ).hexdigest()


    def verify_password(self, password: str) -> bool:
        """Checks if password matches the hash+salt"""
        return self.hashed_password == hashlib.sha256((password + self.salt).encode()).hexdigest()


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))

    # Actual foreign key (stored in DB)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    # Virtual link (not stored in DB!)
    owner: Mapped["User"] = relationship(back_populates="items")
