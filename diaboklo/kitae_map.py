import random
import keyboard
import time


# 전투 화면 출력 함수(몬스터)
def si_fight_screen(monster, si_monster_nowHp, si_monster_maxHp, si_choco):
    print('ㅡ' * 23)
    # 몬스터 출력
    print(f"{monster[0]}  HP: {si_monster_nowHp}/{si_monster_maxHp}")
    print('\n' * 5)
    # 초코의용군 상태 출력
    print(f"{si_choco[0]:>20}  HP: {si_choco[2][0]}/{si_choco[2][1]}")
    print(f"{'[포션(':>18}{si_choco[3]}개)] [엘릭서({si_choco[4]}개)]")
    print('ㅡ' * 23)


# 포션 사용 함수, y 포션 사용 선택시
def sy_potion(si_choco):
    print("포션을 사용합니다")
    si_choco[2][0] = si_choco[2][1]
    # 현재 hp => 최대 hp
    print("HP가 회복됩니다")
    print(f"{si_choco[0]:>20} {si_choco[2][0]}/{si_choco[2][1]}")
    # 포션 개수 차감
    si_choco[3] -= 1


# 전투 후 승리시 보상 함수
def sy_reward(si_choco):
    time.sleep(1)
    print("전투에서 승리했습니다")
    print("공격력과 HP가 5%씩 상승합니다")
    # 최소 공격력 5% 상승
    si_choco[1][0] += round(si_choco[1][0] * 0.05)
    # 최대 공격력 5% 상승
    si_choco[1][1] += round(si_choco[1][1] * 0.05)
    # 현재 HP 5% 상승
    si_choco[2][0] += round(si_choco[2][0] * 0.05)
    # 최대 HP 5% 상승
    si_choco[2][1] += round(si_choco[2][1] * 0.05)

    # 포션 랜덤 50% 획득
    potion = random.randint(1, 2)
    # 엘릭서는 포션 획득 시 랜덤 0.5% 획득
    elixir = random.randint(1, 1000)
    # 포션 획득 할 경우
    if potion == 1 and elixir > 5:
        print("포션을 획득했습니다")
        si_choco[3] += 1
    # 포션 얻은 후 엘릭서 획득 할 경우
    elif potion == 1 and elixir <= 5:
        print("엘릭서를 획득했습니다")
        si_choco[4] += 1
    # 포션 획득하지 못 할 경우
    else:
        print("포션을 획득하지 못했습니다")
    return si_choco


# 이벤트 발생 함수
def si_event_appear():
    print("!" * 37)
    print("!" * 37)
    print("!" * 37)
    print("!" * 37)
    print("!!!!!!!!!!!!!!!!몬스터!!!!!!!!!!!!!!!!")
    print("!" * 37)
    print("!" * 37)
    print("!" * 37)
    print("!" * 37)
    print()


# 몬스터 등장 함수
def si_monster_appear(si_monster_list):
    # 랜덤값 담아줄 변수
    si_monster_rate = random.randint(1, 100)
    # 몬스터 출현 함수호출
    si_event_appear()
    # 딜레이 1초
    time.sleep(1)

    # 좀비일 경우
    if si_monster_rate in range(1, 49):
        # 좀비가 나타났다 출력
        print(f"{si_monster_list[0][0]:>14}가 나타났다!")
        # '좀비' 반환
        return si_monster_list[0]
    # 구울일 경우
    if si_monster_rate in range(49, 79):
        # 구울이 나타났다 출력
        print(f"{si_monster_list[1][0]:>14}이 나타났다!")
        # '구울' 반환
        return si_monster_list[1]
    # 해골일 경우
    if si_monster_rate in range(79, 91):
        # 해골이 나타났다 출력
        print(f"{si_monster_list[2][0]:>14}이 나타났다!")
        # '해골' 반환
        return si_monster_list[2]
    # 버그베어일 경우
    if si_monster_rate in range(91, 96):
        # 버그베어가 나타났다 출력
        print(f"{si_monster_list[3][0]:>14}가 나타났다!")
        # '버그베어' 반환
        return si_monster_list[3]
    # 동혀니일 경우
    if si_monster_rate in range(96, 98):
        # 동혀니가 나타났다 출력
        print(f"{si_monster_list[4][0]:>14}가 나타났다!")
        # '동혀니' 반환
        return si_monster_list[4]
    # 홍거리일 경우
    if si_monster_rate in range(98, 100):
        # 홍거리가 나타났다 출력
        print(f"{si_monster_list[5][0]:>14}이가 나타났다!")
        # '홍거리' 반환
        return si_monster_list[5]
    # 디아복로일 경우
    if si_monster_rate in range(100, 101):
        # 디아복로가 나타났다 출력
        print(f"{si_monster_list[6][0]:>14}가 나타났다!")
        # '디아복로' 반환
        return si_monster_list[6]


