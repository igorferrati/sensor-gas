#define sensorAnalogico A0
#define ledverde 4
#define ledvermelho 3

void setup() {
  pinMode(sensorDigital, INPUT);
  pinMode(ledverde, OUTPUT);
  pinMode(ledvermelho, OUTPUT);
  Serial.begin(9600);
  digitalWrite(ledverde, LOW);
  digitalWrite(ledvermelho, LOW);
}

void loop() {
  int ValorA = analogRead(sensorAnalogico);

  if (ValorA <= 40) {
    Serial.print("Sensor Analogico: ");
    Serial.println(ValorA);
    Serial.println("Qualidade do ar normal");
    digitalWrite(ledverde, HIGH);
    digitalWrite(ledvermelho, LOW);
  } 
  else if (ValorA > 40 && ValorA <= 75) {
    Serial.print("Sensor Analogico: ");
    Serial.println(ValorA);
    Serial.println("ATENCAO: Presença de gases nocivos no ar");
    digitalWrite(ledverde, LOW);
    digitalWrite(ledvermelho, LOW);
  } 
  else {
    Serial.print("Sensor Analogico: ");
    Serial.println(ValorA);
    Serial.println("CUIDADO: Qualidade do ar comprometida");
    digitalWrite(ledvermelho, HIGH);
    digitalWrite(ledverde, LOW);
  }

  delay(2000);
}