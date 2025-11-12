# RT-PC integration service with 1C

- Exchange CRM and 1C counterparties
- Generate an invoice in 1C with a click in CRM

Stack:
- Python3
- Fastapi
- Kafka
- Redpanda Console (kafka UI)

Services:
- kafka - file exchange, three topics:

1. Account_creation - data from the database
2. nomenclature_guid_updater - data from 1C
3. vin_updater - data from the database

- rest-api - service on fastapi - endpoint "api/account/{id}", retrieves data from the database by ID and passes it to the kafka topic (account_creation)
- guid_updater - service with a kafka consumer, which will wait for messages in the nomenclature_guid_updater topic and save them to the database
- vin_updater - a service with a Python script that will periodically retrieve NomenclatureForm data with a filled-in car_guid and send it to Kafka to populate VIN numbers in 1C Nomenclature.
- redpanda-ui - user UI (visualization of Kafka work)
