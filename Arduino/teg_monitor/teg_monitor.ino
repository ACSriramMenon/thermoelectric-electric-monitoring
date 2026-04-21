void setup(){
  Serial.begin(9600);
}

void loop(){
  int rawTemp = analogRead(A0);
  int rawVolt = analogRead(A1);

  float temperature = rawTemp * (5.0 / 1023.0) * 100.0;
  float voltage = rawVolt * (5.0 / 1023.0);

  Serial.print("Temperature:");
  Serial.print(temperature, 2);
  Serial.print(", Voltage:");
  Serial.println(voltage, 2);

  delay(1000);
}