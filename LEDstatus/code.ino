void setup(){
  Serial.begin(9600);
  pinMode(13, OUTPUT);
 
}

void loop(){ 
   
    digitalWrite(13, HIGH);
    Serial.write('1');
    delay(1000); 
               
    digitalWrite(13, LOW);
    Serial.write('0');
    delay(1000);
} 
