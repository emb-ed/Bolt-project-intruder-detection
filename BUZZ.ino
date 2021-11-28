volatile int flag = 0;
uint8_t comp = B0000100;
int Buzzer = A0;



void setup() {
  // put your setup code here, to run once:

  DDRD &= ~B100;
  PCICR |= B00000100;
  PCMSK2 |= B00000100;

  pinMode(Buzzer, OUTPUT);
  

}

void buzz()
{
  digitalWrite(A0, HIGH);
  delay(1000);
  digitalWrite(A0,LOW);
}

ISR(PCINT2_vect)
{
  if (PIND & comp)
  {
    if (!flag)
    { 
      flag = 1;
      buzz();
      
    }

  }
  else {
    flag = 0 ;
  }
}

void loop() {

}
