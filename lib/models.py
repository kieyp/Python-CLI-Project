from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime

engine = create_engine('sqlite:///factory_data.db')

Base = declarative_base()

employee_shift_association = Table(
    "employee_shift_association",
    Base.metadata,
    Column("employee_id", Integer, ForeignKey("employees.id")),
    Column("shift_id", Integer, ForeignKey("shifts.id"))
)

class Factory(Base):
    __tablename__ = 'factories'
    id = Column(Integer, primary_key=True)
    location = Column(String)
    type = Column(String)

    managers = relationship("Manager", back_populates="factory")
    employees = relationship('Employee', back_populates="factory")
    shifts = relationship("Shift", back_populates="factory")

class Manager(Base):
    __tablename__ = 'managers'
    __table_args__ = (UniqueConstraint('email', name='unique_email'),)
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    start_date = Column(DateTime, default=datetime.now)
    email = Column(String)
    employee_no = Column(String)
    salary_type = Column(String)
    salary_amount = Column(Integer)
    job_title = Column(String)
    role = Column(String)

    factory_id = Column(Integer, ForeignKey('factories.id'))
    factory = relationship("Factory", back_populates="managers")

    shifts = relationship("Shift", back_populates="manager")


class Employee(Base):
    __tablename__ = 'employees'
    __table_args__ = (UniqueConstraint('email', name='unique_email'),)
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    start_date = Column(DateTime, default=datetime.now)
    email = Column(String)
    employee_no = Column(String)
    salary_type = Column(String)
    salary_amount = Column(Integer)
    job_title = Column(String)
    role = Column(String)

    factory = relationship('Factory', back_populates="employees")
    factory_id = Column(Integer, ForeignKey('factories.id'))

    shifts = relationship("Shift", secondary=employee_shift_association, back_populates="employees")

class Shift(Base):
    __tablename__ = 'shifts'
    id=Column(Integer(),primary_key=True)
    shift_name = Column(String)
    shift_supervisor = Column(String)

    factory_id = Column(Integer, ForeignKey("factories.id"))
    factory = relationship("Factory", back_populates="shifts")
    employees = relationship("Employee", secondary=employee_shift_association, back_populates="shifts")

    manager_id = Column(Integer, ForeignKey("managers.id"))
    manager = relationship("Manager", back_populates="shifts")