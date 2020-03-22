unsigned char keyscan()
{
  while(1)
  {
        KEYPAD_PORT = 0XeF;
        delay(1000);  /////must for response at port when key press
        if((KEYPAD_PORT&0X01)==0){while((KEYPAD_PORT&0X01)==0); return 'C';}
        if((KEYPAD_PORT&0X02)==0){while((KEYPAD_PORT&0X02)==0); return '8';}
        if((KEYPAD_PORT&0X04)==0){while((KEYPAD_PORT&0X04)==0); return '4';}
        if((KEYPAD_PORT&0X08)==0){while((KEYPAD_PORT&0X08)==0); return '0';}

        KEYPAD_PORT = 0XdF;
        delay(1000);
        if((KEYPAD_PORT&0X01)==0){while((KEYPAD_PORT&0X01)==0); return 'D';}
        if((KEYPAD_PORT&0X02)==0){while((KEYPAD_PORT&0X02)==0); return '9';}
        if((KEYPAD_PORT&0X04)==0){while((KEYPAD_PORT&0X04)==0); return '5';}
        if((KEYPAD_PORT&0X08)==0){while((KEYPAD_PORT&0X08)==0); return '1'  ;}

        KEYPAD_PORT = 0XbF;
        delay(1000);
        if((KEYPAD_PORT&0X01)==0){while((KEYPAD_PORT&0X01)==0); return 'E';}
        if((KEYPAD_PORT&0X02)==0){while((KEYPAD_PORT&0X02)==0); return 'A';}
        if((KEYPAD_PORT&0X04)==0){while((KEYPAD_PORT&0X04)==0); return '6';}
        if((KEYPAD_PORT&0X08)==0){while((KEYPAD_PORT&0X08)==0); return '2';}

        KEYPAD_PORT = 0X7F;
        delay(1000);
        if((KEYPAD_PORT&0X01)==0){while((KEYPAD_PORT&0X01)==0); return 'F';}
        if((KEYPAD_PORT&0X02)==0){while((KEYPAD_PORT&0X02)==0); return 'B';}
        if((KEYPAD_PORT&0X04)==0){while((KEYPAD_PORT&0X04)==0); return '7';}
        if((KEYPAD_PORT&0X08)==0){while((KEYPAD_PORT&0X08)==0); return '3';}
   }
}