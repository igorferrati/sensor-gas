#define sensorDigital 9
#define sebsirAnalogico A0
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
  int ValorD = digitalRead(sensorDigital);
  int ValorA = analogRead(sebsirAnalogico);

  if (ValorA <= 40) {
    Serial.print("Sensor Analogico: ");
    Serial.println(ValorA);
    //Serial.print("Sensor Digital: ");
    //Serial.println(ValorD);
    Serial.println("Ar sem presenca de gases toxicos");
    digitalWrite(ledverde, HIGH);
    digitalWrite(ledvermelho, LOW);
  } else {
    Serial.print("Sensor Analogico: ");
    Serial.println(ValorA);
    //Serial.print("Sensor Digital: ");
    //Serial.println(ValorD);
    Serial.println("[ATENÇÃO] Qualidade do ar comprometida");
    digitalWrite(ledvermelho, HIGH);
    digitalWrite(ledverde, LOW);
  }

  delay(10000);
}