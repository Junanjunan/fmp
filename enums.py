from dataclasses import dataclass
from enum import Enum


@dataclass
class SymbolType:
    id: str
    description: str

@dataclass
class Exchange:
    id: str
    name: str


# https://financialmodelingprep.com/api/v3/stock/list
class SymbolTypeEnum(Enum):
    STOCK = SymbolType(id='stock', description='Stock')
    ETF = SymbolType(id='etf', description='ETF')
    FUND = SymbolType(id='fund', description='Fund')
    TRUST = SymbolType(id='trust', description='Trust')

    @classmethod
    def get_symbol_type_list(cls):
        return [symbol_type.value.id for symbol_type in cls]


# https://financialmodelingprep.com/api/v3/stock/list
# 'NONE' is for symbols that don't have an exchange
class ExchangeEnum(Enum):
    SET = Exchange(id='SET', name='Thailand')
    BUD = Exchange(id='BUD', name='Budapest')
    MIL = Exchange(id='MIL', name='Milan')
    HAM = Exchange(id='HAM', name='Hamburg')
    LSE = Exchange(id='LSE', name='London Stock Exchange')
    PAR = Exchange(id='PAR', name='Paris')
    PRG = Exchange(id='PRA', name='Prague')
    SAO = Exchange(id='SAO', name='São Paulo')
    OSL = Exchange(id='OSL', name='Oslo Stock Exchange')
    CPH = Exchange(id='CPH', name='Copenhagen')
    NEO = Exchange(id='NEO', name='NEO')
    XETRA = Exchange(id='XETRA', name='Frankfurt Stock Exchange')
    MCX = Exchange(id='MCX', name='Moscow Stock Exchange')
    DFM = Exchange(id='DFM', name='Dubai')
    OTC = Exchange(id='OTC', name='Other OTC')
    DUS = Exchange(id='DUS', name='Dusseldorf')
    BVC = Exchange(id='BVC', name='BVC')
    VIE = Exchange(id='VIE', name='Vienna')
    KUW = Exchange(id='KUW', name='Kuwait')
    SHH = Exchange(id='SHH', name='Shanghai')
    HEL = Exchange(id='HEL', name='Helsinki')
    PNK = Exchange(id='PNK', name='Other OTC')
    HOSE = Exchange(id='HOSE', name='Ho Chi Minh Stock Exchange')
    SGO = Exchange(id='SGO', name='Santiago')
    JPX = Exchange(id='JPX', name='Tokyo')
    AMS = Exchange(id='AMS', name='Amsterdam')
    ASX = Exchange(id='ASX', name='Australian Securities Exchange')
    ATH = Exchange(id='ATH', name='Athens')
    NASDAQ = Exchange(id='NASDAQ', name='NASDAQ')
    TSXV = Exchange(id='TSXV', name='Toronto Stock Exchange Ventures')
    NYSE = Exchange(id='NYSE', name='New York Stock Exchange')
    EGX = Exchange(id='EGX', name='EGX')
    ICE = Exchange(id='ICE', name='Iceland')
    RIS = Exchange(id='RIS', name='Riga')
    CNQ = Exchange(id='CNQ', name='Canadian Securities Exchange')
    STU = Exchange(id='STU', name='Stuttgart')
    EURONEXT = Exchange(id='EURONEXT', name='Paris')
    IST = Exchange(id='IST', name='Istanbul Stock Exchange')
    SIX = Exchange(id='SIX', name='Swiss Exchange')
    DXE = Exchange(id='DXE', name='Cboe Europe')
    STO = Exchange(id='STO', name='Stockholm Stock Exchange')
    IOB = Exchange(id='IOB', name='International Order Book')
    BRU = Exchange(id='BRU', name='Paris')
    HKSE = Exchange(id='HKSE', name='HKSE')
    WSE = Exchange(id='WSE', name='Warsaw Stock Exchange')
    BSE = Exchange(id='BSE', name='Bombay Stock Exchange')
    CAI = Exchange(id='CAI', name='EGX')
    MUN = Exchange(id='MUN', name='Munich')
    SAU = Exchange(id='SAU', name='Saudi')
    SHZ = Exchange(id='SHZ', name='Shenzhen')
    BME = Exchange(id='BME', name='Madrid Stock Exchange')
    TWO = Exchange(id='TWO', name='Taipei Exchange')
    KOE = Exchange(id='KOE', name='KOSDAQ')
    JNB = Exchange(id='JNB', name='Johannesburg')
    SES = Exchange(id='SES', name='Stock Exchange of Singapore')
    TAI = Exchange(id='TAI', name='Taiwan')
    TSX = Exchange(id='TSX', name='Toronto Stock Exchange')
    BER = Exchange(id='BER', name='Berlin')
    KLS = Exchange(id='KLS', name='Kuala Lumpur')
    KSC = Exchange(id='KSC', name='KSE')
    NSE = Exchange(id='NSE', name='National Stock Exchange of India')
    MEX = Exchange(id='MEX', name='Mexico')
    AQS = Exchange(id='AQS', name='Aquis AQSE')
    TLV = Exchange(id='TLV', name='Tel Aviv')
    NZE = Exchange(id='NZE', name='NZSE')
    BUE = Exchange(id='BUE', name='Buenos Aires')
    JKT = Exchange(id='JKT', name='Jakarta Stock Exchange')
    AMEX = Exchange(id='AMEX', name='New York Stock Exchange Arca')
    DOH = Exchange(id='DOH', name='Qatar')
    CBOE = Exchange(id='CBOE', name='Cboe US')

    @classmethod
    def get_exchange_dict(cls):
        return {exchange.value.id: exchange.value.name for exchange in cls}