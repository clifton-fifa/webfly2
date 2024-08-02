from django.test import TestCase
from django.urls import reverse
from .models import YourModel

class YourModelTests(TestCase):
    
    def setUp(self):
        # สร้างข้อมูลทดสอบที่ใช้ในการทดสอบ
        YourModel.objects.create(field1='value1', field2='value2')
    
    def test_model_creation(self):
        # ทดสอบการสร้างโมเดล
        obj = YourModel.objects.get(field1='value1')
        self.assertEqual(obj.field2, 'value2')

class YourViewTests(TestCase):
    
    def test_view_status_code(self):
        # ทดสอบสถานะการตอบกลับของวิว
        url = reverse('your_view_name')  # เปลี่ยนเป็นชื่อวิวของคุณ
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_template_used(self):
        # ทดสอบว่าชื่อเทมเพลตที่ถูกใช้ถูกต้องหรือไม่
        url = reverse('your_view_name')  # เปลี่ยนเป็นชื่อวิวของคุณ
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'your_template_name.html')  # เปลี่ยนเป็นชื่อเทมเพลตของคุณ

class YourFormTests(TestCase):
    
    def test_form_validity(self):
        # ทดสอบความถูกต้องของฟอร์ม
        form_data = {'field1': 'value1', 'field2': 'value2'}
        form = YourForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalidity(self):
        # ทดสอบความไม่ถูกต้องของฟอร์ม
        form_data = {'field1': 'value1'}  # ข้อมูลที่ไม่ครบถ้วน
        form = YourForm(data=form_data)
        self.assertFalse(form.is_valid())
