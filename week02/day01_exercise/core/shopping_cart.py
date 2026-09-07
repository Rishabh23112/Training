"""Shopping cart"""

from dataclasses import dataclass


@dataclass
class Product:
    """Product with data validation"""

    name: str
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")


class ShoppingCart:
    """Shopping cart with products."""

    def __init__(self):
        self._items: dict[str, tuple[Product, int]] = {}  # name -> (product, quantity)

    def add_item(self, product: Product, quantity: int = 1) -> None:
        """Add product to cart."""
        if quantity < 0:
            raise ValueError("Quantity should be greater than 0.")

        if product.name in self._items:
            existing_product, existing_quantity = self._items[product.name]
            self._items[product.name] = (
                existing_product,
                existing_quantity + quantity,
            )
        else:
            self._items[product.name] = (product, quantity)

    def remove_item(self, product_name: str) -> None:
        """Remove product from cart."""
        self._items.pop(product_name)

    def get_total(self) -> float:
        """Calculate total price."""
        return sum(
            product.price * quantity for product, quantity in self._items.values()
        )

    def __len__(self) -> int:
        """Return total number of items (considering quantities)."""
        return sum(quantity for i, quantity in self._items.values())
