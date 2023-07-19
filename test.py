from PIL import Image, ImageDraw, ImageFont  
import adafruit_ssd1306  
import board  
import digitalio  
from time import sleep  


oled=adafruit_ssd1306.SSD1306_SPI(128,64,board.SPI(),digitalio.DigitalInOut(board.D6),digitalio.DigitalInOut(board.D4),digitalio.DigitalInOut(board.D5)) 
#oled=adafruit_ssd1306.SSD1306_SPI(width,height,spi_interface,dc,rst,cs) 
oled.fill(0)  
oled.show()  
font=ImageFont.load_default()  
image=Image.new('1',(128,64))  
draw=ImageDraw.Draw(image)  
for i in range(40):  
	for j in range(56):  
		draw.text((i,j),"HELLO WORLD",font=font,fill=255)  
		oled.image(image)  
		led.show()  
		sleep(0.01)
		raw.text((i,j),"HELLO WORLD",font=font,fill=0)  
		led.image(image)  
		led.show()  
