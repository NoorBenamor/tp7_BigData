from kafka import KafkaProducer
import json
import time
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

topic_name = 'machine-data'

try:
    for i in range(5):
        timestamp = datetime.now().isoformat()
        sensor_data = {
            'machine_id': 'machine-123',
            'timestamp': timestamp,
            'temperature': 25 + i * 2,
            'pressure': 100 + i * 5,
            'status': 'running' if i % 2 == 0 else 'idle'
        }

        producer.send(topic_name, value=sensor_data)
        print(f"تم إرسال: {sensor_data}")
        time.sleep(1)

except Exception as e:
    print(f"حدث خطأ أثناء الإرسال: {e}")

finally:
    producer.flush()
    producer.close()
