from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/checkDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    """
     This is User model which store a data about users in application
        - username and email should be unique to identify the user and to prevent create user with same credentials
        - ContactNo length should be 10.
        - If isAdmin is set to True then that user is consider as Admin
        - If status is False then that user is consider as Deleted or deactive
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)
    first_name = db.Column(db.String(25), default="")
    last_name = db.Column(db.String(25), default="")
    email = db.Column(db.String(50), unique=True)
    contactNo = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(50), default="")
    password = db.Column(db.String(80))
    total_visits = db.Column(db.Integer, default=0)
    isAdmin = db.Column(db.Boolean, default=False, nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    # defining Relationship with Quotation table
    quotations = db.relationship(
        "Quotation", backref="quotations", lazy="dynamic")
    # defining Relationship with Visits table
    visits = db.relationship("Visits", backref="visits", lazy="dynamic")
    # defining Relationship with Todos table
    todos = db.relationship("Todos", backref="todos", lazy="dynamic")


class Visits(db.Model):
    """
        This is Visits Model which store a information about all Visits.
            - company_id is foreign key from company table to recognize visit is for which company
            - user_id is Foreign key from users table to recognize which user has visited the company
            - quotation_id is Foreign key from quotation table to know the quotation details on visit
            - date and time fields is for know the date and time of visit
            - location store the geographical visit location where visit or meeting conducted.
            - If status is False then that entry is consider as Deleted or deactive
    """
    __tablename__ = "visits"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    compnay_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    quotaion_id = db.Column(db.Integer, db.ForeignKey('quotations.id'))
    summary = db.Column(db.String(250), default="")
    date_of_visit = db.Column(db.Date, nullable=False)
    time_of_visit = db.Column(db.Time, nullable=False)
    location = db.Column(db.String(50), default="")
    status = db.Column(db.Boolean, default=True)
    # defining Relationship with Attachements model
    attachments = db.relationship(
        "Attachments", backref='attachments', lazy="dynamic")


# Attachments Model
class Attachments(db.Model):
    """
        This is Attachment Model which store a url of attachment for corresponding visit.
            - visit_id is Foreign key from visits table to recognize this attachment is for which visit.
            - attachment_url is for stored the file location url in string format
            - If status is False then that entry is consider as Deleted or deactive
    """
    __tablename__ = "attachments"

    id = db.Column(db.Integer, primary_key=True)
    attachment_url = db.Column(db.String(250), default="")
    visit_id = db.Column(db.Integer, db.ForeignKey('visits.id'))
    status = db.Column(db.Boolean, default=True)


class Company(db.Model):
    """
     This is Company model which store a data about Company in application
        - email should be unique to identify the company and to prevent create company with same credentials
        - ContactNo length should be 10.
        - type_of_foundry and all other fields are characteristics fo company.
        - location field store the actual Geographical location in database in the form of longitude and latitude
        - If status is False then that company is consider as Deleted or deactive
    """
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    contactNo = db.Column(db.String(10), unique=True, nullable=False)
    address = db.Column(db.String(50), default="")
    type_of_foundry = db.Column(db.String(30), default="")
    product_type = db.Column(db.String(30), default="")
    operation_type = db.Column(db.String(30), default="")
    furnace_type = db.Column(db.String(30), default="")
    tunnage = db.Column(db.Integer, default=0)
    location = db.Column(db.String(50), default="")
    status = db.Column(db.Boolean, default=True, nullable=False)
    # contact_person is not a column, we just defining a relationship with contact_person table
    contact_persons = db.relationship(
        "ContactPerson", backref="contact_persons", lazy='dynamic')
    # Defining relationship with InventryProduct
    inventry_products = db.relationship(
        "InventryProduct", backref="inventry_products", lazy="dynamic")
    # defining Relationship with Quotation table
    quotations = db.relationship(
        "Quotation", backref="quotations", lazy="dynamic")

# Contact Person Model


class ContactPerson(db.Model):
    """
    This is ContactPerson Model which store a information about the contactPerson of company
        - company_id is foreign key from company table to recognize the person from which company
        - email shoul be unique
        - If status is False then that contactPerson is consider as Deleted or deactive
    """
    __tablename__ = 'contact_persons'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), default="")
    last_name = db.Column(db.String(25), default="")
    email = db.Column(db.String(50), unique=True, nullable=False)
    contactNo = db.Column(db.String(10), default="")
    # company_id is Foreign key from company table
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))


class EmailTemplates(db.Model):
    """
        This is EmailTemplates model which store a sample email templates in database
            - If status is False then that user is consider as Deleted or deactive
    """
    __tablename__ = "email_templates"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), default="")
    subject = db.Column(db.String(50), default="")
    containt = db.Column(db.String(250), default="")
    isForAll = db.Column(db.Boolean,  default=False)
    status = db.Column(db.Boolean, default=False)


class Product(db.Model):
    """
       This is Product Model which store a information about the Products
           - diameter and capcity feilds are not applicable for all products, In that case it set to its default value
           - Price and name should not to be blank
           - Stock show us a how much quantity we have of that products
           - If status is False then that Product is consider as Deleted or deactive
    """
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    HSCcode = db.Column(db.String(30), default="")
    product_type = db.Column(db.String(30), default="")
    weight = db.Column(db.Float, default=0.0)
    top_diameter = db.Column(db.Float, default=0.0)
    Bottom_diameter = db.Column(db.Float, default=0.0)
    water_capcity = db.Column(db.Float, default=0.0)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    status = db.Column(db.Boolean, default=True, nullable=False)
    # Defining a relationship with InventryProducts
    inventry_products = db.relationship(
        "InventryProduct", backref="inventry_products", lazy="dynamic")
    # defining Relationship with QuotationProducts table
    quotations = db.relationship(
        "QuotationProducts", backref="quotation_products", lazy="dynamic")


# InventryProduct Model
class InventryProduct(db.Model):
    """
       This is InventryProduct Model which store a information about the Products import nad export.
           - product_id is foreign key from products table to recognize which product is imported/exported
           - company_id is foreign key from company table to recognize from which company we import/export a products
           - date and time show on wich date and on what time deal is done
           - If status is False then that entry is consider as Deleted or deactive
    """
    __tablename__ = "inventry_products"

    id = db.Column(db.Integer, primary_key=True)
    # product_id is Foreign Key from Products table
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer, default=0, nullable=False)
    # Type should be IMPORT or EXPORT
    type = db.Column(db.String(10), default="None")
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    # compnay_id is Foreign Key from Company table
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))


class Quotation(db.Model):
    """
       This is Quotation Model which store a information about all Quotation which made for company on the visits.
           - company_id is foreign key from company table to recognize quotation is for which company
           - user_id is Foreign key from users table to recognize which user added this
           - No_of_products and price show total no products in quotaion and there total price
           - If status is False then that entry is consider as Deleted or deactive
    """
    __tablename__ = "quotations"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    no_of_products = db.Column(db.Integer, default=0)
    total_price = db.Column(db.Float, default=0.0)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    # defining Relationship with QuotationProducts
    quotation_products = db.relationship(
        "QuotationProducts", backref="quotation_products", lazy="dynamic")


# Quotation_Products Model
class QuotationProducts(db.Model):
    """
       This is Quotation_Products Model which store a information about all Quotation_products
           - products_id is foreign key from products table to recognize this quotation is for which Product
           - quotation_id is foreign key from products table to recognize this entry is for which Quotations
           - price store updated or default value for selected Product
           - If status is False then that entry is consider as Deleted or deactive
    """
    __tablename__ = "quotation_products"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    price = db.Column(db.Float, nullable=False)
    quotation_id = db.Column(db.Integer, db.ForeignKey('quotations.id'))


class Todos(db.Model):
    """
        This is Todos Model which store a todos/Tasks which is created by user
            - it contain date and time on which it create
            - it contain date and time on which task is plan
            - If status is False then that entry is consider as Deleted or deactive
    """
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250), default="")
    create_date = db.Column(db.Date, nullable=False)
    create_time = db.Column(db.Time, nullable=False)
    plan_date = db.Column(db.Date, nullable=False)
    plan_time = db.Column(db.Time, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.Boolean, default=True)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
