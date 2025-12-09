# Adapter Pattern in Real Software How it work Pyment System
# class PayPal:
#     def send_payment(self, amount):
#         print(f"PayPal payment: {amount}")

# class Stripe:
#     def make_payment(self, amount):
#         print(f"Stripe payment: {amount}")

# class PayPalAdapter:
#     def __init__(self, paypal):
#         self.paypal = paypal
#     def pay(self, amount):
#         self.paypal.send_payment(amount)

# class StripeAdapter:
#     def __init__(self, stripe):
#         self.stripe = stripe
#     def pay(self, amount):
#         self.stripe.make_payment(amount)

# # Client code uses same interface
# payments = [PayPalAdapter(PayPal()), StripeAdapter(Stripe())]
# for payment in payments:
#     payment.pay(100)
