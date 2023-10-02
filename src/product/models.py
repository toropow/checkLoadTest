from datetime import datetime

from sqlalchemy import (JSON, TIMESTAMP, Boolean, Column, ForeignKey, Integer,
                        MetaData, String, Table, Enum)
from sqlalchemy.dialects.postgresql import JSONB

from src.database import Base, metadata

import enum


class LoadTools(enum.Enum):
    locust = 1
    yandex_tank = 2


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)


class LoadTestDescribe(Base):
    __tablename__ = 'load_test_describe'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey(Product.id))
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)


class LoadTestResult(Base):
    __tablename__ = 'load_test_result'

    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, ForeignKey(LoadTestDescribe.id))
    data = Column(JSONB, nullable=True)
    type_load_tool = Column(Enum(LoadTools), nullable=True)
    upload_time = Column(TIMESTAMP, default=datetime.utcnow)
    test_time_start = Column(TIMESTAMP, nullable=False)
    test_time_end = Column(TIMESTAMP, nullable=False)
    successful_result_test = Column(Boolean, default=None)
    calculated_test = Column(Boolean, default=False)


class LoadTestResultSummary(Base):
    __tablename__ = 'load_test_result_summary'

    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, ForeignKey(LoadTestDescribe.id))
    data = Column(JSONB)
    upload_time = Column(TIMESTAMP, default=datetime.utcnow)
    test_time_start = Column(TIMESTAMP, nullable=False)
    test_time_end = Column(TIMESTAMP, nullable=False)
    successful_result_test = Column(Boolean, default=None)
    calculated_test = Column(Boolean, default=False)
