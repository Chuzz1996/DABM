void setup() {
  // put your setup code here, to run once:
  pinMode(12,OUTPUT);
  pinMode(11,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()){
    char lecturaSerial = Serial.read();
    if(lecturaSerial== 'V'){
      digitalWrite(12,HIGH);
    }else if(lecturaSerial== 'v'){
      digitalWrite(12,LOW);
    }else if(lecturaSerial== 'L'){
      digitalWrite(11,HIGH);
    }else if(lecturaSerial== 'l'){
      digitalWrite(11,LOW);
    }
  }

}

