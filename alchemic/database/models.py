from sqlalchemy import Column, ForeignKey, Table, orm, Integer


class Base(orm.DeclarativeBase):
    """Base database model."""

    pk: orm.Mapped[int] = orm.mapped_column(
        primary_key=True,
    )


potion_ingredient_association = Table(
    "potion_ingredient",
    Base.metadata,
    Column("potion_id", Integer(), ForeignKey("potion.pk")),
    Column("ingredient_id", Integer(), ForeignKey("ingredient.pk")),
)


class Ingredient(Base):
    """Ingredient database model."""

    __tablename__ = "ingredient"

    name: orm.Mapped[str]


class Potion(Base):
    """Potion database model."""

    __tablename__ = "potion"

    name: orm.Mapped[str]
    ingredients: orm.Mapped[list[Ingredient]] = orm.relationship(
        secondary=potion_ingredient_association,
        backref="potions",
        lazy="selectin",
    )
