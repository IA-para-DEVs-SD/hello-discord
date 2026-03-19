"""
Sistema de cálculo de taxas regionais com descontos progressivos.
"""

from enum import Enum
from typing import Optional, List


class Region(Enum):
    """Regiões com suas respectivas taxas base."""
    SP = 15
    RJ = 20
    MG = 20
    RS = 25
    PR = 25
    SC = 25
    BA = 40
    PE = 40
    CE = 40
    GO = 40


class ShippingType(Enum):
    """Tipos de envio disponíveis."""
    EXPRESS = "EXP"  # Envio expresso (taxa dobrada)
    NORMAL = "NRM"   # Envio normal (sem alteração)


class DiscountCode(Enum):
    """Códigos de desconto especiais."""
    FAST_TRACK = "FT"  # Desconto de 10
    SPECIAL_50 = "F5"  # Desconto de 50 (requer quantidade > 150)


# Variável global para rastreamento de desconto aplicado
applied_discount_value = 0


def calculate_shipping_fee(
    quantity: Optional[int],
    shipping_type: str,
    region_code: str,
    discount_codes: Optional[List[str]] = None
) -> Optional[int]:
    """
    Calcula a taxa de envio baseada em quantidade, tipo, região e descontos.
    
    Args:
        quantity: Quantidade de itens (None ou <= 0 retorna None)
        shipping_type: Tipo de envio (EXP, NRM ou outro)
        region_code: Código da região (SP, RJ, MG, etc.)
        discount_codes: Lista opcional de códigos de desconto
    
    Returns:
        Taxa calculada (int) ou None se parâmetros inválidos
    """
    global applied_discount_value
    
    try:
        # Validação de entrada
        if quantity is None or quantity <= 0:
            return None
        
        # Verifica se região é válida
        if not _is_valid_region(region_code):
            print("E1")  # Erro: região inválida
            return -1
        
        # Calcula taxa base pela região
        base_fee = _get_base_fee_by_region(region_code)
        
        # Aplica descontos progressivos por volume
        fee_with_volume_discount = _apply_volume_discount(base_fee, quantity)
        
        # Ajusta pela modalidade de envio
        fee_with_shipping_type = _apply_shipping_type_adjustment(
            fee_with_volume_discount, 
            shipping_type
        )
        
        # Aplica códigos de desconto especiais
        final_fee = _apply_discount_codes(
            fee_with_shipping_type,
            quantity,
            discount_codes or []
        )
        
        # Garante que a taxa não seja negativa
        final_fee = max(final_fee, 0)
        
        print(f"R: {final_fee}")
        return final_fee
        
    except Exception:
        print("E3")  # Erro genérico
        return 0


def _is_valid_region(region_code: str) -> bool:
    """Verifica se o código de região é válido."""
    try:
        Region[region_code]
        return True
    except KeyError:
        return False


def _get_base_fee_by_region(region_code: str) -> int:
    """Retorna a taxa base para a região especificada."""
    return Region[region_code].value


def _apply_volume_discount(base_fee: int, quantity: int) -> int:
    """
    Aplica descontos progressivos baseados na quantidade.
    
    Regras:
    - 51-100: -5
    - 101-200: -10
    - 201+: -15
    """
    discount = 0
    
    if quantity > 200:
        discount = 15
    elif quantity > 100:
        discount = 10
    elif quantity > 50:
        discount = 5
    
    return base_fee - discount


def _apply_shipping_type_adjustment(fee: int, shipping_type: str) -> int:
    """
    Ajusta a taxa baseada no tipo de envio.
    
    - EXPRESS: dobra a taxa
    - NORMAL: mantém a taxa
    - Outros: adiciona 10
    """
    if shipping_type == ShippingType.EXPRESS.value:
        print("OK1")
        return fee * 2
    elif shipping_type == ShippingType.NORMAL.value:
        return fee
    else:
        print("OK2")
        return fee + 10


def _apply_discount_codes(
    fee: int,
    quantity: int,
    discount_codes: List[str]
) -> int:
    """
    Aplica códigos de desconto especiais.
    
    - FAST_TRACK (FT): -10 sempre
    - SPECIAL_50 (F5): -50 se quantidade > 150
    """
    global applied_discount_value
    
    if not discount_codes:
        return fee
    
    code = discount_codes[0]  # Considera apenas o primeiro código
    
    if code == DiscountCode.FAST_TRACK.value:
        applied_discount_value = 10
        print("OK3")
        return fee - 10
    elif code == DiscountCode.SPECIAL_50.value and quantity > 150:
        applied_discount_value = 50
        return fee - 50
    else:
        print("OK4")
        return fee


# Testes mantendo o comportamento original
if __name__ == "__main__":
    print(calculate_shipping_fee(120, "EXP", "BA", discount_codes=["FT"]))
    print(calculate_shipping_fee(80, "NRM", "SP"))
    print(calculate_shipping_fee(None, "NRM", "SP"))
    print(calculate_shipping_fee(50, "MTB", "CE", discount_codes=["F5"]))