# 엘릭서 사용 함수
def sy_elixir(si_choco):
    print("엘릭서를 사용합니다")
    elixir = 10
    print("10턴동안 무적")
    # 현재 hp = 최대 hp
    si_choco[2][0] = si_choco[2][1]
    print("HP가 회복됩니다")
    # 엘릭서 개수 차감
    si_choco[4] -= 1
    return elixir


# 몬스터 체력 설정 함수
def si_Monster_Hp(si_who_monster):
    # 몬스터 최대체력 랜덤값 받기
    si_monster_maxHp = random.randint(si_who_monster[3][0], si_who_monster[3][1])
    # 몬스터 현재체력
    si_monster_nowHp = si_monster_maxHp
    return si_monster_nowHp, si_monster_maxHp


# 전투 함수
def si_fight(si_who_monster, si_monster_nowHp, si_choco):
    # 좀비 - 등장확률: 48%, 공격력: 100, HP: 300~500
    si_zombie = ['좀비', 48, [100], [300, 500]]

    # 구울 - 등장활률 30%, 공격력: 180, HP: 450~700
    si_ghoul = ['구울', 30, [180], [450, 700]]

    # 해골 - 등장확률: 12% 공격력: 220, HP: 480~800
    si_skull = ['해골', 12, [220], [480, 800]]

    # 버그베어 - 등장확률: 5%, 공격력: 350, HP: 550~900
    si_bugbear = ['버그베어', 5, [350], [550, 900]]

    # 동혀니 - 등장확률: 2%, 공격력 1000 ~ 3000, HP 3000~8000
    si_donghyeon = ['동혀니', 2, [1000, 3000], [3000, 8000]]

    # 홍거리 - 등장확률 2%, 공격력 1000 ~ 3000, HP 3000~8000
    si_honggeol = ['홍거리', 2, [1000, 3000], [3000, 8000]]

    # 디아복로 - 등장확률 1%, 공격력 2500 ~ 8000, HP 5000~15000
    si_diaboklo = ['디아복로', 1, [2500, 8000], [5000, 15000]]

    # 몬스터 리스트 0= 좀비, 1= 구울, 2= 해골, 3= 버그베어, 4= 동혀니, 5= 홍거리, 6= 디아복로
    si_monster_list = [si_zombie, si_ghoul, si_skull, si_bugbear, si_donghyeon, si_honggeol, si_diaboklo]
    si_monster_Hp = []
    si_monster_maxHp = si_monster_nowHp


    # 초코의용 엘릭서 턴 초기화
    sy_elixir_turn = 0



    while True:
        # 무슨 행동을 할껀지 사용자에게 입력받기
        si_action = input(f"{'무엇을 할까?':>20}\n"
                          f"{'[1.공격]　[2.도망]':>23}\n"
                          f"{'[3.포션(':>12}{si_choco[3]}개)] [4.엘릭서({si_choco[4]}개)]\n"
                          f"{'ㅡ' * 23}\n"
                          f"숫자를 입력해주세요: ")
        # 공격 선택
        if si_action == '1':
            # 초코의용 공격력
            si_choco_power = random.randint(si_choco[1][0], si_choco[1][1])
            # 공격 데미지 출력
            print(f"초코의용이 공격합니다.\n"
                  f"{si_who_monster[0]}에게 {si_choco_power}의 데미지를 입혔습니다.")
            # 몬스터 현재체력에 초코의용의 공격력만큼 빼줌
            si_monster_nowHp -= si_choco_power
            # 전투화면 함수 호출
            si_fight_screen(si_who_monster, si_monster_nowHp, si_monster_maxHp, si_choco)
            # 몬스터 체력이 0과 같거나 작을 때
            if si_monster_nowHp <= 0:
                # 몬스터 처치 출력문
                print(f"{si_who_monster[0]}을(를) 처치했습니다.")
                si_choco = sy_reward(si_choco)
                # 처치한 몬스터가 디아복로면 엔딩
                if si_who_monster[0] == si_monster_list[6][0]:
                    print("디아복로를 처치하였습니다.")
                    # 엔딩함수 삽입 해야함
                break
        # 도망 선택
        elif si_action == '2':
            # 도망시도 출력물
            print("빤스런을 시도합니다.")
            # 1.5초 딜레이
            time.sleep(1.5)
            # 도망 확률: 80%
            si_pantierun_rate = random.randint(1, 100)
            # 도망 성공
            if si_pantierun_rate in range(1, 81):
                print("빤스런에 성공했습니다.")
                break
            # 도망 실패
            else:
                print("빤스런에 실패 하였습니다.")
        # 포션 선택
        elif si_action == '3':
            # 현재체력이 최대일 때
            if si_choco[2][0] == si_choco[2][1]:
                print("체력이 꽉 차있습니다.")
                # 전투화면 출력
                si_fight_screen(si_who_monster, si_monster_nowHp, si_monster_maxHp, si_choco)
            # 포션이 없을 때
            elif si_choco[3] == 0:
                print("포션이 없습니다.")
                # 전투화면 출력
                si_fight_screen(si_who_monster, si_monster_nowHp, si_monster_maxHp, si_choco)
            # 포션 사용
            else:
                # 포션사용 함수 호출
                sy_potion(si_choco)
                # 포션사용후 전투화면 출력
                si_fight_screen(si_who_monster, si_monster_nowHp, si_monster_maxHp, si_choco)
            continue
        # 엘릭서 선택
        elif si_action == '4':
            # 엘릭서가 없을 경우
            if si_choco[4] == 0:
                print("엘릭서가 없습니다.\n다시 입력해주세요.")
                # 전투화면 출력
                si_fight_screen(si_who_monster, si_monster_nowHp, si_monster_maxHp, si_choco)
                continue
            # 엘릭서 턴에 엘릭서 사용함수의 리턴값 담아주기
            sy_elixir_turn = sy_elixir(si_choco)
            # 엘릭서 사용 후 전투화면 출력
            # si_fight_screen(si_who_monster, si_monster_nowHp, si_monster_maxHp)
        # 범위 밖을 입력했을 경우
        else:
            print("다시 입력해주세요.")
            continue

        # 엘릭서 턴이 없을 경우 공격받게
        if sy_elixir_turn == 0:
            # 1.5초 딜레이
            time.sleep(1.5)
            # 몬스터가 좀비, 구울, 해골, 버그베어일 경우
            if si_who_monster in si_monster_list[0:4]:
                # 몬스터 공격력
                si_monster_power = si_who_monster[2][0]
            # 몬스터가 동혀니, 홍거리, 디아복로일 경우
            else:
                # 몬스터 공격력
                si_monster_power = random.randint(si_who_monster[2][0], si_who_monster[2][1])
            # 몬스터 공격 출력문
            print(f"{si_who_monster[0]}이(가) 공격합니다.\n"
                  f"{si_who_monster[0]}에게 {si_monster_power}의 데미지를 입었습니다.")
            # 초코의용의 현재 체력에서 몬스터의 공격력 빼주기
            si_choco[2][0] -= si_monster_power
            # 차감된 체력확인 하기 위한 전투화면 출력
            si_fight_screen(si_who_monster, si_monster_nowHp, si_monster_maxHp, si_choco)
            # 초코의용의 체력이 0과 같거나 작을 경우
            if si_choco[2][0] <= 0:
                # 초코의용 사망, 엔딩 출력
                print("초코의용이 사망했습니다.\nGame Over")
                break
        # 엘릭서 효과 받고 있을 때
        else:
            sy_elixir_turn -= 1  # 엘릭서 턴 차감
            # 1.5초 딜레이
            time.sleep(1.5)
            # 몬스터가 좀비, 구울, 해골, 버그베어일 경우
            if si_who_monster in si_monster_list[0:4]:
                # 몬스터 공격력
                si_monster_power = si_who_monster[2][0]
            # 몬스터가 동혀니, 홍거리, 디아복로일 경우
            else:
                # 몬스터 공격력
                si_monster_power = random.randint(si_who_monster[2][0], si_who_monster[2][1])
            # 몬스터 공격 출력문
            # 엘릭서 효과 출력
            print(f"{si_who_monster[0]}이(가) 공격합니다.\n"
                  f"엘릭서의 효과로 데미지를 입지 않습니다.\n"
                  f"{si_monster_power}의 데미지를 방어했습니다.\n"
                  f"남은 엘릭서 효과: {sy_elixir_turn}")
            # 차감되지 않은 체력확인을 위한 전투화면 출력
            si_fight_screen(si_who_monster, si_monster_nowHp, si_monster_maxHp, si_choco)


