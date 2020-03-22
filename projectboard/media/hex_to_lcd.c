#include<reg51.h>
//////////// PIN DEFINED ///////////////
#define KEYPAD_PORT  P1
#define DATA P1
//control port2
sbit RS=P2^0;
sbit E=P2^1;
#include"delay.h"
#include"lcd.h"
#include"keypad.h"

void main(void)
{
  unsigned char key;
  init_lcd();                           //lcd init.
  cmd_lcd(0x80);                        //Set curser position
  string_lcd("Press key : ");        //Display string
  while(1)
  {
        cmd_lcd(0xc0);
        key = keyscan();                        //Scan keypad
        data_lcd(key);                                //Display pressed key on lcd
  }
}
