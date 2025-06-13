import os
import json
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QStackedWidget, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from datetime import datetime
import random

USERS_FILE = "users.json"
CART_FILE = "cart.json"
TICKETS_FILE = "tickets.json"

def load_tickets():
    if os.path.exists(TICKETS_FILE):
        with open(TICKETS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tickets(tickets):
    with open(TICKETS_FILE, "w") as f:
        json.dump(tickets, f, indent=4)

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def save_cart(user_id, cart_items):
    total = sum(item["price"] for item in cart_items)
    data = {}
    if os.path.exists(CART_FILE):
        try:
            with open(CART_FILE, "r") as f:
                data = json.load(f)
                if not isinstance(data, dict):
                    data = {}
        except json.JSONDecodeError:
            data = {}
    
    data[user_id] = {
        "items": cart_items,
        "total": total
    }

    with open(CART_FILE, "w") as f:
        json.dump(data, f)

def load_cart(user_id):
    try:
        if os.path.exists(CART_FILE):
            with open(CART_FILE, "r") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return data.get(user_id, {"items": [], "total": 0})
    except Exception as e:
        print(f"Error cargando carrito: {e}")
    return {"items": [], "total": 0}

products = [
    {"name": "Sudadera Oversize con Gráficos Grandes", "price": 750,"id":"0"},
    {"name": "Sudadera con Parche Bordado + Capucha Forrada", "price": 1100,"id":"1"},
    {"name": "Sudadera Tie-Dye con Zipper Lateral", "price": 950,"id":"2"},
    {"name": "Sudadera Minimalista con Toques Techwear", "price": 1400,"id":"3"}
]
TotalPrice = 0
ShowPass = False

class LoginScreen(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("loginscreen.ui", self)
        self.loginbutton.clicked.connect(self.login)
        self.registerbutton.clicked.connect(self.goto_register)
        self.showpassword.clicked.connect(self.togglepassword)
    
    def reset_fields(self):
        self.name.clear()
        self.password.clear()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)


    def togglepassword(self):
        global ShowPass
        if ShowPass == False:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
            ShowPass = True
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
            ShowPass = False

    def login(self):
        users = load_users()
        name = self.name.text()
        password = self.password.text()
        for user_id, user in users.items():
            if user["name"] == name and user["password"] == password:
                store = StoreScreen(user_id)
                widget.addWidget(store)
                widget.setCurrentWidget(store)
                login = widget.widget(0)
                login.reset_fields()
                return
        QMessageBox.warning(self, "Error", "Correo o contraseña incorrectos")


    def goto_register(self):
        register = RegisterScreen()
        widget.addWidget(register)
        widget.setCurrentWidget(register)

class RegisterScreen(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("registerscreen.ui", self)
        self.signupbutton.clicked.connect(self.register)

    def register(self):
        users = load_users()
        name = self.name.text()
        password = self.password.text()
        confirm = self.confirm.text()
        if password != confirm:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden")
            return
        user_id = str(len(users) + 1)
        users[user_id] = {"name": name, "password": password}
        save_users(users)
        QMessageBox.information(self, "Éxito", "Cuenta creada correctamente")
        widget.setCurrentIndex(0)

class StoreScreen(QDialog):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi("store.ui", self)
        self.user_id = user_id
        carrito_data = load_cart(user_id)
        self.carrito = carrito_data["items"]


        self.addbutton1.clicked.connect(lambda: self.add_to_cart(products[0]))
        self.addbutton2.clicked.connect(lambda: self.add_to_cart(products[1]))
        self.addbutton3.clicked.connect(lambda: self.add_to_cart(products[2]))
        self.addbutton4.clicked.connect(lambda: self.add_to_cart(products[3]))
        self.cartbutton.clicked.connect(self.show_cart)
        self.closesession.clicked.connect(self.logout)

        widget.setFixedSize(834, 903)

    def add_to_cart(self, product):
        self.carrito.append(product)
        save_cart(self.user_id, self.carrito)
        QMessageBox.information(self, "Agregado", f"{product['name']} añadido al carrito.")

    def show_cart(self):
        cart = CartScreen(self.user_id)
        cart.store_screen = self
        widget.addWidget(cart)
        widget.setCurrentWidget(cart)
    
    def logout(self):
        widget.setCurrentIndex(0)
        widget.setFixedSize(519, 368)

class CartScreen(QDialog):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi("cart.ui", self)
        self.user_id = user_id
        carrito_data = load_cart(user_id)
        self.carrito = carrito_data["items"]
        self.total_price = carrito_data["total"]


        self.back.clicked.connect(self.go_back)
        self.deletecart.clicked.connect(self.delete_cart)
        self.buyall.clicked.connect(self.buy_all)

        self.populate_cart()
        
        self.setMinimumSize(675, 590)
        self.setMaximumSize(16777215, 16777215)
        
        self.total.setText(f"${self.total_price}")
    
    def populate_cart(self):
        contents = self.scrollArea.widget()

        for child in contents.findChildren(QWidget):
            child.setParent(None)

        y_offset = 0
        item_height = 120

        for item in self.carrito:
            item_widget = uic.loadUi("item.ui")
            item_widget.setParent(contents)

            item_widget.name.setText(item["name"])
            item_widget.price.setText(f"${item['price']}")
            img_path = f"sweater{item['id']}.png"
            if os.path.exists(img_path):
                pixmap = QPixmap(img_path)
                item_widget.image.setPixmap(pixmap.scaled(100, 100))

            item_widget.setGeometry(0, y_offset, contents.width(), item_height)
            y_offset += item_height + 10

            print("Item Añadido")

        contents.setMinimumHeight(y_offset)
    
    def delete_cart(self):
        self.carrito = []
        save_cart(self.user_id, self.carrito)
        QMessageBox.information(self, "Carrito eliminado", "Tu carrito ha sido vaciado.")
        self.populate_cart()

    def buy_all(self):
        if not self.carrito:
            QMessageBox.warning(self, "Carrito vacío", "No hay productos para comprar.")
            return

        buy_screen = BuyScreen(self.user_id, self.carrito, self.total_price, self)
        widget.addWidget(buy_screen)
        widget.setCurrentWidget(buy_screen)

    def go_back(self):
        store = StoreScreen(self.user_id)
        widget.addWidget(store)
        widget.setCurrentWidget(store)
        widget.setFixedSize(834, 903)

class BuyScreen(QDialog):
    def __init__(self, user_id, carrito, total, cart_screen):
        super().__init__()
        uic.loadUi("buy.ui", self)
        self.user_id = user_id
        self.carrito = carrito
        self.total = total
        self.cart_screen = cart_screen

        self.cancelbuy.clicked.connect(self.cancel_purchase)
        self.confirmbuy.clicked.connect(self.confirm_purchase)

    def cancel_purchase(self):
        widget.setCurrentWidget(self.cart_screen)

    def confirm_purchase(self):
        ticket_screen = TicketScreen(self.user_id, self.carrito, self.total)
        widget.addWidget(ticket_screen)
        widget.setCurrentWidget(ticket_screen)

class TicketScreen(QDialog):
    def __init__(self, user_id, carrito, total):
        super().__init__()
        uic.loadUi("ticket.ui", self)
        self.user_id = user_id

        tickets = load_tickets()
        existing_ids = {t["id"] for t in tickets}

        ticket_id = random.randint(1000, 9999)
        while ticket_id in existing_ids:
            ticket_id = random.randint(1000, 9999)

        fecha = datetime.now().strftime("%d/%m/%Y")
        self.ticketHeader.setText(f"[SubUrban Shop]\nVenta realizada el {fecha}\nTicket {ticket_id}\n------------------------")

        iva_total = 0
        layout = self.findChild(QVBoxLayout, "ticketListWidget")

        for item in carrito:
            nombre = item["name"]
            precio = item["price"]
            item_id = item["id"]
            iva = round(precio * 0.16, 2)
            iva_total += iva

            label = QLabel(f"{nombre}  {item_id}  ${precio}")
            layout.addWidget(label)

        self.ticketFooter.setText(f"Total: ${total}\nIVA: ${round(iva_total, 2)}")

        tickets.append({
            "id": ticket_id,
            "user_id": user_id,
            "fecha": fecha,
            "items": carrito,
            "total": total,
            "iva_total": round(iva_total, 2)
        })
        save_tickets(tickets)

        self.accept.clicked.connect(self.back_to_cart)

    def back_to_cart(self):
        save_cart(self.user_id, [])
        cart_screen = CartScreen(self.user_id)
        widget.addWidget(cart_screen)
        widget.setCurrentWidget(cart_screen)
        QMessageBox.information(self, "Gracias", "Gracias por su compra.")

app = QApplication([])
app.setApplicationName("Suburban Shop")
app.setWindowIcon(QtGui.QIcon("logo.png"))
widget = QStackedWidget()
login = LoginScreen()
widget.addWidget(login)
widget.setFixedSize(600, 400)
widget.show()
app.exec_()