def battle(si_choco):
    # 좀비 - 등장확률: 48%, 공격력: 100, HP: 300~500
    si_zombie = ['좀비', 48, [100], [300, 500]]

    # 구울 - 등장활률 30%, 공격력: 180, HP: 450~700
    si_ghoul = ['구울', 30, [180], [450, 700]]

    # 해골 - 등장확률: 12% 공격력: 220, HP: 480~800
    si_skull = ['해골', 12, [220], [480, 800]]

    # 버그베어 - 등장확률: 5%, 공격력: 350, HP: 550~900
    si_bugbear = ['버그베어', 5, [350], [550, 900]]

    # 동혀니 - 등장확률: 2%, 공격력 1000 ~ 3000, HP 3000~8000
    si_donghyeon = ['동혀니', 2, [1000, 3000], [3000, 8000]]

    # 홍거리 - 등장확률 2%, 공격력 1000 ~ 3000, HP 3000~8000
    si_honggeol = ['홍거리', 2, [1000, 3000], [3000, 8000]]

    # 디아복로 - 등장확률 1%, 공격력 2500 ~ 8000, HP 5000~15000
    si_diaboklo = ['디아복로', 1, [2500, 8000], [5000, 15000]]

    # 몬스터 리스트 0= 좀비, 1= 구울, 2= 해골, 3= 버그베어, 4= 동혀니, 5= 홍거리, 6= 디아복로
    si_monster_list = [si_zombie, si_ghoul, si_skull, si_bugbear, si_donghyeon, si_honggeol, si_diaboklo]
    si_monster_Hp = []

    # 어떤 몬스터가 출현했는지 리턴값 저장하기
    si_who_monster = si_monster_appear(si_monster_list)
    # 몬스터 Hp 담아주기
    si_monster_Hp = list(si_Monster_Hp(si_who_monster))
    # 전투 화면 함수 호출(매개변수: 몬스터 등장 리턴값)
    si_fight_screen(si_who_monster, si_monster_Hp[0], si_monster_Hp[1], si_choco)
    # 전투 함수 호출
    si_fight(si_who_monster, si_monster_Hp[0], si_choco)


