from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'machine-data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("بدأ المستهلك في الاستماع إلى الرسائل...")
try:
    for message in consumer:
        print(f"الموضوع: {message.topic}, القسم: {message.partition}, الإزاحة: {message.offset}, القيمة: {message.value}")
except KeyboardInterrupt:
    print("تم إيقاف المستهلك.")
finally:
    consumer.close()
