############# 버튼 #############
class Button:
  def click(slef):
    pass
  
class DarkButton(Button):
  def click(slef):
    print("dark click")
    
class LightButton(Button):
  def click(slef):
    print("light click")

class RedButton(Button):
  def click(slef):
    print("red click")
    
class BlueButton(Button):
  def click(slef):
    print("blue click")
    

############# 체크박스 #############
class CheckBox:
  def check(self):
    pass
  
class DarkCheckBox(CheckBox):
  def check(self):
    print("dark check")
    
class LightCheckBox(CheckBox):
  def check(self):
    print("light check")
    
class RedCheckBox(CheckBox):
  def check(self):
    print("red check")
    
class BlueCheckBox(CheckBox):
  def check(self):
    print("blue check")

############# 스크롤 #############
class ScrollBar:
  def scroll(self):
    pass
  
class DarkScrollBar(ScrollBar):
  def scroll(self):
    print("dark scroll")
    
class LightScrollBar(ScrollBar):
  def scroll(self):
    print("light scroll")
    
class RedScrollBar(ScrollBar):
  def scroll(self):
    print("red scroll")
    
class BlueScrollBar(ScrollBar):
  def scroll(self):
    print("blue scroll")

############# 슬라이더 #############
class Slider:
  def slider(self):
    pass
  
class DarkSlider(Slider):
  def slider(self):
    print("dark slider")
    
class LightSlider(Slider):
  def slider(self):
    print("light slider")
    
class RedSlider(Slider):
  def slider(self):
    print("red slider")
    
class BlueSlider(Slider):
  def slider(self):
    print("blue slider")
############# 텍스트박스 #############
class TextBox:
  def textbox(self):
    pass
  
class DarkTextBox(TextBox):
  def textbox(self):
    print("dark textbox")
    
class LightTextBox(TextBox):
  def textbox(self):
    print("light textbox")
    
class RedTextBox(TextBox):
  def textbox(self):
    print("red textbox")
    
class BlueTextBox(TextBox):
  def textbox(self):
    print("blue textbox")

############# UIFactory #############
class UIFactory():
  def getButton(self):
    pass
  
  def getCheck(self):
    pass
  
  def getScroll(self):
    pass
  
  def getSlider(self):
    pass
  
  def getText(self):
    pass

############# DarkFactory #############
class DarkFactory(UIFactory):
  def getButton(self):
    return DarkButton()
  
  def getCheck(self):
    return DarkCheckBox()
  
  def getScroll(self):
    return DarkScrollBar()
  
  def getSlider(self):
    return DarkSlider()
  
  def getText(self):
    return DarkTextBox()
  
############# LightFactory #############
class LightFactory(UIFactory):
  def getButton(self):
    return LightButton()
  
  def getCheck(self):
    return LightCheckBox()
  
  def getScroll(self):
    return LightScrollBar()
  
  def getSlider(self):
    return LightSlider()
  
  def getText(self):
    return LightTextBox()
  
############# RedFactory #############
class RedFactory(UIFactory):
  def getButton(self):
    return RedButton()
  
  def getCheck(self):
    return RedCheckBox()
  
  def getScroll(self):
    return RedScrollBar()
  
  def getSlider(self):
    return RedSlider()
  
  def getText(self):
    return RedTextBox()
  
############# BlueFactory #############
class BlueFactory(UIFactory):
  def getButton(self):
    return BlueButton()
  
  def getCheck(self):
    return BlueCheckBox()
  
  def getScroll(self):
    return BlueScrollBar()
  
  def getSlider(self):
    return BlueSlider()
  
  def getText(self):
    return BlueTextBox()

######################################
if __name__ == "__main__":
  # DarkFactory 실행
  print("DarkFactory 실행")
  darkfact = DarkFactory()
  dbt = darkfact.getButton()
  dck = darkfact.getCheck()
  dsc = darkfact.getScroll()
  dsd = darkfact.getSlider()
  dtb = darkfact.getText()

  dbt.click()
  dck.check()
  dsc.scroll()
  dsd.slider()
  dtb.textbox()
  print()

  # LightdFactory 실행
  print("LightFactory 실행")
  lightfact = LightFactory()
  lbt = lightfact.getButton()
  lck = lightfact.getCheck()
  lsc = lightfact.getScroll()
  lsd = lightfact.getSlider()
  ltb = lightfact.getText()

  lbt.click()
  lck.check()
  lsc.scroll()
  lsd.slider()
  ltb.textbox()
  print()

  # RedFactory 실행
  print("RedFactory 실행")
  redfact = RedFactory()
  rbt = redfact.getButton()
  rck = redfact.getCheck()
  rsc = redfact.getScroll()
  rsd = redfact.getSlider()
  rtb = redfact.getText()

  rbt.click()
  rck.check()
  rsc.scroll()
  rsd.slider()
  rtb.textbox()
  print()

  # BlurFactory 실행
  print("BlueFactory 실행")
  bluefact = BlueFactory()
  bbt = bluefact.getButton()
  bck = bluefact.getCheck()
  bsc = bluefact.getScroll()
  bsd = bluefact.getSlider()
  btb = bluefact.getText()

  bbt.click()
  bck.check()
  bsc.scroll()
  bsd.slider()
  btb.textbox()