# 수학과 프로그래밍 기말 프로젝트
# Penguin Ice Adventure

파이썬으로 만든 펭귄이 전진하는 게임입니다.
난이도 선택, 점프 기능, 체력 시스템, 레벨업, 최고 점수 기능까지 구현된 최종 버전입니다.

기능
메인 메뉴 (로비)  
난이도 선택 (Easy / Normal / Hard)  
점프 기능 (스페이스바)  
체력(HP) 시스템
레벨업 (속도 증가)  
최고 점수 기록  
생선 아이템 (점수 +5)  
게임 오버 시 로비로 자동 복귀

조작법
| 1   | Start Game (로비 메뉴) |
| 2   | Quit (로비 메뉴) |
| 1/2/3 | 난이도 선택 (Easy/Normal/Hard) |
| ← → | 펭귄 좌우 이동 |
| SPACE | 점프 |
| ESC / 창 닫기 | 종료 |

Folder Structure
finalproject/
├── penguin_game.py
├── README.md
└── assets/
    ├── penguin.png
    ├── snow_bg.png
    ├── rock.png
    ├── fish.png

How to Run
1.파이썬 설치 (Python 3.8 이상 권장)  
2.`pygame` 설치:
pip install pygame
3.실행
python penguin_game.py
