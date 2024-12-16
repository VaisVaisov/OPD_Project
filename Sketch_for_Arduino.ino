#define sensor_pin A0
void setup() {
  pinMode(sensor_pin, INPUT);
  Serial.begin(115200);
  threshold = 512;
}

void loop() {
  sensor_value = byte(analogRead(sensor_pin));
  if (sensor_value > threshold){
    Serial.println(sensor_value);
  }
}