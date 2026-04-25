void setup() {
  Serial.begin(9600);
}

void loop() {
  int AnalogTemp = analogRead(A0);
  int AnalogVolt = analogRead(A1);

  float temperature = AnalogTemp * (5.0 / 1023.0) * 100.0;
  float voltage = AnalogVolt * (5.0 / 1023.0);

  Serial.print("Temp:");
  Serial.print(temperature, 2);
  Serial.print(",Volt:");
  Serial.println(voltage, 2);

  delay(1000);
}