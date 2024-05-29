# 関数内関数
def outer(func):
  def inner(*args, **kwargs):
    print('===開始===')
    func(*args, **kwargs)
    print('===終了===')
  return inner

# タプル
nums = (10, 20, 30, 40)
@outer
def show_num(nums):
  sum = 0
  for num in nums:
    sum += num
  print(sum)

# 辞書
users = {'山田': 30, '田中': 40, '中村': 50}
@outer
def show_info(users):
  for name, age in users.items():
    print(f'名前:{name}, 年齢:{age}')

show_num(nums)
show_info(users)
