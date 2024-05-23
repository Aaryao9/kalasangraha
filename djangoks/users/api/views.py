from ..models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password  
import jwt
import datetime
from ..models import *



class signupView (APIView):
    permission_classes = []
    authentication_classes = []
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(email=email).exists():
            return Response({'error': 'email already exists'})
        
        hashed_password = make_password(password)
        print (hashed_password)
        user=User(username=username,email=email,password=hashed_password)   
        user.save()
        return Response({'success': 'account created'})    
    
class loginView (APIView):
        permission_classes = []
        authentication_classes = []
        def post(self, request):
            email = request.data.get('email')
            password = request.data.get('password')
            try:
                 user = User.objects.filter(email=email).first()
            except User.DoesNotExist:
               return Response({'error': 'Invalid email'})
            cp= check_password(password, user.password)
            if cp==False:
                return Response({'error': 'Invalid password'})
            else:
                now=datetime.datetime.now(datetime.timezone.utc)
                expire=now+datetime.timedelta(days=1)
                payload = {
                    'id': user.id,
                    'email': user.email,
                    'username': user.username,
                    'exp': expire,
                    'iat': now
                }

                token = jwt.encode(payload, 'SECRET', algorithm='HS256')
                response= Response()
                
                response.data = {
                    'message'  : 'login success',
                    'jwt': token
                }
                return response
            
class profileView (APIView):
    permission_classes = []
    authentication_classes = []
    def get(self, request):
        token = request.GET.get('jwt',None)
        if not token:
            return Response({'error': 'not authenticated'})
        try:
            payload = jwt.decode(token, 'SECRET', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'error': 'expired'})
        except jwt.InvalidTokenError:
            return Response({'error': 'invalid'})
        user = User.objects.filter(id=payload['id']).first()
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        return Response(user_data)

class logoutView (APIView):
    permission_classes = []
    authentication_classes = []
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        } 
        return response
class categoryView(APIView):
    permission_classes = []
    authentication_classes = []
    
    def get(self, request):
        categories = Category.objects.all()
        data = []
        for category in categories:
            data.append({
                'id': category.id,
                'name': category.name
            })
        return Response(data)
    
class productView(APIView):
    permission_classes = []
    authentication_classes = []
  
    def get(self, request):
        products = Product.objects.all()
        data = []
        for product in products:
            data.append({
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'image': product.image.url,
                'sold': product.sold,
                'stock': product.stock,
                'seller': product.seller,
                'listedin': product.listedin,
                'discount': product.discount,
                'category': product.Category.name
            })
        return Response(data)
    
    def post(self, request):
        name = request.data.get('name')
        price = request.data.get('price')
        description = request.data.get('description')
        image = request.data.get('image')
        sold = request.data.get('sold')
        stock = request.data.get('stock')
        seller = request.data.get('seller')
        listedin = request.data.get('listedin')
        discount = request.data.get('discount')
        category_id = request.data.get('category_id')
        category = Category.objects.filter(id=category_id).first()
        product = Product(name=name, price=price, description=description, image=image, sold=sold, stock=stock, seller=seller, listedin=listedin, discount=discount, Category=category)
        product.save()
        return Response({'success': 'product created'})
    
    
    


class cartView(APIView):
    permission_classes = []
    authentication_classes = []
    
    def get(self, request):
        token = request.GET.get('jwt',None)
        if not token:
            return Response({'error': 'not authenticated'})
        try:
            payload = jwt.decode(token, 'SECRET', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'error': 'expired'})
        except jwt.InvalidTokenError:
            return Response({'error': 'invalid'})
        user = User.objects.filter(id=payload['id']).first()
        cart = Cart.objects.filter(user=user).first()
        cart_items = CartItems.objects.filter(user=user)
        data = []
        for cart_item in cart_items:
            data.append({
                'id': cart_item.id,
                'product': cart_item.product.name,
                'quantity': cart_item.quantity,
                'price': cart_item.price
            })
        return Response(data)
    
    
    
    def delete(self, request):
        token = request.GET.get('jwt',None)
        if not token:
            return Response({'error': 'not authenticated'})
        try:
            payload = jwt.decode(token, 'SECRET', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'error': 'expired'})
        except jwt.InvalidTokenError:
            return Response({'error': 'invalid'})
        user = User.objects.filter(id=payload['id']).first()
        product_id = request.data.get('product_id')
        product = Product.objects.filter(id=product_id).first()
        cart = Cart.objects.filter(user=user).first()
        cart_item = CartItems.objects.filter(product=product, user=user).first()
        cart.products.remove(cart_item)
        cart_item.delete()
        return Response({'success': 'removed from cart'})

class orderView(APIView):
    permission_classes = []
    authentication_classes = []
    
    def get(self, request):
        token = request.GET.get('jwt',None)
        if not token:
            return Response({'error': 'not authenticated'})
        try:
            payload = jwt.decode(token, 'SECRET', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'error': 'expired'})
        except jwt.InvalidTokenError:
            return Response({'error': 'invalid'})
        user = User.objects.filter(id=payload['id']).first()
        orders = Order.objects.filter(user=user)
        data = []
        for order in orders:
            order_details = Orderdetails.objects.filter(order=order)
            order_data = []
            for order_detail in order_details:
                order_data.append({
                    'product': order_detail.product.name,
                    'quantity': order_detail.quantity,
                    'price': order_detail.price
                })
            data.append({
                'id': order.id,
                'order_details': order_data
            })
        return Response(data)
    
    def post(self, request):
        token = request.GET.get('jwt',None)
        if not token:
            return Response({'error': 'not authenticated'})
        try:
            payload = jwt.decode(token, 'SECRET', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'error': 'expired'})
        except jwt.InvalidTokenError:
            return Response({'error': 'invalid'})
        user = User.objects.filter(id=payload['id']).first()
        cart = Cart.objects.filter(user=user).first()
        cart_items = CartItems.objects.filter(user=user)
        order = Order(user=user)
        order.save()
        for cart_item in cart_items:
            order_detail = Orderdetails(product=cart_item.product, quantity=cart_item.quantity, price=cart_item.price, order=order)
            order_detail.save()
        cart.products.clear()
        return Response({'success': 'order placed'})
    
    
class bestsellerView(APIView):
    permission_classes = []
    authentication_classes = []
    
    def get(self, request):
        products = Product.objects.all().order_by('-sold')[:4]
        data = []
        for product in products:
            data.append({
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'image': product.image.url,
                'sold': product.sold,
                'stock': product.stock,
                'seller': product.seller,
                'listedin': product.listedin,
                'discount': product.discount,
                'category': product.Category.name
            })
        return Response(data)
    
class addtocartView(APIView):
    permission_classes = []
    authentication_classes = []
    
    def post(self, request):
        token = request.GET.get('jwt',None)
        if not token:
            return Response({'error': 'not authenticated'})
        try:
            payload = jwt.decode(token, 'SECRET', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'error': 'expired'})
        except jwt.InvalidTokenError:
            return Response({'error': 'invalid'})
        user = User.objects.filter(id=payload['id']).first()
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        product = Product.objects.filter(id=product_id).first()
        cart = Cart.objects.filter(user=user).first()
        cart_item = CartItems.objects.filter(product=product, user=user).first()
        if cart_item:
            cart_item.quantity += quantity
            cart_item.price = product.price * cart_item.quantity
            cart_item.save()
        else:
            cart_item = CartItems(product=product, quantity=quantity, price=product.price*quantity, user=user)
            cart_item.save()
        cart.products.add(cart_item)
        cart.save()
        return Response({'success': 'added to cart'})