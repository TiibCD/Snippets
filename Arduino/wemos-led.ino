// original code here : https://github.com/CleverCloud/wemos-ws-led

#include <Adafruit_NeoPixel.h>    // https://github.com/adafruit/Adafruit_NeoPixel
#include <ESP8266WiFi.h>

#define PIXEL_COUNT       30

struct RGB {
  byte r;
  byte g;
  byte b;
};

Adafruit_NeoPixel strip = Adafruit_NeoPixel(PIXEL_COUNT, D4, NEO_GRB + NEO_KHZ800);
WiFiClient client;

RGB color;
RGB lastColor;
int scrolling;

bool connected;

void setup() {
  Serial.begin(9600); // Used for debugging messages

  // Initialize the colors
  lastColor = {0, 0, 0};
  color = {0, 0, 0};
  scrolling = 0;
  strip.begin();
  strip.show();

  // Connexion au wifi
}

void loop() {
  // If connection fails / breaks, the first LED blinks red
  if (!client.connected() || !connected) {
    renderLEDColor(0, {255, 0, 0});
    delay(500);
    renderLEDColor(0, {0, 0, 0});
    delay(500);
  } else if (scrolling > 0) { // If scrolling is greater than 0, render LEDs
    renderLED(strip.numPixels() - scrolling);
    delay(20);
    scrolling--;
  } else {
    // When receiving data, process it and start scrolling animation
    // Expected format is: RRRGGGBBB (as in 255000000, 035127078, ...)
    // There is no error handling
    String data;
    
    if (data.length() > 0) {
      Serial.print("Received: ");
      Serial.println(data);
      int red   = data.substring(0, 3).toInt() / 255.0 * 100;
      int green = data.substring(3, 6).toInt() / 255.0 * 100;
      int blue  = data.substring(6, 9).toInt() / 255.0 * 100;
      Serial.print("Red: ");
      Serial.println(red);
      Serial.print("Green: ");
      Serial.println(green);
      Serial.print("Blue: ");
      Serial.println(blue);

      // Update colors
      lastColor = color;
      color = {red, green, blue};

      // Start scrolling animation
      scrolling = strip.numPixels();
    }
  }
}


double diffAbs(byte last, byte current) {
  return (double) (last > current ? last - current : current - last);
}

byte computeValueAt(byte last, byte current, int i) {
  double ratio = (double) i / (double) strip.numPixels();
  return (current + (last > current ? 1 : -1) * (byte) (diffAbs(last, current) * ratio));
}

void renderLED(int i) {
  byte r = computeValueAt(lastColor.r, color.r, i);
  byte g = computeValueAt(lastColor.g, color.g, i);
  byte b = computeValueAt(lastColor.b, color.b, i);
  strip.setPixelColor(i, r, g, b);
  strip.show();
}

void renderLEDColor(int i, RGB color) {
  strip.setPixelColor(i, color.r, color.g, color.b);
  strip.show();
}
