import random
import math

def calc_distance(pos1, pos2):
  diff_x = pos1[0] - pos2[0]
  diff_y = pos1[1] - pos2[1]

  dis = math.sqrt(diff_x**2 + diff_y**2)
  return f'{dis:.1f}'

def generate_position(size):
  x = random.randrange(0, size)
  y = random.randrange(0, size)
  return (x, y)

def move_position(direction, pos):

      (current_x, current_y) = pos

      if direction == "n":
         current_y = current_y - 1

      elif direction == "s":
          current_y = current_y + 1

      elif direction == "e":
          current_x = current_x + 1

      elif direction == "w":
        current_x = current_x - 1

      return (current_x, current_y)

def suika(BOARD_SIZE):
    #スイカの位置を決める
    suika_pos = generate_position(BOARD_SIZE)

    #プレイヤーの位置を決める
    player_pos = generate_position(BOARD_SIZE)

    print("スイカを見つけて")

    while suika_pos != player_pos:

      distance = calc_distance(suika_pos, player_pos)
      print("スイカとの距離:", distance)

    #プレイヤーの移動処理
      c = input("n:北に移動 s:南に移動 e:東に移動 w:西に移動")
      
      player_pos = move_position(c, player_pos)

    print("スイカをはっけんしました。")
    return


suika(int(input("ボードサイズを選んでください")))