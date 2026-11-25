"""E13. Компоненты комплектов."""
from common import add

TABLE = "kit_component"


def generate(cur, batches, rng):
    for b in batches:
        add(cur, TABLE, kit_sku=b.products[2].sku, composition_version=1,
            component_sku=b.products[1].sku, quantity=b.units_per_kit,
            component_order="Основной компонент", is_required=True, allowed_substitutions=None)
    return len(batches)
