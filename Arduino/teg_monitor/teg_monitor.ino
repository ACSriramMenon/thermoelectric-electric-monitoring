void setup(){
  Serial.begin(9600);
}

//Loop runs infinitely

void loop(){
  int AnalogTemp = analogRead(A0);      //Reads temperature analog value
  int AnalogVolt = analogRead(A1);      //Reads Voltage analog value

  float temperature = AnalogTemp * (5.0 / 1023.0) * 100.0;    //Converts temperature analog value to Temperature value
  float voltage = AnalogVolt * (5.0 / 1023.0);                //Converts voltage analog value to Voltage value

  Serial.print("Temperature:");
  Serial.print(temperature, 2);       //Returns temperature with 2 decimal
  Serial.print(", Voltage:");         //Returns voltage with 2 decimal
  Serial.println(voltage, 2);

  delay(1000);
}