# -------------------------------------------- 아래부터 던전 함수 ---------------------------------------------------------


# 던전 만드는 함수, 변수들 앞에 이니셜 mm 붙임
def make_maze():
    # 10 x 10(임의)로 행렬 크기 설정
    cols = 10
    rows = 10
    # cols, rows 행변수, 열변수의 값만큼 행렬 크기를 설정한 값을 maze 변수에 넣음
    mm_maze = [["X" for j in range(cols)] for i in range(rows)]

    # 던전 좌표마다 랜덤 값 부여
    for mm_x in range(10):
        for mm_y in range(10):
            # 0은 아무 이벤트 없음, 1은 몬스터 출현, 2는 포션
            mm_event = random.randint(0, 2)
            if mm_event == 0:
                mm_maze[mm_x][mm_y] = '⬜'
            elif mm_event == 1:
                mm_maze[mm_x][mm_y] = '😈'
            elif mm_event == 2:
                mm_maze[mm_x][mm_y] = '🍖'

    # 10x10의 테두리 '🏔'로 지정
    for mm_x in range(len(mm_maze)):  # 상단 테두리
        mm_maze[mm_x][0] = '🏔'
    for mm_x in range(len(mm_maze)):  # 좌측 테두리
        mm_maze[0][mm_x] = '🏔'
    for mm_x in range(len(mm_maze)):  # 우측 테두리
        mm_maze[len(mm_maze) - 1][mm_x] = '🏔'
    for mm_x in range(len(mm_maze)):  # 아래 테두리
        mm_maze[mm_x][len(mm_maze) - 1] = '🏔'
    return mm_maze


