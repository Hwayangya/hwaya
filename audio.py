import pygame
import os

# MP3 파일 재생을 위한 초기화
pygame.mixer.init()

# MP3 파일 경로
mp3_files = {
    "1": "1.mp3",
    "2": "2.mp3",
    "3": "3.mp3",
    "4": "4.mp3",
    "5": "5.mp3"
}

def play_mp3(file_name):
    """MP3 파일을 재생하는 함수"""
    if os.path.exists(file_name):
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play()
        print(f"{file_name} 재생 중... 'Ctrl+C'를 눌러 종료하거나 곡 재생이 끝날 때까지 기다리세요.")
        while pygame.mixer.music.get_busy():
            continue
    else:
        print(f"파일 '{file_name}'을(를) 찾을 수 없습니다.")

def main():
    """메인 프로그램"""
    while True:
        print("1, 2, 3, 4, 5 중 하나를 입력하여 MP3를 재생하세요. 종료하려면 'q'를 입력하세요.")
        choice = input("선택: ").strip()
        if choice == 'q':
            print("프로그램을 종료합니다.")
            break
        elif choice in mp3_files:
            play_mp3(mp3_files[choice])
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()
