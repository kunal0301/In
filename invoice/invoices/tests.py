from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail
# Create your tests here.



class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice = Invoice.objects.create(date='2024-02-17', customer_name='Test Customer')
        self.invoice_detail = InvoiceDetail.objects.create(
            invoice=self.invoice,
            description='Test Description',
            quantity=1,
            unit_price=10,
            price=10
        )

    def test_get_invoices(self):
        response = self.client.get('/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invoice(self):
        data = {
            'date': '2024-02-17',
            'customer_name': 'New Customer',

            'description': 'New Description',
            'quantity': 2,
            'unit_price': 15,
            'price': 30
        }
        response = self.client.post('/invoices/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_invoice(self):
        data = {
            'date': '2024-02-17',
            'customer_name': 'Updated Customer',
            'description': 'Updated Description',
            'quantity': 2,
            'unit_price': 15,
            'price': 30

        }
        response = self.client.put(f'/invoices/{self.invoice.id}/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_invoice(self):
        response = self.client.delete(f'/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