# 던전 출력 함수
def print_map(pm_maze, si_choco):
    # 현재 상태 창
    print('ㅡ' * 23)
    print(f"{si_choco[0]} HP: {si_choco[2][0]}/{si_choco[2][1]}  공격력: {si_choco[1][0]}/{si_choco[1][1]}")
    print(f"포션: {si_choco[3]}개 엘릭서: {si_choco[4]}개")
    print('ㅡ' * 23)
    # 10 x 10(임의)로 행렬 크기 설정
    cols = 10
    rows = 10

    # 랜덤으로 뽑은 a, b를 인덱스 값으로 지정해서 포탈을 생성해 줍니다
    potal_a = random.randrange(1, 9)
    potal_b = random.randrange(1, 9)

    pm_maze[potal_a][potal_b] = '🚪'

    # (1, 1)자리에 스폰
    mx = 1
    my = 1
    pm_maze[mx][my] = "😊"

    # 그림자를 씌울 shadow_maze 변수
    shadow_maze = [["X" for j in range(cols)] for i in range(rows)]
    for x in range(10):
        for y in range(10):
            shadow_maze[x][y] = ('\033[100m' + '☁' + '\033[0m')

    # 던전을 3개 만들었습니다.
    maze1 = make_maze()
    maze2 = make_maze()
    maze3 = make_maze()

    map_list = [maze1, maze2, maze3]

    # 맵 출력
    for i in range(10):
        for j in range(10):
            # 주인공 주변 3x3만 보이게 출력
            if (i == (mx - 1) and j == (my - 1)) or (i == mx and j == (my - 1)) or (i == (mx + 1) and j == (my - 1)) \
                    or (i == (mx - 1) and j == my) or (i == mx and j == my) or (i == (mx + 1) and j == my) \
                    or (i == (mx - 1) and j == (my + 1)) or (i == mx and j == (my + 1)) or (
                    i == (mx + 1) and j == (my + 1)):
                print(pm_maze[i][j], end='')
            # 주인공 주변 3x3이 아니면 그림자 출력
            else:
                print(shadow_maze[i][j], end='')
        print()
    print('ㅡ' * 23)

    cnt = 0

    while 1:
        print()
        # 키보드 입력
        while 1:
            if keyboard.is_pressed('Up'):
                key = 'up'
                time.sleep(0.1)
                break
            elif keyboard.is_pressed('Down'):
                key = 'down'
                time.sleep(0.1)
                break
            elif keyboard.is_pressed('Left'):
                key = 'left'
                time.sleep(0.1)
                break
            elif keyboard.is_pressed('Right'):
                key = 'right'
                time.sleep(0.1)
                break

        # 위로 이동
        if key == "up" and pm_maze[mx - 1][my] != '🏔':
            # 기존 주인공 자리 0으로 초기화
            pm_maze[mx][my] = '⬜'
            print(f'{"<위로 전진!>":^33}')
            # 이동하는 곳의 값이 1이면 몬스터 이벤트 발생
            if pm_maze[mx - 1][my] == '😈':
                battle(si_choco)
            # 이동하는 곳의 값이 P이면 포탈 이벤트 발생
            elif pm_maze[mx - 1][my] == '🚪':
                print(f'{"<다음 던전으로 이동합니다...>":^33}')
                # 다음 던전으로 랜덤 이동
                a = random.choice(map_list)
                print(f"{map_list.index(a) + 1:>15}번째 맵입니다")
                return print_map(a)
            # 이동하는 곳의 값이 2면 포션 획득
            elif pm_maze[mx - 1][my] == '🍖':
                print(f'{"<포션을 획득했습니다!>":^33}')
                si_choco[3] += 1
            mx -= 1
            cnt += 1
        # 왼쪽 이동
        elif key == "left" and pm_maze[mx][my - 1] != '🏔':
            # 기존 주인공 자리 0으로 초기화
            pm_maze[mx][my] = '⬜'
            print(f'{"<왼쪽으로 전진!>":^33}')
            # 이동하는 곳의 값이 1이면 몬스터 이벤트 발생
            if pm_maze[mx][my - 1] == '😈':
                battle(si_choco)
            # 이동하는 곳의 값이 P이면 포탈 이벤트 발생
            elif pm_maze[mx][my - 1] == '🚪':
                print(f'{"<다음 던전으로 이동합니다...>":^33}')
                # 다음 던전으로 랜덤 이동
                a = random.choice(map_list)
                print(f"{map_list.index(a) + 1:>15}번째 맵입니다")
                return print_map(a)
            # 이동하는 곳의 값이 2면 포션 획득
            elif pm_maze[mx][my - 1] == '🍖':
                print(f'{"<포션을 획득했습니다!>":^33}')
                si_choco[3] += 1
            my -= 1
            cnt += 1
        # 아래 이동
        elif key == "down" and pm_maze[mx + 1][my] != '🏔':
            # 기존 주인공 자리 0으로 초기화
            pm_maze[mx][my] = '⬜'
            print(f'{"<아래로 전진!>":^33}')
            # 이동하는 곳의 값이 1이면 몬스터 이벤트 발생
            if pm_maze[mx + 1][my] == '😈':
                battle(si_choco)
            # 이동하는 곳의 값이 P이면 포탈 이벤트 발생
            elif pm_maze[mx + 1][my] == '🚪':
                print(f'{"<다음 던전으로 이동합니다...>":^33}')
                # 다음 던전으로 랜덤 이동
                a = random.choice(map_list)
                print(f"{map_list.index(a) + 1:>15}번째 맵입니다")
                return print_map(a)
            # 이동하는 곳의 값이 2면 포션 획득
            elif pm_maze[mx + 1][my] == '🍖':
                print(f'{"<포션을 획득했습니다!>":^33}')
                si_choco[3] += 1
            mx += 1
            cnt += 1
        # 오른쪽 이동
        elif key == "right" and pm_maze[mx][my + 1] != '🏔':
            # 기존 주인공 자리 0으로 초기화
            pm_maze[mx][my] = '⬜'
            print(f'{"<오른쪽으로 전진!>":^33}')
            # 이동하는 곳의 값이 1이면 이벤트 발생
            if pm_maze[mx][my + 1] == '😈':
                battle(si_choco)
            # 이동하는 곳의 값이 P이면 포탈 이벤트 발생
            elif pm_maze[mx][my + 1] == '🚪':
                print(f'{"<다음 던전으로 이동합니다...>":^33}')
                # 다음 던전으로 랜덤 이동
                a = random.choice(map_list)
                print(f"{map_list.index(a) + 1:>15}번째 맵입니다")
                return print_map(a)
            # 이동하는 곳의 값이 2면 포션 획득
            elif pm_maze[mx][my + 1] == '🍖':
                print(f'{"<포션을 획득했습니다!>":^33}')
                si_choco[3] += 1
            my += 1
            cnt += 1
        # 이동 불가
        else:
            print(f'{"그 쪽으론 갈 수 없습니다.":^33}')

        if cnt == 3:
            pm_maze = make_maze()
            pm_maze[potal_a][potal_b] = '🚪'
            cnt = 0
            print(f'{"던전의 모양이 바꼈습니다!":^33}')
        pm_maze[mx][my] = "😊"
        # 현재 상태 창
        print('ㅡ' * 23)
        print(f"{si_choco[0]} {si_choco[2][0]}/{si_choco[2][1]}  공격력: {si_choco[1][0]}/{si_choco[1][1]}")
        print(f"포션: {si_choco[3]} 엘릭서: {si_choco[4]}")
        print('ㅡ' * 23)
        # 이동한 맵 출력
        for i in range(10):
            for j in range(10):
                if (i == (mx - 1) and j == (my - 1)) or (i == mx and j == (my - 1)) or (i == (mx + 1) and j == (my - 1)) \
                        or (i == (mx - 1) and j == my) or (i == mx and j == my) or (i == (mx + 1) and j == my) \
                        or (i == (mx - 1) and j == (my + 1)) or (i == mx and j == (my + 1)) or (
                        i == (mx + 1) and j == (my + 1)):
                    print(pm_maze[i][j], end='')
                else:
                    print(shadow_maze[i][j], end='')
            print()
        print('ㅡ' * 23)


def main():
    print(f'{"<초코의용군의 대모험!>":^33}')
    maze = make_maze()
    si_choco = ['초코의용군', [100, 150], [500, 500], 3, 3]
    print_map(maze, si_choco)


main()