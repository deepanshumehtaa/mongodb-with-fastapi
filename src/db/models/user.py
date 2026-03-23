import uuid
from typing import Optional, List
from ..clients.mongo import RWModel
from ..schemas.bill import Book, BillCategory, Account


default_expenditure_cat = [
    BillCategory(id=0, icon=0, name="Dining"),
    BillCategory(id=1, icon=1, name="Snacks & Drinks"),
    BillCategory(id=2, icon=2, name="Housing"),
    BillCategory(id=3, icon=3, name="Transportation"),
    BillCategory(id=4, icon=4, name="Entertainment"),
    BillCategory(id=5, icon=5, name="Travel & Leisure"),
    BillCategory(id=6, icon=6, name="Education"),
    BillCategory(id=7, icon=7, name="Automotive"),
    BillCategory(id=8, icon=8, name="Utilities"),
    BillCategory(id=9, icon=9, name="Childcare"),
    BillCategory(id=10, icon=10, name="Medical"),
    BillCategory(id=11, icon=11, name="Cleaning"),
    BillCategory(id=12, icon=12, name="Social & Gifts"),
    BillCategory(id=13, icon=13, name="Shopping", sub="Clothing"),
    BillCategory(id=14, icon=14, name="Shopping", sub="Digital"),
    BillCategory(id=15, icon=15, name="Shopping", sub="Home"),
    BillCategory(id=16, icon=16, name="Others"),
]


default_income_cat = [
    BillCategory(id=0, icon=1000, is_expenditure=False, name="Salary"),
    BillCategory(id=1, icon=1001, is_expenditure=False, name="Bonus"),
    BillCategory(id=2, icon=1002, is_expenditure=False, name="Loans"),
    BillCategory(id=3, icon=1003, is_expenditure=False, name="Debt Collection"),
    BillCategory(id=4, icon=1004, is_expenditure=False, name="Interest"),
    BillCategory(id=5, icon=1005, is_expenditure=False, name="Windfall"),
    BillCategory(id=6, icon=1006, is_expenditure=False, name="Investment Recovery"),
    BillCategory(id=7, icon=1007, is_expenditure=False, name="Investment Income"),
    BillCategory(id=8, icon=1008, is_expenditure=False, name="Reimbursement"),
    BillCategory(id=9, icon=1009, is_expenditure=False, name="Other Income"),
]

class UserDoc(RWModel):
    __collection__ = "user"
    __indexes__ = {"username": "unique"}

    id: Optional[str] = str(uuid.uuid4())[:7]
    username: Optional[str]
    password: Optional[str]

    books: List[Book] = [Book(id=0, name="Default Ledger")]
    accounts: List[Account] = [Account(id=0, name="Default Account")]
    expenditure_cats: List[BillCategory] = default_expenditure_cat
    income_cats: List[BillCategory] = default_income_cat
