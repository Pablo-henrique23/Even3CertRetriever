from utils import *

print("[#] Trocou o cookie, ne?\n\n")

first_cert_page = get_certificate_list()
cert_select_for_payment_page = get_select_for_payment_page(first_cert_page)
data = find_data(cert_select_for_payment_page)

create_output(data)
