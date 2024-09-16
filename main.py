from time import sleep
import pygame
import random
import sys
from pygame.locals import *

store = [0, 0, 0, 0, 0, 0, 0] # 存储已选择物品的列表
windows_width = 600      # 窗口大小
windows_height = 900     # 窗口大小
icoSize = 48             # 图像大小
patterns = [pygame.image.load(f"pattern/T_animals_{i}.png") for i in range(1, 24)]
sheepList = [pygame.transform.smoothscale(p, (icoSize, icoSize)) for p in patterns]

# 定义点类，用于存储坐标
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# 判断每回合消除结果
def judge(x, storeCount):

    global store
    y = 0
    for i in range(storeCount):
        if store[i] == 0:
            store[i] = x
            break

    # 比较是否有三个图案相等
    cnt = 0
    for i in range(storeCount):
        if store[i] == x:
            cnt += 1
    if cnt == 3:           # 消除成功
        y = 1
        for i in range(storeCount):
            if store[i] == x:
                store[i] = 0
    return y
# 游戏开始界面
def main():
    pygame.init()
    playSurface = pygame.display.set_mode((windows_width, windows_height))  # 设置屏幕大小

    font = pygame.font.Font("钉钉进步体 DingTalkJinBuTi/DingTalkJinBuTi-Regular.ttf", 36)  # 渲染文本

    background_image = pygame.image.load(f"pattern/illustration_1.png")

    # 填充背景色
    playSurface.fill(color="antiquewhite")
    # 确保图片大小与屏幕一致
    background_image = pygame.transform.scale(background_image, (177.5*2.5, 210.8*2.5))
    playSurface.blit(background_image, ((windows_width-177.5*2.5)/2, (windows_height-250.8*2.5)/2))
    # 更新屏幕
    pygame.display.update()
    pygame.display.set_caption("Pygame Button Example")

    # 定义按钮参数：颜色、文本
    button_color = (250,128,114)
    button_rect = pygame.Rect(windows_width/2-100, windows_height/2+220,200,76)
    button_text = '开始游戏'

    # 定义按钮功能
    def draw_button():
        pygame.draw.rect(playSurface, button_color, button_rect)
        text_surface = font.render(button_text, True, (0,0,0))
        text_rect = text_surface.get_rect(center=button_rect.center)
        playSurface.blit(text_surface, text_rect)
        pygame.display.update()

    # 按钮点击功能
    def handle_click(pos):
        if button_rect.collidepoint(pos):
            print("Button clicked, function ending.")
            return True
        return False

    # 主循环，判断鼠标点击是否到按钮
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if handle_click(event.pos):
                    running = False

        draw_button()
        pygame.display.flip()
    pygame.quit()

