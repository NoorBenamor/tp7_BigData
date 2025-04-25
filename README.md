# مشروع مراقبة الآلات باستخدام Apache Kafka

##  نظرة عامة

هذا المشروع يقدم نظام مراقبة في الوقت الحقيقي للآلات باستخدام **Apache Kafka** كمنصة رسائل. يتم إرسال بيانات من حساسات (حقيقية أو محاكاة) إلى Kafka، حيث يتم استقبالها ومعالجتها لاكتشاف الأعطال أو مراقبة الأداء.

---

##  الهدف من المشروع

- محاكاة أو استقبال بيانات من حساسات متصلة بآلات صناعية.
- إرسال هذه البيانات إلى Kafka عبر منتج (Producer).
- قراءة وتحليل البيانات عبر مستهلك (Consumer).
- اكتشاف الحالات غير الطبيعية مثل: ارتفاع الحرارة أو اهتزاز زائد.

---

## خطوات العمل 
داخل cmd لملف kafka ننفذ هذه الاوامر :
1/ تشغيل Apache Kafka على Windows 
تشغيل Zookeeper :
`.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties`

-------------
تشغيل Kafka Broker :
`.\bin\windows\kafka-server-start.bat .\config\server.properties`

--------------------
 إنشاء موضوع (Topic) في Kafka :
 `.\bin\windows\kafka-topics.bat --create --topic my-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`

 -----------------
 عرض جميع الـ Topics :
 `.\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092`

 ----------------
 تشغيل مستهلك Kafka (Consumer) :
 `.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic my-topic --from-beginning`

 ----------------
 تشغيل منتج Kafka (Producer) :
 `.\bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic my-topic`

 ---------------------
 ارسال بيانات مثل : `{"status": "running", "temperature": 65}`
 ![kafka](https://github.com/user-attachments/assets/61de61da-6e5b-437d-98dd-4b3eb1928a3d)

 -------------

 ![kafka2](https://github.com/user-attachments/assets/b4585baf-f996-41f6-9020-131df8489dd1)


 
