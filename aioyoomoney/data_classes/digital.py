from dataclasses import dataclass


@dataclass
class DigitalArticle:
    merchant_article_id: str
    serial: str
    secret: str


@dataclass
class DigitalBonus:
    serial: str
    secret: str


@dataclass
class DigitalGoods:
    articles: list[DigitalArticle]
    bonuses: list[DigitalBonus]
