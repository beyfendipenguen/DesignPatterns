"""
Senaryo: Sipariş Süreci Yönetimi

Bir e-ticaret sisteminde, farklı ödeme yöntemleri (Kredi Kartı, PayPal, Kripto vb.) ile sipariş alma sürecini yönetmek istiyorsun.
Her siparişin temel adımları aynı olacak ancak ödeme yöntemi farklı olabilecek.

Genel Sipariş Akışı:

    Sipariş detaylarını doğrula
    Ödeme işlemini gerçekleştir (Bu adım her ödeme yöntemi için farklı)
    Siparişi tamamla

"""
from accounts.paypal_account import PaypalAccount
from orders.paypal_order import PaypalOrder

def main():
    account = PaypalAccount(5000)
    print("Account is created")
    order = PaypalOrder(account)
    order.place_order(500)

if __name__ == "__main__":
    main()
