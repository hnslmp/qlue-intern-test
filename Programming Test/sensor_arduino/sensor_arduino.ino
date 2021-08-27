/*
  Sensor Datalogger & Lamp switch
  by Hansel Matthew - FTUI'18

  Board: Arduino Uno
  Sensor: dht11 & Light dependent resistor

  Printed data: data number, timestamp using millis(),
  and acceleration on x,y,z axis. 
 */

#include "DHT.h" //Temp and Humidity Sensor Library

#define DHTPIN 2     // DHT Pin number

#define DHTTYPE DHT11   // DHT sensor type, i use DHT11 sensor

DHT dht(DHTPIN, DHTTYPE); //make dht object

float ADC_value = 0.0048828125; // ADC resolution
int lampPin = 11;

//Message variable
char msg[60];
char outstr_photosensor[15];
char outstr_humid[15];
char outstr_temp[15];

void setup() {
  Serial.begin(9600); //begin serial communication
  dht.begin(); //begin dht communication
  pinMode(lampPin,OUTPUT);
}

void loop() {
  delay(1000); //Sensor Reading Interval 1Ms

  if (Serial.available() > 0) {
    //Only run when it receive data
    
    //Convert string msg to int
    int state = Serial.readString().toInt();

    //Turn ON/OFF the lamp
    if(state == 1){
      digitalWrite(lampPin,HIGH);
    }
    else if(state == 0){
      digitalWrite(lampPin,LOW);
    }
  }
  
  float LDR_value = analogRead(A0); //Read value from ldr
  float lux = (250.00/(ADC_value*LDR_value))-50.00; //Convert from analog value into lux

/*If using own temperature and humidity sensor
    //Input
// int humid = analogRead(A1);
// int temp = analogRead(A2);

    //Scaling for celcius and percentage
// temp_scaled = temp*scaler_temp
// humid_scaled = humid*scaler_humid/100
*/
    
  //If using dht11 sensor
  float humid = dht.readHumidity(); //Read humidity (already in percentage)
  float temp = dht.readTemperature(); //Read temperature (already in celcius)

  dtostrf(lux, 7, 2, outstr_photosensor);  //Convert data from float/int to string for message transmission using sprintf()
  dtostrf(humid, 7, 2, outstr_humid);
  dtostrf(temp, 7, 2, outstr_temp);
  
  sprintf(msg, "%s %s %s", outstr_photosensor, outstr_humid, outstr_temp); //Encode message
  Serial.println(msg); //Send message
}
