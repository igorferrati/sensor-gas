#define sensorDigital 9
#define sebsirAnalogico A0
#define ledverde 5
#define ledvermelho 3

void setup() {
  pinMode(sensorDigital, INPUT);
  pinMode(ledverde, OUTPUT);
  pinMode(ledvermelho, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int ValorD = digitalRead(sensorDigital);
  int ValorA = analogRead(sebsirAnalogico);

  Serial.println("Sensor Analogico:");
  Serial.println(ValorA);
  Serial.println("Sensor Digital:");
  Serial.println(ValorD);

  if (ValorA < 1) {
    Serial.println("LUZ VERDE");
    digitalWrite(ledverde, HIGH);
  } else {
    Serial.println("LUZ VERMELHA");
    digitalWrite(ledvermelho, HIGH);
  }

  delay(200);
}