#include <LiquidCrystal.h>
#include <Keypad.h>

const byte ROW = 4;
const byte COLM = 4;
 
char AllKeys[ROW][COLM] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};
 
byte rowPin[ROW] = {9, 8, 7, 6};
byte colPin[COLM] = {5, 4, 3, 2};
 
Keypad K = Keypad(makeKeymap(AllKeys), rowPin, colPin, ROW, COLM);
 
LiquidCrystal lcd(10, 11, 12, 13, 14, 15);

void setup() {
  lcd.begin(16, 2);
}
 
void loop() {
  char Key = K.getKey();
 
  if (Key) {
    lcd.setCursor(0, 0);
    lcd.print(Key);
  }
}
