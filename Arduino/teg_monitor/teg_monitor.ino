void setup() {
  Serial.begin(9600);
}

void loop() {
  int AnalogVolt = analogRead(A1);

  float voltage = AnalogVolt * (5.0 / 1023.0) * 5;

  Serial.print(",Volt:");
  Serial.println(voltage, 2);

  delay(1000);
}