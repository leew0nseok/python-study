chosung_list = [u'ㄱ',u'ㄲ',u'ㄴ',u'ㄷ',u'ㄸ',u'ㄹ',u'ㅁ',u'ㅂ',u'ㅃ',u'ㅅ',u'ㅆ',u'ㅇ',u'ㅈ',u'ㅉ',u'ㅊ',u'ㅋ',u'ㅌ',u'ㅍ',u'ㅎ']
jungsung_list = [u'ㅏ',u'ㅐ',u'ㅑ',u'ㅒ',u'ㅓ',u'ㅔ',u'ㅕ',u'ㅖ',u'ㅗ',u'ㅘ',u'ㅙ',u'ㅚ',u'ㅛ',u'ㅜ',u'ㅝ',u'ㅞ',u'ㅟ',u'ㅠ',u'ㅡ',u'ㅢ',u'ㅣ']
jongsung_list = [u'',u'ㄱ',u'ㄲ',u'ㄳ',u'ㄴ',u'ㄵ',u'ㄶ',u'ㄷ',u'ㄹ',u'ㄺ',u'ㄻ',u'ㄼ',u'ㄽ',u'ㄾ',u'ㄿ',u'ㅀ',u'ㅁ',u'ㅂ',u'ㅄ',u'ㅅ',u'ㅆ',u'ㅇ',u'ㅈ',u'ㅊ',u'ㅋ',u'ㅌ',u'ㅍ',u'ㅎ']

# 자모분리
def jamo_split(word):
    
    result = []
    # 문자열을 문자 단위로 
    for char in word:
        
        character_code = ord(char) # ord함수는 문자의 순서 위치 값을 반환(아스키코드)
        
        # 아스키코드로 한글영역 범위: 0xAC00 ~ 0xD7A3
        # 따라서 아래 조건문은 한글이 아닐경우 실행되는 코드
        if 0xD7A3 < character_code or character_code < 0xAC00:
            result.append(char)
            continue

        # 한글인 경우 아스키코드를 이용해 초성, 중성, 종성의 인덱스 계산 
        # 한글은 초성 19개, 중성 21개, 종성 28개로 이루어져 있음.
        # (character_code - 0xAC00) 0xAC00을 기준으로 한글문자의 상대적인 위치를 나타냄

        chosung_index = int((((character_code - 0xAC00) / 28) / 21) % 19) # 초성을 계산하기위해 28로 나눈뒤 21로 나눈뒤 19로 나눈 나머지 값
        jungsung_index = int(((character_code - 0xAC00) / 28) % 21) # 중성을 계산하기 위해 28로 나눈뒤 21로 나눈 나머지 값
        jongsung_index = int((character_code - 0xAC00) % 28) # 종성 계산을 위해 28로 나눔
        
        # 계산된 인덱스를 이용 -> 각 list에서 해당하는 값을 가져옴
        chosung = chosung_list[chosung_index]
        joongsung = jungsung_list[jungsung_index]
        jongsung = jongsung_list[jongsung_index]
        
        result.append(chosung)
        result.append(joongsung)
        result.append(jongsung)

    return "".join(result)

sentence = "안녕하세요"
print(jamo_split(sentence))