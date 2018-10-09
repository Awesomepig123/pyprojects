//bbccccc
// Hardware: Grove - Ear-clip Heart Rate Sensor, Grove - Base Shield, Grove - LED
// Also Grove Galvanic Skin Response Sensor
// by www.seeedstudio.com

// Working combined GSR and heartrate, CoderDojo Athenry

#include<Keyboard.h>

// Initiate GSR
//const int BUZZER=3;
const int GSR=A2;
int threshold=0;
int sensorValue;


// Initiate heart rate

unsigned int heartpin = 3; // D3 Digital Pin 3
unsigned char ledpin = 13; // heartrate LED
unsigned char counter=0;
unsigned int heart_rate=0; 
unsigned long temp[21];
unsigned long sub=0;
volatile unsigned char state = LOW; // LED state
bool data_effect=true;
const int max_heartpluse_duty=2000; //you can change it follow your system's request.2000 meams 2 seconds, heart rate is 60/2. System return error if the duty overtrip 2 second.

void setup()
{
  Keyboard.begin();



  // Setup for GSR
  
  long sum=0;
  Serial.begin(9600);
  //pinMode(BUZZER,OUTPUT);
  //digitalWrite(BUZZER,LOW);
  delay(1000);

  for(int i=0;i<500;i++)
  {
    sensorValue=analogRead(GSR);
    sum += sensorValue;
    delay(5);
  }
  threshold = sum/500;
  Serial.print("GSR threshold =");
  Serial.println(threshold);

  
  // Setup for heartrate
  pinMode(ledpin, OUTPUT);
  Serial.begin(9600);
  Serial.println("Please attach heart rate ear clip.");
  delay(5000);//wait finger press ready
  array_init();
  Serial.println("Beginning to test heart rate.");
  attachInterrupt(digitalPinToInterrupt(heartpin), interrupt, RISING);//set interrupt 0,digital port 2
}


void loop()
{
  // Loop for GSR
  int temp;

  int outthreshold = 10000;
  static int outcount = 0;
  outcount++;
  
  sensorValue=analogRead(GSR);
  if (outcount >= outthreshold) {
    Serial.print("MM GSR sensorValue=");
    Serial.println(sensorValue);
    outcount=0;
  }
  
  temp = threshold - sensorValue;
  
  if(abs(temp)>50)
  {
    sensorValue=analogRead(GSR);
    temp = threshold - sensorValue;
    if(abs(temp)>50)
    {
      //digitalWrite(BUZZER,HIGH);
      Serial.println("GSR Stress detected!");
      delay(3000);
      //digitalWrite(BUZZER,LOW);
      delay(1000);
    }
  }

  // Loop for heartrate - just flashes LED if attached
  digitalWrite(ledpin, state); // flash LED
}

void sum()  //calculate the heart rate
{
 if(data_effect)
    {
      heart_rate=1200000/(temp[20]-temp[0]);//60*20*1000/20_total_time 
      Serial.print("Heart_rate_is:\t");
      Serial.println(heart_rate);
     
      if (heart_rate>95 && heart_rate <200) {
        Keyboard.press('c');
        delay(10);
        Keyboard.release('c');
      }
       if (heart_rate>85 && heart_rate <95) {
        Keyboard.press('b');
        delay(10);
        Keyboard.release('b');
      }
       if (heart_rate>0 && heart_rate <85) {
        Keyboard.press('a');
        delay(10);
        Keyboard.release('a');
      }
    }
   data_effect=1;//sign bit
}


/* Interrupt service routine. Get the sigal from the external interrupt. */
void interrupt()
{
    temp[counter]=millis(); //get sys time
    state = !state;    //change LED status

    // commenting out number display
    // Serial.println(counter,DEC);
    // Serial.println(temp[counter]); 
    switch(counter)
      {
       case(0):
         sub=temp[counter]-temp[20];
         // Serial.println(sub);
         break;
       default:
         sub=temp[counter]-temp[counter-1];
         //Serial.println(sub);
         break;
      }

    if(sub>max_heartpluse_duty) //set 2 seconds as max heart pluse duty
    {
        data_effect=0;//sign bit
        counter=0;
        Serial.println("Heart rate measure error,test will restart!" );
        array_init();
    }
    
    if (counter==20 && data_effect)
    {
      counter=0;
      sum();
    }
    else if(counter!=20 && data_effect) 
    {
      counter++;
    }
    else 
    {
      counter=0;
      data_effect=1;
    }
}

/** Initialise array used to store heartrate data **/
void array_init()
{
  for(unsigned char i=0;i!=20;++i)
  {
    temp[i]=0;
  }
  temp[20]=millis();
}