# 游戏界面
def main1():
    # 初始化变量
    totalScore = 0    # 总分
    score = 0         # 每关分数
    itemCount = 8     # 初始物种数
    Level = 1         # 关卡等级
    storeCount = 5    # 家庭初始容量
    pygame.init() # 初始化pygame
    pygame.mixer.init()  # 初始化音频
    playSurface = pygame.display.set_mode((windows_width, windows_height))  # 设置屏幕大小

    font = pygame.font.Font("钉钉进步体 DingTalkJinBuTi/DingTalkJinBuTi-Regular.ttf", 36)  # 渲染文本

    # 加载音频文件
    sound = pygame.mixer.Sound(f"sound/button_1.wav")

    # 设置倒计时时间（秒）
    countdown_time = 30
    start_time = pygame.time.get_ticks()

    data = [[i + 1 for i in range(4)] for j in range(4)]
    data1 = [[i + 1 for i in range(4)] for j in range(4)]
    # 生成一个矩阵，并随机打乱——第一层
    for r in range(4):
        for c in range(4):
            r1 = random.randint(1, 100) % 4;
            c1 = random.randint(1, 100) % 4;
            t = data[r1][c1];
            data[r1][c1] = data[r][c];
            data[r][c] = t;
    # 生成一个矩阵，并随机打乱——第二层
    for r in range(4):
        for c in range(4):
            r1 = random.randint(1, 100) % 4;
            c1 = random.randint(1, 100) % 4;
            t = data1[r1][c1];
            data1[r1][c1] = data[r][c];
            data1[r][c] = t;

    # 计算图标位置和偏移
    offsetX = (windows_width - (3 * (48 + icoSize) + 48)) / 2
    offsetY = (windows_height - (3 * (48 + icoSize) + 48)) / 2
    end = 0

    while True:
        # 计算时间
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        remaining_time = countdown_time - elapsed_time
        if remaining_time <= 0:
            remaining_time = 0
            end = 1  # 结束主循环

        # 更新屏幕
        pygame.display.update()
        # 填充背景色
        playSurface.fill(color="antiquewhite")

        # 绘制文本
        color = (0, 176, 170)
        s = "关卡            ：" + str(Level)
        text = font.render(s, True, color)
        playSurface.blit(text, (5, 45))

        color = (104, 47, 99)
        text = font.render("物种类型: " + str(itemCount), True, color)
        playSurface.blit(text, (5, 115))

        color = (255, 63, 63)
        text = font.render("当前分数    : " + str(totalScore), True, color)
        playSurface.blit(text, (5, 80))

        color = (63, 255, 255)
        text = font.render(f"剩余时间: {remaining_time:.1f}", True, color)
        playSurface.blit(text, (5, 150))

        color = (0, 176, 170)
        text = font.render("家园容量：" + str(storeCount),True, color)
        playSurface.blit(text, (5, 700))

        # 绘制游戏板上的图标
        sheepList1 = [pygame.transform.smoothscale(p, (30, 30)) for p in sheepList]
        for r in range(4):
            for c in range(4):
                if (data[r][c]):
                    playSurface.blit(sheepList[data[r][c]-1],(offsetX + c * (48 + icoSize), offsetY + r * (48 + icoSize)))
                    playSurface.blit(sheepList1[data1[r][c]-1],
                                     (offsetX + 40 + c * (48 + icoSize), offsetY + 40 + r * (48 + icoSize)))


        # 绘制已选择物种
        count = 0                 # 用来保证已选择物种紧密排列在左侧
        for i in range(storeCount):
            if store[i]:
                playSurface.blit(sheepList[store[i] - 1], ((count * 50) + 50, 750))
                count += 1
        pygame.display.update()
                # Rect(x, y, width, height)，其中(x, y)是矩形左上角的坐标，width和height分别是矩形的宽度和高度。
        # 结束模块
        if (end == 1):
            print("游戏结束")
            color = (255, 0, 0)
            text = font.render("游戏结束", True, color)
            title_text_rect = text.get_rect(center=(windows_width // 2,210))  # 高度自定义
            playSurface.blit(text, title_text_rect)
            pygame.display.update()

            # 播放游戏结束音频文件
            sound = pygame.mixer.Sound(f"sound/game_over.wav")
            sound.play()

            sleep(1)
            break
        # 处理事件
        for event in pygame.event.get():
            msg = Point()
            if event.type == MOUSEBUTTONUP:  # 获取鼠标位置
                (x, y) = event.pos
                print(x, y)
                msg = Point(x, y)
            else:
                continue
            # 检测鼠标点击是否在图标上
            for r in range(4):
                for c in range(4):
                    x = offsetX + c * (48 + icoSize)
                    y = offsetY + r * (48 + icoSize)

                    if msg.x > x and msg.x < x + 48 and msg.y > y and msg.y < y + 48:

                        col = int((msg.x - offsetX) / (48 + icoSize))
                        row = int((msg.y - offsetY) / (48 + icoSize))
                        print("row:", row, col);


                        y = judge(data[row][col],storeCount)  # 判断结果
                        if y == 1:       # 如果出现消除
                            # 播放音频文件
                            sound.play()

                            score += 1
                            totalScore += 1
                            if score == 5:
                                Level += 1
                                countdown_time += 10
                                if itemCount < 24:         # 难度上限，之后是无尽模式
                                    itemCount += 1
                                if Level == 8 or itemCount == 16:  # 奖励机制，容量增加
                                    storeCount += 1
                                score = 0
                        else:  # 如果容量满了就结束
                            end = 1
                            for i in range(storeCount):
                                if store[i] == 0:
                                    end = 0
                                    break

                        data[row][col] = data1[row][col]
                        data1[row][col] = random.randint(1, 100) % itemCount + 1
    return totalScore
# 结束界面
def main2(totalScore):
    pygame.init()
    playSurface = pygame.display.set_mode((windows_width, windows_height))  # 设置屏幕大小

    font = pygame.font.Font("钉钉进步体 DingTalkJinBuTi/DingTalkJinBuTi-Regular.ttf", 36)  # 渲染文本

    background_image = pygame.image.load(f"pattern/illustration_1.png")

    # 填充背景色
    playSurface.fill(color="antiquewhite")
    # 确保图片大小与屏幕一致
    background_image = pygame.transform.scale(background_image, (177.5*2.5, 210.8*2.5))
    playSurface.blit(background_image, ((windows_width-177.5*2.5)/2, (windows_height-250.8*2.5)/2))
    color = (255, 0, 0)
    text = font.render("游戏结束,你的最终得分是:" + str(totalScore) + " 分！", True, color)
    title_text_rect = text.get_rect(center=(windows_width // 2, 100))  # 高度自定义
    playSurface.blit(text, title_text_rect)
    pygame.display.update()
    # 更新屏幕
    pygame.display.update()
    pygame.display.set_caption("Pygame Button Example")

    # 定义按钮颜色
    button_color = (250,128,114)

    def draw_button(button_rect,button_text):
        pygame.draw.rect(playSurface, button_color, button_rect)
        text_surface = font.render(button_text, True, (0,0,0))
        text_rect = text_surface.get_rect(center=button_rect.center)
        playSurface.blit(text_surface, text_rect)
        pygame.display.update()

    # 按钮点击功能——再来一次/结束游戏
    def handle_click(button_rect,pos):
        if button_rect.collidepoint(pos):
            print("Button clicked, function ending.")
            return True
        return False

    def handle_click1(button_rect1,pos):
        if button_rect1.collidepoint(pos):
            print("Button1 clicked, function ending.")
            return True
        return False

    button_rect = pygame.Rect(windows_width / 2 - 250, windows_height / 2 + 220, 200, 76)
    button_text = '再来一次'
    draw_button(button_rect,button_text)
    button_rect1 = pygame.Rect(windows_width / 2 + 50, windows_height / 2 + 220, 200, 76)
    button_text = '结束游戏'
    draw_button(button_rect1,button_text)
    pygame.display.flip()
    running = True
    y = 1                         # 判断再来一次还是结束游戏
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if handle_click(button_rect,event.pos):
                    running = False
                    y = 1
                elif handle_click1(button_rect1,event.pos):
                    running = False
                    y = 0
    pygame.quit()
    return y

if __name__ == "__main__":
    main()
    store = [0, 0, 0, 0, 0, 0, 0, 0]  # 存储已选择物品的列表
    totalScore = main1()
    y = main2(totalScore)
    print(y)
    while y:
        store = [0, 0, 0, 0, 0, 0, 0]
        totalScore = main1()
        y = main2(totalScore)
