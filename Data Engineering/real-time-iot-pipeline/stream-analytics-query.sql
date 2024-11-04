SELECT
    device_id,
    System.Timestamp AS event_time,
    AVG(temperature) AS avg_temp,
    AVG(humidity) AS avg_humidity,
    MAX(air_quality) AS max_air_quality
INTO
    [iot-hub-sql]
FROM
    [iot-hub-environment]
GROUP BY
    device_id, TumblingWindow(second, 10)