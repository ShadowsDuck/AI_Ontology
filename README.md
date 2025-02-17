ในการใช้งานโค้ดที่คุณให้มานั้น คุณต้องติดตั้งไลบรารีที่จำเป็นก่อน โดยใช้คำสั่ง `pip install` ดังนี้:

1. **Flask**: สำหรับการพัฒนาเว็บแอปพลิเคชัน
2. **rdflib**: สำหรับการทำงานกับไฟล์ RDF/OWL
3. **flask-cors**: สำหรับอนุญาตให้มีการทำงานข้ามโดเมน (Cross-Origin Resource Sharing)

โดยใช้คำสั่งติดตั้งเหล่านี้:

```bash
pip install flask rdflib flask-cors
```

หลังจากติดตั้งไลบรารีแล้ว ก็สามารถรันโปรเจกต์นี้ได้ตามปกติ

### ขั้นตอน:
1. ติดตั้งไลบรารีที่ต้องการ:
   ```bash
   pip install flask rdflib flask-cors
   ```

2. รัน Flask app ด้วยคำสั่ง:
   ```bash
   python app.py
   ```
