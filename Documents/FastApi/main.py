from fastapi import FastAPI
from models import Products
app = FastAPI()

@app.get("/")
def greet():
    return {"message": "Welcome to my website"}
    
products = [
    Products(id=1, name="Laptop", description="A high-end laptop", price=1500.00, quantity=10),
    Products(id=2, name="Smartphone", description="A latest model smartphone", price=800.00, quantity=25),
    Products(id=3, name="Headphones", description="Noise-cancelling headphones", price=200.00, quantity=50),
    Products(id=4, name="Monitor", description="4K UHD Monitor", price=400.00, quantity=15) ,
    Products(id=5, name="Keyboard", description="Mechanical keyboard", price=100.00, quantity=30)   
] 

@app.get("/products")
def get_all_products():
    return products

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
        
        return "Product not found"

# to post data
@app.post("/products")
def add_product(product: Products):
    products.append(product)
    return product