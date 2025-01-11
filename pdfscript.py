from datetime import datetime
from django.template.loader import get_template
from django.conf import settings
import pdfkit
from orders.models import *
from utils.utility import *
order = Order.objects.last()
generateOrderPdf(order, order.getOrderData())


def generateOrderPdf(instance,data):
    dynamic_directory_name = f"public/static/pdfs/{instance.order_id}.pdf"
    template_name = "invoice"

    options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    
    'no-outline': None
}
    path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    template = get_template(f"{template_name}.html")
    content = template.render(data)
    exact_file_path = f"{settings.BASE_DIR}/{dynamic_directory_name}"
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_string(content, exact_file_path, options = options, configuration=config)